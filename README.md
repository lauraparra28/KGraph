# KGraph: Graphs in OWL Knowledge 

Este repositório contém dois scripts Python que exploram e comparam ontologias OWL usando a biblioteca owlready2. Esses scripts são úteis para realizar diversas operações em grafos de conhecimento, como verificação de consistência, inferência de instâncias, extração de informações e comparação de ontologias.

## 1. Exploração de Grafos em Ontologias

O notebook `exploracao_grafos.ipynb` fornece uma interface interativa para explorar grafos em ontologias OWL. Abra o notebook em um ambiente Jupyter para seguir passo a passo as operações disponíveis. Ele utiliza a biblioteca owlready2 para realizar diversas operações em ontologias OWL. Alguns dos principais recursos incluem:
- Verificação de consistência da ontologia.
- Inferência de instâncias e propriedades.
- Extração de informações específicas da ontologia.
- Consultas SPARQL para recuperar dados específicos.
- Manipulação e visualização de grafos com NetworkX e matplotlib.


## 2. Visualização das Ontologias no Notebook
Para explorar um grafo no formato OWL mais detalhadamente, pode ser util utilizar visualizações gráficas interativas para uma exploração mais dinâmica. O uso da biblioteca networkx em conjunto com o matplotlib para visualização é uma boa opção para grafos com poucas entidades e subclasses. O notebook `exploracao_grafos.ipynb` fornece visualizações interativas dos grafos de ontologias OWL. Os gráficos são gerados usando a biblioteca NetworkX e podem ser personalizados para exibir diferentes aspectos da ontologia. Aqui estão algumas dicas sobre como interpretar as visualizações:

- Nós: Representam classes, instâncias ou conceitos na ontologia.
- Arestas: Representam relações ou propriedades entre classes ou instâncias.
- Cores e Tamanhos: Podem ser usados para indicar diferentes propriedades ou características das classes ou instâncias.

### Protégé 
É uma ferramenta para a criação e edição de ontologias, e possui integração com o [Graphviz](https://graphviz.org/download/), como uma ferramenta externa, _**para a visualização ou gerar representações gráficas de ontologias.**_ Basicamente é uma ferramenta para visualização de grafos e pode ser utilizada para representar ontologias de maneira gráfica. 

Ontologia foi definida na linguagem de modelagem ontológica OWL (Web Ontology Language) e foram definidos os conceitos, propriedades e relações no NER_geologica (https://codigo-externo.petrobras.com.br.mcas.ms/buscasemantica/ontologias_entidades_relacoes/ner_geologica)

### WebVOWL
Consegui visualizar o grafo usando o [WebVOWL (Visual Notation for OWL Ontologies)](https://service.tib.eu/webvowl/) é uma ferramenta web que permite a visualização gráfica de ontologias OWL (Web Ontology Language). Ele fornece uma representação visual intuitiva de classes, propriedades e suas relações em uma ontologia. O objetivo principal do WebVOWL é melhorar a compreensão e a interpretação de ontologias complexas.

## 2. Comparação entre Ontologias
O notebook `compare_class_ontologies.ipynb` realiza a comparação entre duas ontologias, analisando as classes em comum. Esse script é útil para identificar semelhanças e diferenças entre ontologias diferentes.

## 3. Pré-requisitos
Certifique-se de ter a biblioteca owlready2 instalada antes de executar o script. Você pode instalá-la usando o seguinte comando:
```bash
pip install owlready2
pip install networkx
pip install matplotlib
```
## 4. Contribuições 
Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar problemas, sinta-se à vontade para abrir uma issue ou enviar um pull request.
