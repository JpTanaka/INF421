from union_find import UnionFind

class Graph:
    def __init__(self, n, m):
        # edges contains triplets (v_1, v_2, w)
        self.edges =  []
        self.mst = []
        self.mst_UF = UnionFind()
        self.depth_mp = {}
        self.ancestors_mp = {}

        for i in range(1, n + 1):
            self.edges[i] = {}

        self.n = n
        self.m = m
        self.mst_UF = UnionFind(n)

    def countEdges(self):
        count = 0
        for node1, val1 in self.edges.items():
            for node2, weight in val1.items():
                count += 1
        return count

    def addEdge(self, v1, v2, w):
        self.edges.append((v1, v2, w))


    def make_mst(self):
        if self.m == self.n - 1:
            self.mst = self.edges
            return
            
        
        priority_queue = sorted(self.edges, key=lambda x: x[2])

        count = 0
        x = 0
        while count < self.n - 1:
            curr_edge = priority_queue[x]
            if self.mst_UF.find_parent(curr_edge[0]) != self.mst_UF.find_parent(curr_edge[1]):
                self.mst.append((curr_edge[0], curr_edge[1], curr_edge[2]))
                self.mst_UF.union_vertices(curr_edge[0], curr_edge[1])
                count += 1
            x += 1

    def itineraries_v1(self, u, v):
        if not self.mst:
            self.make_mst()
            
        inverse_path = {}
        seen = []
        graph_stack = [u]
        
        while graph_stack:
            curr = graph_stack.pop()
            if curr == v:
                break
            if curr in seen:
                continue
            seen.add(curr)
            
            for neighbor, weight in self.mst[curr].items():
                graph_stack.append(neighbor)
                if neighbor not in seen:
                    inverse_path[neighbor] = curr
        
        max_weight = 0
        curr_node = v
        
        while curr_node != u:
            next_node = inverse_path[curr_node]
            max_weight = max(max_weight, self.mst[curr_node][next_node])
            curr_node = next_node
            
        return max_weight
    
    
