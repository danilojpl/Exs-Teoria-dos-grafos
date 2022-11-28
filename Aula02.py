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
      gf[t[0]][t[1]] = 1
    self.g = gf


  def printMatriz(self, g, num_v):
        for x in range(num_v):
            for y in range(num_v):
                print(g[x][y], end="")
            print("")  
    
    #exs Aula 02
  def verificar_caminho(self, caminho):
    vertice = None 
    for v in caminho:
      if(vertice == None):
        vertice = v 
      else:
        if(self.g[vertice][v] != 1):
          if(self.g[v][vertice] != 1):
            return 0
        vertice = v
    return 1

  def verificar_caminho_simples_grafo(self, caminho):
    if(self.verificar_caminho(caminho)):
      vertices_visitados = [0] * self.num_v
      vertice = None 
      for v in caminho:
        if(vertice == None):
          vertice = v 
          vertices_visitados[vertice] = 1 
        else:
          if(vertices_visitados[v] == 1):
            return 0
          else:
            vertices_visitados[v] = 1
      return 1
    else:
      return 0

  def set_lista_adj(self, arestas):
    l = []
    for _ in range(self.num_v-1):
      l.append([])
    
    for aresta in arestas:
       l[aresta[0]-1].append([aresta[1]])

    self.list = l

  def caminho_entreVertices(self, s, t):
        s = s-1
        t = t-1
        visitado =[False]*(self.num_v)
  
        fila=[]
  
        fila.append(s)
        visitado[s] = True
  
        while fila:

            n = fila.pop(0)
             
            if n == t:
                   return True
 
            for i in self.list[n]:
                if visitado[i[0]-1] == False:
                    fila.append(i[0]-1)
                    visitado[i[0]-1] = True

        return False
      
  def print_caminho_entreVertices(self, s, t):
        s = s-1
        t = t-1
        visitado =[False]*(self.num_v)
        caminho = []
        fila=[]
  
        fila.append(s)
        visitado[s] = True
  
        while fila:

            n = fila.pop(0)
            caminho.append(n+1) 
            if n == t:
              return caminho
 
            for i in self.list[n]:
                if visitado[i[0]-1] == False:
                    fila.append(i[0]-1)
                    visitado[i[0]-1] = True

        return False

arestas = ((1,2),(2,3), (2,4),(2,5), (4,5))
num_v = 6
graph = Grafo(6)
graph.set_grafo(arestas)

caminho = [1,3,4,2,3,4,5]

#ex 01
print("--------ex 01--------")
print("O caminho existe? ",graph.verificar_caminho(caminho))

print('\n')
#ex 02
print("--------ex 02--------")
print("O caminho simples existe? ",graph.verificar_caminho_simples_grafo(caminho))

print('\n')
#ex 03
print("--------ex 03--------")
graph.set_lista_adj(arestas)
print("O caminho de um vertice ao outro existe? ",graph.caminho_entreVertices(1,5))

#ex 04
print("--------ex 04--------")
print("caminho: ",graph.print_caminho_entreVertices(1,5))


#ex 04
print("--------ex 06 Arco--------")
