# Langchain with Free Graph Database do Neo4j

## 💻  Langchain with Free Graph Database do Neo4j
✅ Neo4jGraph
✅ GraphCypherQAChain

O Jupyter notebook `Neo4jGraph_Langchain.ipynb` configura uma cadeia de processamento de perguntas e respostas que utiliza um modelo de linguagem da OpenAI como base (ChatOpenAI) e se conecta a um banco de dados Neo4j (Neo4jGraph). Especificamente, cria a cadeia de processamento de perguntas e respostas, especificando o modelo de linguagem, a conexão com o Neo4j e habilitando mensagens de depuração. Finalmente, executa a cadeia de processamento com uma pergunta específica para receber uma resposta. Esse processo combina inteligência artificial com uma base de conhecimento em grafo para responder a perguntas específicas de forma contextualizada.


###  👩‍💻 Results: Implement Langchain over Neo4j Sandbox: Dataset Movies

![image](https://github.com/lauraparra28/Graphs/assets/10816198/80e1e7ff-22ba-418c-bcba-aef5e74e15cf)

![image](https://miro.medium.com/v2/resize:fit:1400/1*aIPT_zo4zQnsQbRP3s8Tpg.png)


## 🕵️‍♀️ Text2Cypher on NebulaGraph
Within LlamaIndex’s `KnowledgeQueryEngine `and LangChain’s `NebulaGraphQAChain`, we don’t need to concern ourselves with NebulaGraph’s Schema retrieval, Cypher statement generation prompts, various LLM calls, result processing, or linkage. [[Ref]](https://siwei.io/en/llm-text-to-nebulagraph-query/)

### 1. Using LlamaIndex [[Reference documentation]](https://gpt-index.readthedocs.io/en/latest/examples/query_engine/knowledge_graph_query_engine.html)

With LlamaIndex, all we need to do is:

- Create a `NebulaGraphStore `instance.
- Create a `KnowledgeQueryEngine`.

### 2. Using LangChain [[Reference documentation]](https://python.langchain.com/docs/modules/chains/additional/graph_nebula_qa)
Similarly, in Langchain, we just need to:

- Create a `NebulaGraph `instance.
- Create a `NebulaGraphQAChain `instance.

## 🕵️‍♀️ KGraph RAG Llama Index 
### 💻 Knowledge Graph Demo [[Link]](https://docs.llamaindex.ai/en/stable/examples/index_structs/knowledge_graph/KnowledgeGraphDemo.html)


### 📃 Why Knowledge Graph RAG Query Engine?

In Llama Index, there are two scenarios we could apply Graph RAG:

- Build Knowledge Graph from documents with Llama Index, with LLM or even [local models](https://colab.research.google.com/drive/1G6pcR0pXvSkdMQlAK_P-IrYgo-_staxd?usp=sharing), to do this, we should go for `KnowledgeGraphIndex`.
- Leveraging existing Knowledge Graph, in this case, we should use `KnowledgeGraphRAGQueryEngine`.

###  💻 CODE - CODE - Convert .json to RDF format [[Link Colab]](https://colab.research.google.com/drive/1k_UPxolACruYuhDTubPT0iD2vcn6mUNl?usp=sharing) 
⚠️Important: Verificar se a chave 'elementId' está presente no item
⚠️Chave 'identity' não encontrada para o item

### Concepts: 
- [x]  Cypher
- [x]  Text2Cyper [[Link]](https://siwei.io/en/llm-text-to-nebulagraph-query/)
- [ ]  Biblioteca `Llama Index`
