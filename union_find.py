class UnionFind:
    def __init__(self, n=0):
        self.parents = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.nElements = n

    def findParent(self, v):
        parent = self.parents[v]
        if v == parent:
            return v
        newParent = self.findParent(parent)
        self.parents[v] = newParent
        return newParent

    def unionVertices(self, v1, v2):
        parent1 = self.findParent(v1)
        parent2 = self.findParent(v2)

        if parent1 == parent2:
            return

        if self.rank[parent1] < self.rank[parent2]:
            self.parents[parent1] = parent2
        elif self.rank[parent1] > self.rank[parent2]:
            self.parents[parent2] = parent1
        else:
            self.parents[parent2] = parent1
            self.rank[parent1] += 1
