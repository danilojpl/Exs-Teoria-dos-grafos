import numpy as np


class Grafo:
  def __init__(self, num_v):
    self.num_v = num_v
    


  def set_lista_adj(self, arestas):
    l = []
    for _ in range(self.num_v-1):
      l.append([])
    
    for aresta in arestas:
       l[aresta[0]-1].append([aresta[1]])

    self.list = l
    
    
    
  def ordenacao_topologicaUtil(self,v,visitado,pilha):
 
        visitado[v] = True
 
        for i in self.list[v]:
            if visitado[i[0]-1] == False:
                self.ordenacao_topologicaUtil(i[0]-1,visitado,pilha)
 
        pilha.insert(0,v+1)
 
  def ordenacao_topologica(self):
        visitado = [False]*self.num_v
        pilha =[]
 
        for i in range(self.num_v-1):
            if visitado[i] == False:
                self.ordenacao_topologicaUtil(i,visitado,pilha)
 
        print (pilha)
    
    
    
arestas = ((1,2),(2,3), (2,4),(2,5), (4,5))
num_v = 6
graph = Grafo(6)
graph.set_lista_adj(arestas)

graph.ordenacao_topologica()
