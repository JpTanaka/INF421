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

    def set_parent(self, u, parent):
        self.parents[u] = parent

    def get_parent(self, u):
        return self.parents[u]

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

    def find_root_no_compression(self, u):
            parent = self.parents[u]
            if u == parent: return u
            else: return self.find_root_no_compression(parent); 
        
    def find_root(self, v):
        parent = self.parents[v]
        if v == parent:
            return v
        new_parent = self.find_root(parent)
        self.parents[v] = new_parent # path compression
        return new_parent


    def union_vertices_color_set(self,  v1, v2, depth_v1, depth_v2):
            if (depth_v1 < depth_v2): 
                self.parents[v2] = v1

            else:
                self.parents[v2] = v1
        
    