class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank ={}
    
    def makeSet(self, list):
        for element in list:
            self.parent[element] = element
            self.rank[element] = 0

    def find(self, val):
        if(self.parent[val] == val): return val
        self.parent[val] = self.find(self.parent[val]) # Collapsing find
    
    def union(self, x,y):
        parentX = self.find(x)
        parentY = self.find(y)

        # if both already in the same set, no need to do anything
        if(parentX == parentY): return

        # select the parent with higher rank
        if(self.rank[parentX] > self.rank[parentY]): self.parent[parentY] = parentX
        elif(self.rank[parentX] < self.rank[parentY]): self.parent[parentX] = parentY
        # if both parents have same rank, choose one as the parent and increase rank
        else:
            self.parent[parentY] = parentX
            self.rank[parentX] += 1