
import networkx as nx
import Biblioteca
from Biblioteca import Funcoes


#Iniciando o grafo no arquivo
Meu_Grafo = Funcoes()

#adicionando vertices ao grafo "Meu_Grafo"
Meu_Grafo.adiciona_vertice("a", 5)
Meu_Grafo.adiciona_vertice("b", 6)
Meu_Grafo.adiciona_vertice("c", 1)
Meu_Grafo.adiciona_vertice("d",0)
Meu_Grafo.adiciona_vertice("e",3)
Meu_Grafo.adiciona_vertice("f",7)


#Adicionando arestas no grafo "Meu_Grafo"
Meu_Grafo.adiciona_aresta("a","b",1)
Meu_Grafo.adiciona_aresta("a","c",3)
Meu_Grafo.adiciona_aresta("c","b",2)
Meu_Grafo.adiciona_aresta("c","f",4)

#Removendo aresta do grafo "Meu_Grafo"
Meu_Grafo.remove_aresta("a","c")



Meu_Grafo.qtd_vertices()
Meu_Grafo.qtd_arestas()
Meu_Grafo.lista_vertices()
Meu_Grafo.lista_arestas()
Meu_Grafo.mostra_matriz_adj()
Meu_Grafo.mostra_lista_adj()
Meu_Grafo.mostra_peso_vertices()
Meu_Grafo.mostra_peso_arestas()
