  
import numpy as np


class Grafo:
  def __init__(self, num_v):
    self.num_v = num_v  
  
  
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
      if(type(t) != int):
        gf[t[0]][t[1]] = 1
      else:
        pass
    self.g = gf
    self.arestas = arestas
  
  def set_lista_adj(self, arestas):
    l = []
    for _ in range(self.num_v-1):
      l.append([])
    
    for aresta in arestas:
      if(type(aresta) != int):
        l[aresta[0]-1].append([aresta[1]])
      else:
        l[aresta-1].append([aresta])

    self.list = l  
  
  def subgrafo(self, g1):
    if((len(self.g)-1)*(len(self.g[0])-1) >= (len(g1)-1)*(len(g1[0])-1)):
      for l in range(1, len(g1)):
        for c in range (1, len(g1[0])):
          if(g1[l][c] != self.g[l][c]):
            if(g1[l][c] != 0):
              return False
    else:
      return False
    return True


  def subgrafo_gerador(self, g1):
    if((len(self.g)-1)*(len(self.g[0])-1) == (len(g1)-1)*(len(g1[0])-1)):
      for l in range(1, len(g1)):
        for c in range (1, len(g1[0])):
          if(g1[l][c] != self.g[l][c]):
            if(g1[l][c] != 0):
              return False
    else:
      return False
    return True
  
  
  def induzido(self, v_l):
    H = {}  

    for vL_i in v_l:
      H[vL_i] = set()
      
    for vL_i in v_l:
        adj = self.list[vL_i-1]
        for v in adj:
            if v[0] in v_l: 
                H[vL_i].add(v[0]) 
    return H
    
  def numeroComponentes(self):
         
        visitado = [False for i in range(self.num_v-1)]
         
        count = 0
         
        for v in range(self.num_v-1):
            if (visitado[v] == False):
                self.DFSUtil(v, visitado)
                count += 1
                 
        return count
      
      
  def DFSUtil(self, v, visitado):
 
        visitado[v] = True
 
        for i in self.list[v]:
            if (type(i) != int):
              if (not visitado[i[0]-1]):
                  self.DFSUtil(i[0]-1, visitado)
            else:
                if (not visitado[i-1]):
                  self.DFSUtil(i-1, visitado)

  def conexo(self):
     x = self.numeroComponentes()
     if(x > 0):
       return False
     else:
       return True


arestas = ((1,2),(2,3), (2,4),(2,5), (4,5))
num_v = 5
graph = Grafo(num_v+1)
graph.set_grafo(arestas)
graph.set_lista_adj(arestas)


#ex 02
print("--------ex 02--------")
arestas_g1 = ((1,2),(3),(2,4), (5))
num_v2 = 5
graph_g1 = Grafo(num_v2+1)
graph_g1.set_grafo(arestas_g1)
print("Subgrafo:",graph.subgrafo(graph_g1.g))

#ex 03
print("\n")
print("--------ex 03--------")
print("Subgrafo gerador:",graph.subgrafo_gerador(graph_g1.g))


#ex 04
print("\n")
print("--------ex 04--------")
arestas = [2,5,4]
print("Subgrafo induzido:",graph.induzido(arestas))


#ex 05
print("\n")
print("--------ex 05--------")
arestas3 = ((1,2),(2,3), (2,4),(5),(6))
num_v3 = 6
graph3 = Grafo(num_v3+1)
graph3.set_lista_adj(arestas3)
print("Número de componentes:",graph3.numeroComponentes())

#ex 06
print("\n")
print("--------ex 06--------")
print("O grafo é conexo?",graph3.conexo())

