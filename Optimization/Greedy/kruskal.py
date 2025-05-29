import heapq
import Disjoint

class Graph:
    def __init__(self):        
        # Dictionary of Dictionaries (Adj List)
        # __adjList[source] = {{destination,weight}}
        self.__adjList = {}
    
    def addVertex(self, vertex):
        if vertex not in self.__adjList:
            self.__adjList[vertex] = {}
    
    def addEdge(self,source,destination,weight = 1, isUndirected = True):
        self.addVertex(source)
        self.addVertex(destination)
        self.__adjList[source][destination] = weight

        if(isUndirected):
            self.__adjList[destination][source] = weight

    def __str__(self):
        result = []
        for vertex,neighbors in self.__adjList.items():
            result.append(f"{vertex}:{neighbors}")
        return "\n".join(result)
    
    def getLength(self): return len(self.__adjList)

    def kruskal(self):
        G = Graph()
        ds = Disjoint.DisjointSet()
        minCost,edgeCount = 0,0
        n = len(self.__adjList)
        edgeList = []
        seenEdges = set()

        # Turn Graph into an edgelist sorted into a heap
        for source, neighbors in self.__adjList.items():
            for destination, weight in neighbors.items():
                if((source,destination) not in seenEdges):
                    edgeList.append((weight,source,destination))
                    seenEdges.add((destination,source))
        heapq.heapify(edgeList)

        ds.makeSet(self.__adjList.keys())
        
        while(edgeList and edgeCount < n-1):
            min = edgeList[0][0]
            tmp = heapq.heappop(edgeList)
            u = tmp[1] # source
            v = tmp[2] # destination

            if(ds.find(u) != ds.find(v)):
                minCost += tmp[0]
                edgeCount += 1
                ds.union(u,v)
                G.addEdge(u,v,tmp[0])
        return [G,minCost]

    
    # Example usage
G = Graph()
G.addEdge(1, 2, 28)
G.addEdge(1, 6, 10)
G.addEdge(2, 3, 16)
G.addEdge(2, 7, 14)
G.addEdge(3, 4, 12)
G.addEdge(4, 5, 22)
G.addEdge(4, 7, 18)
G.addEdge(5, 7, 24)
G.addEdge(5, 6, 25)

print("G:")
print(G)
H,cost = G.kruskal()
print("\nH:")
print(H)
print(f"\nCost: {cost}")