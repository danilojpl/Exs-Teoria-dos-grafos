from collections import defaultdict
  
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list) 
        self.Time = 0
  
    def addAresta(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    def rmvAresta(self, u, v):
        for idx, chave in enumerate(self.graph[u]):
            if chave == v:
                self.graph[u].pop(idx)
        for idx, chave in enumerate(self.graph[v]):
            if chave == u:
                self.graph[v].pop(idx)
 
    def DFSCount(self, v, visitado):
        count = 1
        visitado[v] = True
        for i in self.graph[v]:
            if visitado[i] == False:
                count = count + self.DFSCount(i, visitado)        
        return count
 
    def proximaAresta(self, u, v):
  
        if len(self.graph[u]) == 1:
            return True
        else:
 
            visitado =[False]*(self.V)
            count1 = self.DFSCount(u, visitado)

            self.rmvAresta(u, v)
            visitado =[False]*(self.V)
            count2 = self.DFSCount(u, visitado)
 
            self.addAresta(u,v)
            
            return False if count1 > count2 else True
 
 
    def printEulerUtil(self, u):
        for v in self.graph[u]:
            if self.proximaAresta(u, v):
                print("%d-%d " %(u,v)),
                self.rmvAresta(u, v)
                self.printEulerUtil(v)
 
 
    def printEulerTrilha(self):
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) %2 != 0 :
                u = i
                break
        print ("\n")
        self.printEulerUtil(u)
        
    def printCircuit(self):
 
        edge_count = dict()
    
        for i in range(len(self.graph)):

            edge_count[i] = len(self.graph[i])
    
        if len(self.graph) == 0:
            return 
    
        curr_path = []
    
        circuit = []
    
        curr_path.append(0)
        curr_v = 0 
    
        while len(curr_path):
    
            if edge_count[curr_v]:
    
                curr_path.append(curr_v)

                next_v = self.graph[curr_v][-1]
    
                edge_count[curr_v] -= 1
                self.graph[curr_v].pop()
    
                curr_v = next_v

            else:
                circuit.append(curr_v)
    
                curr_v = curr_path[-1]
                curr_path.pop()
    
        for i in range(len(circuit) - 1, -1, -1):
            print(circuit[i], end = "")
            if i:
                print(" -> ", end = "")
              

        
 
print("--------ex - trilha euleriana algoritmo de Fleury--------")
g1 = Graph(4)
g1.addAresta(0, 1)
g1.addAresta(0, 2)
g1.addAresta(1, 2)
g1.addAresta(2, 3)
g1.printEulerTrilha()


print("--------ex - trilha euleriana algoritmo de Hierholzer--------")
g2 = Graph(6)
g2.addAresta(0, 1)
g2.addAresta(1, 2)
g2.addAresta(2, 3)
g2.addAresta(3, 0)
g2.addAresta(2, 5)
g2.addAresta(2, 4)
g2.addAresta(4, 1)
g2.addAresta(5, 1)
g2.printCircuit()




