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
        MST = Graph() # Graph to store Minimum Spanning Tree MST = (|V'|, |E'|)
        # |V'| = |V|, |E'| = |V| - 1

        # Disjoint set to keep track of nodes forming cycles
        ds = DisjointSet.DisjointSet()
        ds.makeSet(self.__edgeList.keys())

        minCost = 0 # Total cost of the Minimum Spanning tree
        edgeCount = 0 # Number of edges of the MST |E'| = |V| - 1
        n = len(self.__edgeList) # Total Number of Vertices in the graph |V|

        edgeHeap = [] # Heap to store a min heap of tuples (weight,source,destination)
        seenEdges = set() # set of visited edges

        # Iterating the Graph, and sorting the edge list into a heap
        # Sorted on the basis of their weights
        for source in self.__edgeList:
            for destination,weight in self.__edgeList[source].items():
                if (source,destination) not in seenEdges:
                    edgeHeap.append((weight,source,destination))
                    seenEdges.add((destination,source)) 
                    # We add as destination,source because for undirected graph,
                    # we will check for the reverse as the duplicate
        heapq.heapify(edgeHeap) # Heapify the edgeList

        # Traversing the edgeList Heap until |E'| = |V|-1
        while(edgeCount < n-1 and edgeHeap):
            # Emptying the min-heap and extracting the data from each tuple
            weight,source,destination = heapq.heappop(edgeHeap)

            # if nodes are not in a cycle (Disjoint set elements)
            # add node,edge relationship to MST
            # Update edge count
            # Update sets of the source and destination
            # Calculate the total cost (minCost)
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