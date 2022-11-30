from collections import defaultdict


class Graph:
    
   #Busca em profundidade 
    def dfs(Graph):
        def dfs_recursiva(grafo, vertice):
            visitados.add(vertice)
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                 dfs_recursiva(grafo, vizinho)

        visitados = set()
        for vertice in g1:
           if not vertice in visitados:
            dfs_recursiva(g1, vertice)

   #Algoritmo de Fleury
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = defaultdict(list) # default dictionary para armazenar o grafo
        self.Time = 0

   #Adiciona aresta (não direcionada)
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u)   
        
   #Função para remover a aresta u-v do grafo       
    def rmvEdge(self, u, v): 
        for index, key in enumerate(self.graph[u]): 
            if key == v: 
                self.graph[u].pop(index) 
        for index, key in enumerate(self.graph[v]): 
            if key == u: 
                self.graph[v].pop(index)     


   #Importante - auxiliar para verificar pontes 
    def DFSCount(self, v, visited): 
        count = 1
        visited[v] = True
        for i in self.graph[v]: 
            if visited[i] == False: 
                count = count + self.DFSCount(i, visited)        
        return count    

   #Função que verifica se a aresta u-v pode ser considerada uma aresta no Tour de Euler
    def isValidNextEdge(self, u, v):  
        if len(self.graph[u]) == 1:
            return True
        else:
            visited =[False]*(self.V) 
            count1 = self.DFSCount(u, visited)   
            self.rmvEdge(u, v) 
            visited =[False]*(self.V) 
            count2 = self.DFSCount(u, visited)        
            self.addEdge(u,v) 
            return False if count1 > count2 else True   

   #Printa o tour de Euler tour começando pelo vértice u 
    def printEulerUtil(self, u):
        for v in self.graph[u]:   
             if self.isValidNextEdge(u, v): 
                print("%d-%d " %(u,v)), 
                self.rmvEdge(u, v) 
                self.printEulerUtil(v)        

    def printEulerTour(self):
        u = 0
        for i in range(self.V): 
            if len(self.graph[i]) %2 != 0 : 
                u = i 
                break 
            print ("\n") 
            self.printEulerUtil(u)  


g1 = Graph(5) 
g1.addEdge(0, 1) 
g1.addEdge(0, 2) 
g1.addEdge(1, 2) 
g1.addEdge(2, 3) 
g1.addEdge(2, 3) 
g1.printEulerTour()              
