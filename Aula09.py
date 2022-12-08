import copy
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
    print("Vertice inicial\t vertice final \t Menor caminho")
    def printSolution(self, path,src):
        for i in range(len(path)):
            if(type(path[i]) != int):
                path[i].append(i)
                print(src, "\t\t\t",i,"\t\t", path[i])
 
    def minDistance(self, dist, sptSet):
 
        min = 1e7
 
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
    
    def dijkstra(self, src):
 
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        path = [-1]*self.V
 
        for cout in range(self.V):
 
            u = self.minDistance(dist, sptSet)
 
            sptSet[u] = True
 
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
                    if(path[v] == -1):
                        if(path[u]==-1):
                            path[v]=([u])
                        else:
                            c = copy.copy(path[u])
                            path[v] = c
                            path[v].append(u)
                    else:
                        path[v].append(u)
    
        
                        
    
        self.printSolution(path,src)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
 
src = 1
g.dijkstra(src)