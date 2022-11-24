
import networkx as nx
import Biblioteca
from Biblioteca import Funcoes



Minha_funcao = Funcoes()


Minha_funcao.adiciona_vertice(2)
Minha_funcao.adiciona_vertice(4)
Minha_funcao.adiciona_vertice(6)
Minha_funcao.adiciona_vertice(3)

Minha_funcao.adiciona_aresta(2,4)


print(Minha_funcao.mostra_grafo())
print(Minha_funcao.tamanho_grafo())
