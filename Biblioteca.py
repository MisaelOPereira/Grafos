import networkx as nx
import numpy as np
import matplotlib as mtp


class Funcoes:

    # Contrutor da classe
    def __init__(self):
        self.Grafo = nx.Graph() # Grafo self.Grafo é instanciado para ser manipulado pelas funções da classe
      

    # Função para adicionar uma nova vertice ao grafo
    def adiciona_vertice(self, i, p): # i = vertice para ser adicionado, p = peso do vertice
        self.Grafo.add_node(i, peso = p)

    # Função para adicionar uma nova aresta
    def adiciona_aresta(self, i,j, p): # i = Vertice de origem, j = vertice a concectar, p = peso da aresta
        self.Grafo.add_edge(i,j, peso = p)

    # Função para remover aresta do grafo
    def remove_aresta(self, i,j): # i = Vertice de origem, j = vertice conectado
        print(f"\n\nFoi removida do Grafo a aresta ('{i}', '{j}')")
        self.Grafo.remove_edge(i,j)
        

    # Função para mostrar a quantidade x de vertices
    def qtd_vertices(self):
        return print("\n\nNumero de vertices: ", self.Grafo.number_of_nodes())

    # Função para mostrar a quantidade x de arestas
    def qtd_arestas(self):
       return print("\n\nNumero de arestas: ", self.Grafo.number_of_edges())


    #Função para mostrar a lista de vertices do grafo
    def lista_vertices(self):
        return print( '\n\nLista de Vertices: \n\n',list(self.Grafo.nodes()))

    #Função para mostrar a lista de arestas do grafo
    def lista_arestas(self):
        return print( '\n\n Lista de Arestas: ', list(self.Grafo.edges()))


    # Função para mostrar a matriz de adjacenciado grafo    
    def mostra_matriz_adj(self):
        A = nx.to_numpy_matrix(self.Grafo)
        return print("\n\nMatriz de adjacencia: ",A,"\n\n")

    # Função para mostrar a lista de adjacencia do grafo
    def mostra_lista_adj(self):
        print("Lista de adjacencia: \n")
        for line in nx.generate_adjlist(self.Grafo):
            print(line)

        

    # Função para mostra o peso dos vertices e arestas
    def mostra_peso_vertices(self):
        print("\n\nPeso dos vertices: ", self.Grafo.nodes.data())
        
    # Função para mostra o peso das arestas
    def mostra_peso_arestas(self):
        print("\n\nPeso das arestas: ", self.Grafo.edges.data() )
    