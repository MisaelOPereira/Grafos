import networkx as nx
import numpy as np
import matplotlib as mtp


class Funcoes:

    def __init__(self):
        self.Grafo = nx.Graph()
        
    def instacia(self, Grafo):
        self.Grafo = Grafo

    def tamanho_grafo(self):
        return print("Numero de vertices:", self.Grafo.number_of_nodes(),"  Numero de arestas:", self.Grafo.number_of_edges())
        

    def adiciona_vertice(self, v):
        self.Grafo.add_node(v)

    def adiciona_aresta(self, u,v):
        self.Grafo.add_edge(u,v)
        

    def mostra_grafo(self):
        return print( 'Vertices: ',list(self.Grafo.nodes()) ,'Arestas: ', list(self.Grafo.edges()))
        
    def mostra_matriz(self):
        A = nx.to_numpy_matrix(self.Grafo)
        return A

    def mostra_lista(self):
        #i = self.Grafo.number_of_nodes()
        #self.Grafo = nx.lollipop_graph(int(self.Grafo.number_of_nodes()),int(self.Grafo.number_of_edges())) 
        #for line in nx.generate_adjlist(self.Grafo):
            #print (line)
        for line in nx.generate_adjlist(self.Grafo):
            print(line)
        