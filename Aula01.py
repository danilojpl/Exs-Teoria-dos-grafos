import numpy as np


class Grafo:
  def __init__(self, num_v):
    self.num_v = num_v


  #exs Aula 01 ex01
  def set_grafo(self,arestas):
    nx = 1
    ny = 1
    gf = np.zeros((self.num_v,self.num_v), dtype=np.int64)
    for x in range(self.num_v):
      for y in range(self.num_v):
        if(x == 0 and y > 0):
          gf[x][y] = nx
          nx+=1
        elif(y == 0 and x > 0):
          gf[x][y] = ny
          ny+=1
        
    for t in arestas:
      gf[t[0]][t[1]] = 1
    self.g = gf

  def set_lista_adj(self, arestas):
    l = []
    for _ in range(self.num_v-1):
      l.append([])
    
    for aresta in arestas:
       l[aresta[0]-1].append([aresta[1]])

    self.list = l

  def printMatriz(self, g, num_v):
        for x in range(num_v):
            for y in range(num_v):
                print(g[x][y], end="")
            print("")       

  #exs Aula 01 ex03
  def grau_entrada(self,g,v):
    grau = 0
    for i in range(1,self.num_v):
      if(g[i][v] == 1):
        grau+=1
    return grau

  def grau_saida(self,g,v):
    grau = 0
    for i in range(1,self.num_v):
      if(g[v][i] == 1):
        grau+=1
    return grau

  #exs Aula 01 ex04
  def grafos_iguais(self,g1, g2):
    return np.array_equiv(g1, g2)
    
  #exs Aula 01 ex05
  def convert_grafo(self, g, tipo):
    i = 1
    arestas = []
    if(tipo == 'L'):
      for vs in g:
        for v in vs:
          arestas.append([i,v[0]])
        i+=1
      self.set_grafo(arestas)

    if(tipo ==  'M'):
      for l in range(1,len(g)):
        for c in range(1,len(g[0])):
          if(g[l][c] == 1):
            arestas.append([l,c])
      self.set_lista_adj(arestas)
    
  #exs Aula 01 ex06  
  def invert_list(self,list):
    n = 0
    for i in list:
        list[n] = i[::-1]
        n+=1
    self.list = list
    
  #exs Aula 01 ex08
  def fonte(self, g, v):
      grau_entrada = self.grau_entrada(g,v)
      grau_saida = self.grau_saida(g,v)
      if(grau_saida > 0 and grau_entrada == 0):
          return 1
      else:
          return 0 

  #exs Aula 01 ex09
  def sorvedouro(self, g, v):
      grau_entrada = self.grau_entrada(g,v)
      grau_saida = self.grau_saida(g,v)
      if(grau_saida == 0 and grau_entrada > 0):
          return 1
      else:
          return 0 

  #exs Aula 01 ex10 matriz adjacencia
  def simetrico(self, g, num_v):
      ehsimetrico = True
      for i in range(1,num_v):
            for j in range(1,num_v):
                if(g[i][j] == 1):
                    if(g[j][i] != 1):
                      ehsimetrico = False
                      break
            if(ehsimetrico == False):
                break
      return ehsimetrico
                        
          

arestas = ((1,2), (1,3),(2,3), (2,4),(2,5),(3,4), (4,5))
num_v = 6
graph = Grafo(num_v)
graph.set_grafo(arestas)

#ex 01
print("--------ex 01--------")
graph.printMatriz(graph.g,num_v)
  
print('\n')
#ex 03
print("--------ex 03--------")
print("Grau de entrada: ",graph.grau_entrada(graph.g,5))
print("Grau de saída: ",graph.grau_saida(graph.g,5))

print('\n')
#ex 04
print("--------ex 04--------")
arestas2 = ((1,2), (1,3),(2,3), (2,4),(2,5),(3,4), (4,5), (5,1))
num_v2 = 6
graph2 = Grafo(num_v2)
graph2.set_grafo(arestas2)

print("São iguais? ",graph.grafos_iguais(graph.g, graph2.g))

print('\n')
#ex 05
print("--------ex 05--------")
graph.convert_grafo(graph.g, 'M')
print("Matriz convertida: ", graph.list)

graph2.set_lista_adj(arestas2)
graph2.convert_grafo(graph2.list, 'L')
print("Lista convertida: ")
graph2.printMatriz(graph2.g,num_v2)

print('\n')
#ex 06
print("--------ex 06--------")
print("Lista antes da inversão: ")
print(graph.list)
print("Lista depois da inversão: ")
graph.invert_list(graph.list)
print(graph.list)

print('\n')
#ex 08
print("--------ex 08--------")
print("O vértice é uma fonte: ", graph.fonte(graph.g, 1))

print('\n')
#ex 09
print("--------ex 09--------")
print("O vértice é um sorvedouro: ", graph.sorvedouro(graph.g, 5))


print('\n')
#ex 10
print("--------ex 10--------")
print("O grafo é simetrico? ", graph.simetrico(graph.g, num_v))
arestas3 = ((1,2), (2,1),(1,3),(3,1),(2,3),(3,2),(2,4),(4,2),(2,5),(5,2),(3,4),(4,3),(4,5),(5,4))
num_v3 = 6
graph3 = Grafo(num_v3)
graph3.set_grafo(arestas3)

print("O grafo é simetrico? ", graph3.simetrico(graph3.g, num_v3))














