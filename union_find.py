class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.nElements = n

    def find_parent(self, v):
        parent = self.parents[v]
        if v == parent:
            return v
        newParent = self.find_parent(parent)
        self.parents[v] = newParent
        return newParent

    def union_vertices(self, v1, v2):
        parent1 = self.find_parent(v1)
        parent2 = self.find_parent(v2)
        if parent1 == parent2:
            return

        if self.rank[parent1] < self.rank[parent2]:
            self.parents[parent2] = parent1
        elif self.rank[parent1] > self.rank[parent2]:
            self.parents[parent1] = parent2
        else:
            self.parents[parent2] = parent1
            self.rank[parent1] += 1
