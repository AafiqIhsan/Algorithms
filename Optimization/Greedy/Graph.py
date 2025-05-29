import networkx as nx
import matplotlib.pyplot as plt
import heapq
import DisjointSet

class Graph:
    def __init__(self):
        self.__edgeList = {}
    
    def addVertex(self,vertex):
        if vertex not in self.__edgeList:
            self.__edgeList[vertex] = {}

    def addEdge(self,source,destination,weight = 1, isUndirected = True):
        if source not in self.__edgeList:
            self.addVertex(source)
        if destination not in self.__edgeList:
            self.addVertex(destination)
        self.__edgeList[source][destination] = weight
        if isUndirected:
            self.__edgeList[destination][source] = weight
    
    def __str__(self):
        result = []
        for source, neighbors in self.__edgeList.items():
            for destination, weight in neighbors.items():
                result.append(f"{source}--{weight}-->{destination}")
        return "\n".join(result)

    def plot(self, title = "Graph"):
        G = nx.Graph()
        for source in self.__edgeList:
            for destination,weight in self.__edgeList[source].items():
                if not G.has_edge(source,destination):
                    G.add_edge(source,destination,weight = weight)
        pos = nx.spring_layout(G)
        edgeLabels = nx.get_edge_attributes(G, 'weight')
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1000, font_size=12)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edgeLabels)
        plt.title(title)
        plt.axis('off')
        plt.show()

    def kruskal(self):
        MST = Graph()
        ds = DisjointSet.DisjointSet()
        ds.makeSet(self.__edgeList.keys())
        minCost, edgeCount = 0,0
        n = len(self.__edgeList)
        edgeHeap = []
        seenEdges = set()

        for source in self.__edgeList:
            for destination,weight in self.__edgeList[source].items():
                if (source,destination) not in seenEdges:
                    edgeHeap.append((weight,source,destination))
                    seenEdges.add((destination,source)) 
                    # We add as destination,source because for undirected graph,
                    # we will check for the reverse as the duplicate
        heapq.heapify(edgeHeap)

        while(edgeCount < n-1 and edgeHeap):
            min = heapq.heappop(edgeHeap)
            weight = min[0]
            source = min[1]
            destination = min[2]
            
            if(ds.find(source) != ds.find(destination)):
                MST.addEdge(source,destination,weight)
                edgeCount += 1
                ds.union(source,destination)
                minCost += weight
        return MST, minCost


G = Graph()
G.addEdge("Dhaka", "Sylhet",346)
G.addEdge("Dhaka", "Rajshahi",219)
G.addEdge("Dhaka", "Chittagong",264)
G.addEdge("Dhaka", "Barisal",112)
G.addEdge("Rajshahi", "Chittagong",346)
G.addEdge("Rajshahi", "Khulna",200)
G.addEdge("Rajshahi", "Rangpur",166)
G.addEdge("Dhaka", "Khulna",404)

G.plot("Graph")
MST, minCost = G.kruskal()
MST.plot("Minimum Spanning Tree")