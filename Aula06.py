import numpy as np

class Graph():
 
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)] \
                                for row in range(V)]
        
    def set_grafo(self,arestas):
        gf = np.zeros((self.V,self.V), dtype=np.int64)
            
        for t in arestas:
            gf[t[0]][t[1]] = 1
        self.graph = gf        
        
        

    def bipartite(self, src):
 
        colorArr = [-1] * self.V
 
        colorArr[src] = 1
 
        queue = []
        queue.append(src)

        while queue:
 
            u = queue.pop()
 
            if self.graph[u][u] == 1:
                return False
 
            for v in range(self.V):
 
                if self.graph[u][v] == 1 and colorArr[v] == -1:
                    
                    colorArr[v] = 1 - colorArr[u]
                    queue.append(v)

                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                    return False
 
        return True, colorArr
    
    def colorBipartite(self, src):
        bipartido,colorArray=self.bipartite(src)
        if(bipartido):
            for i in range(len(colorArray)):
                if(colorArray[i] == 0):
                    print("Vértice: ",i, "Cor: Azul")
                else:
                    print("Vértice: ",i, "Cor: Vermelho")
        else:
            print("O Grafo não é bipartido!")

    def isBipartite(self, src):
        bipartido=self.bipartite(src)
        if(bipartido):
            return True
        else:
            return False
                
        
 
#ex 01
print("\n")
print("--------ex 01--------")
g = Graph(4)
g.graph = [[0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]]
g.colorBipartite(0)

#ex 02
print("\n")
print("--------ex 02 O grafo é bipartido?--------")
g1 = Graph(6)
g1.graph = [[0, 1, 1, 1, 0, 0],
            [1, 0, 0, 1, 1, 0],
            [1, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1],
            [0, 1, 0, 1, 0, 1],
            [0, 0, 1, 1, 1, 0]]
             
print ("Sim" if g1.isBipartite(0) else "Não")


#ex leetcode - 886 - adaptado
print("\n")
print("--------ex - é possível dividir todos em dois grupos?--------")
#entrada 01 
n = 4
dislikes = [(0,1),(0,2),(1,3)]
g2 = Graph(n)
g2.set_grafo(dislikes)
print("ENTRADA 01")
print ("True" if g2.isBipartite(0) else "False")
#entrada 02
n = 4
dislikes = [(0,1),(0,2),(1,2)]
g3 = Graph(n)
g3.set_grafo(dislikes)
print("ENTRADA 02")
print ("True" if g3.isBipartite(0) else "False")
#entrada 03
n = 5
dislikes = [(0,1),(1,2),(2,3),(3,4),(4,0)]
g4 = Graph(n)
g4.set_grafo(dislikes)
print("ENTRADA 03")
print ("True" if g4.isBipartite(0) else "False")