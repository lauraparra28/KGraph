# Dataset baseado no novo grafo MiniOntologia.rdf ou MiniKGraph 

A função gerar_perguntas recebe um grafo de conhecimento G como entrada e retorna uma lista de dicionários, cada um contendo uma pergunta, contexto e resposta. A função itera sobre cada aresta no grafo e verifica se o predicado da aresta corresponde a uma URI específica. Se corresponder, a função gera uma pergunta natural a partir do sujeito, predicado e objeto da aresta, e adiciona a pergunta, contexto e resposta a uma lista.

- A função assume que o grafo de conhecimento G contém as informações necessárias para gerar as perguntas e respostas.

- Foi feito o teste, especificamente para o predicado "http://www.semanticweb.org/bg40/ontologies/2022/5/untitled-ontology-2#POCO_CD_POCO_012120" e o objeto "{'label': 'http://www.semanticweb.org/bg40/ontologies/2022/5/untitled-ontology-2#located_in'}", tendo como resultados dados_treinamento-especific.json.

- Despois, foi feita uma função mais genérica, permitindo a geração de perguntas e respostas para diferentes tipos de predicados e objetos.

## 💻 Função gerar_perguntas

Usa a biblioteca rdflib para manipulação de dados em RDF (Resource Description Framework) de uma uma ontologia para extrair informações sobre campos, poços e formações geológicas, e gera um conjunto de perguntas e respostas em português, que são então salvas em um arquivo JSON.

Para cada campo em fields, se houver uma informação de localização (located_in), é criada uma pergunta sobre a localização do campo. Para cada poço em wells, se houver uma informação de cruzamento (crosses), é criada uma pergunta sobre onde o poço atravessa. Em cada loop sobre as formações (formations), são verificadas diferentes propriedades (constituted_by, part_of, has_age) e, se presentes, são criadas perguntas sobre a constituição, a entidade de que faz parte e a idade da formação. A resposta e o contexto da pergunta são baseados nos dados extraídos da ontologia. Finalmente, todas as perguntas geradas são salvas em um arquivo JSON com codificação UTF-8.

Além das relações e entidades do grafo, as perguntas geradas estão baseadas na seguinte lista de perguntas:

### **🔍 Novas Querys with MiniKGraph.rdf** 
Data: 26/07/2024

**Perguntas single-hop sem necessidade de agregação de informações (um para um)**
1.   Em que BACIA está localizado o CAMPO `NOME DO CAMPO` ?
2.   Em que BACIA está localizado o POÇO `NOME DO POÇO`?
3.   Qual a idade geológica da Formação `unidade litoestratigráfica`?

**Perguntas single-hop com necessidade de agregação de informações (um para vários)**

4.   Quais são os CAMPOS localizados na BACIA `NOME DA BACIA` ?
5.   Quais os POÇOS localizados no CAMPO `nome do campo`?
6.   Quantos CAMPOS estão localizados na BACIA `NOME DA BACIA`?
7.   Quantos POCOS estão localizados na BACIA `NOME DA BACIA`?
8.   Que UNIDADES LITOESTRATIGRÁFICAS o POÇO `nome do poço` atravessa?
9.   Que UNIDADES LITOESTRATIGRÁFICAS são constituídas por FLUIDO `tipo de fluido`?
10.   Que ESTRUTURA GEOLÓGICAS são apresentadas pela Formação `unidade litoestratigráfica`?

**Perguntas multi-hop**

11. Que UNIDADES LITOESTRATIGRÁFICAS o poco 9-FZ-2-AM / POCO_CD_POCO_023241 atravessa que são constituídas por ROCHAS do tipo dolomito / dolomite?
12.   Que UNIDADES LITOESTRATIGRÁFICAS o poco 9-FZ-2-AM / POCO_CD_POCO_023241 atravessa que são constituídas por FLUIDO do tipo gás seco / dry_gas?
13.   Que IDADE GEOLÓGICA das UNIDADES LITOESTRATIGRÁFICAS constituídas por FLUIDO `tipo de fluido`?
14.   Quantos POCOS atravessam UNIDADES LITOESTRATIGRÁFICAS constituídas por FLUIDO `tipo de fluido`?
15.   Em quais BACIAS estão as UNIDADES LITOESTRATIGRÁFICAS constituídas por FLUIDO `tipo de fluido`?
16.   Em quais CAMPOS estão as UNIDADES LITOESTRATIGRÁFICAS constituídas por FLUIDO `tipo de fluido`?
17.   Em quais CAMPOS estão as UNIDADES LITOESTRATIGRÁFICAS apresentam ESTRUTURA GEOLÓGICA do tipo falha / TEFR_CD_TIPO_EST_FISICA_ROCHA_058?
18.   Quais ESTRUTURAS GEOLÓGICAS ocorrem nas UNIDADES LITOESTRATIGRÁFICAS constituídas por FLUIDO do tipo gás seco / dry_gas?
19.   Quantos poços da BACIA `NOME DA BACIA` atravessam UNIDADES LITOESTRATIGRÁFICAS que são constituídas por ROCHAS do tipo dolomito / dolomite?
