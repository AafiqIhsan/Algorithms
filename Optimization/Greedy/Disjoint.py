class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def makeSet(self, elements):
        for x in elements:
            self.parent[x] = x
            self.rank[x] = 0
    
    def find(self,x):
        if(self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)

        if(rootX == rootY):
            return
        
        if (self.rank[rootX] < self.rank[rootY]):
            self.parent[rootX] = rootY
        elif (self.rank[rootX] > self.rank[rootY]):
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1