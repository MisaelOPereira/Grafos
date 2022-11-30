grafo = [ [1],           
          [2, 3],        
          [1, 4],        
          [0],           
          [1]            
        ]

def dfs(g1):
    def dfs_recursiva(grafo, vertice):
        visitados.add(vertice)
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                dfs_recursiva(grafo, vizinho)

    visitados = set()
    for vertice in g1:
        if not vertice in visitados:
            dfs_recursiva(g1, vertice)

            
  
# para chamar essa função: dfs(grafo)
        