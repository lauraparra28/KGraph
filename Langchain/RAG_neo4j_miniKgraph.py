import os, json, random
import torch
import sentence_transformers
import networkx as nx
from neo4j import GraphDatabase, Result
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain.prompts.prompt import PromptTemplate
from langchain_community.vectorstores import Neo4jVector
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from httpx import Client
from configparser import ConfigParser, ExtendedInterpolation
from utils import base_utils as bu

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read('config-v1.x.ini', 'UTF-8')

CERTIFICATE_PATH = 'petrobras-ca-root.pem'
OPENAI_BASE_URL = config['OPENAI']['AZURE_OPENAI_BASE_URL']
DEPLOYMENT_NAME = config['OPENAI']['CHATGPT_MODEL']
OPENAI_API_VERSION = '2024-03-01-preview'
cypher_generation_template = config['PROMPTS']['CYPHER_GENERATION_TEMPLATE']
qa_generation_template = config['PROMPTS']['QA_PROMPT']

llm_petrobras = AzureChatOpenAI(
    model=DEPLOYMENT_NAME,
    openai_api_version=OPENAI_API_VERSION,
    openai_api_key=config['OPENAI']['OPENAI_API_KEY'],
    base_url=f"{OPENAI_BASE_URL}/{DEPLOYMENT_NAME}",
    http_client=Client(verify=CERTIFICATE_PATH)
)

EMBEDDINGS_DEPLOYMENT_NAME='text-embedding-petrobras'
embeddings = AzureOpenAIEmbeddings(
    model=EMBEDDINGS_DEPLOYMENT_NAME,
    openai_api_version=OPENAI_API_VERSION,
    openai_api_key=config['OPENAI']['OPENAI_API_KEY'],
    base_url=f'{OPENAI_BASE_URL}/{EMBEDDINGS_DEPLOYMENT_NAME}',
    http_client=Client(verify=CERTIFICATE_PATH)
)

NEO4J_URI = 'neo4j://atn1b03n13:7687' #nodo donde esta rodando neo4j
NEO4J_USERNAME = 'neo4j'
NEO4J_PASSWORD = 'Diripar8$'

# Crear el driver de conexión
driver = None
try:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
    driver.verify_connectivity()
    print(f"✅ Successfully connection to Neo4j Graph")
except Exception as e:
    print("❌ Failed to create driver:", str(e))

# Conectar al grafo de Neo4j
graph = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD)


CYPHER_GENERATION_TEMPLATE = """Task:Generate Cypher statement to query a graph database.
Instructions:
Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.

Schema:
{schema}
Examples: Here are examples of generated Cypher statements for particular questions:

# Quais formações estão constituídas pelo material chamado siltito?
MATCH (f:lithostratigraphic_unit)-[:constituted_by]->(m:siltstone)
RETURN f.rdfs_label

Note: Do not include any explanations or apologies in your responses.
Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
Do not include any text except the generated Cypher statement.

The question is:
{question}"""

CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], template=CYPHER_GENERATION_TEMPLATE
)
# Se por acaso você não encontrar a informação necessária, responda únicamente com "De acordo com as informações dadas, não há dados disponíveis no grafo para responder à questão".

QA_PROMPT = bu.read_file(qa_generation_template)
qa_prompt = PromptTemplate.from_template(QA_PROMPT)

# Can limit the number of results from the Cypher QA Chain using the top_k parameter. The default is 10.
qa_chain = GraphCypherQAChain.from_llm(
    graph=graph, 
    qa_prompt = qa_prompt, 
    llm=llm_petrobras, 
    verbose=True, 
    cypher_prompt=CYPHER_GENERATION_PROMPT)

dataset_file = "dataset_miniKGraph.json"

# Cargar el archivo JSON existente
with open(dataset_file, "r", encoding="utf-8") as f:
    dataset = json.load(f)

random_questions = random.sample(dataset, 10)
selected_questions = [{"id": q["id"], "question": q["question"]} for q in random_questions]

# Chain es objeto GraphCypherQAChain
def get_response(question):
    question_modificada = question.replace("URI", "_id")
    print(question_modificada)
    chain_result = qa_chain.invoke(question_modificada)
    only_response = chain_result.get("result")
    return only_response


#qa_response = qa_chain.invoke("Quantos poços estao localizados na bacia chamada CAMAMU-ALMADA?")
#qa_chain.invoke("Que UNIDADES LITOESTRATIGRÁFICAS o poço identificado como POCO_CD_POCO_022851 atravessa que são constituídas por MATERIAL do tipo argila?")
#qa_chain.invoke("Que unidades litoestratigráficas o poço identificado como POCO_CD_POCO_006146 atravessa que são constituídas por MATERIAL do tipo arenito?")
#qa_chain.invoke("Em quais CAMPOS estão as unidades litoestratigráficas que apresentam ESTRUTURA GEOLÓGICA Falha?")

response_data = []

for q in selected_questions:
    question = q["question"]
    answer = get_response(question)
    response_data.append({
        "id": q["id"],
        "question": question,
        "answer": answer
    })

# Define el nombre del archivo JSON
json_file = "chain_responses.json"

# Guardar las respuestas en un archivo JSON
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(response_data, f, ensure_ascii=False, indent=4)

print(f"✅ Respostas guardadas no arquivo {json_file}")
