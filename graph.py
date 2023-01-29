from union_find import UnionFind
from collections import deque

class Graph:
    def __init__(self, n, m):
        # edges_general contains triplets edges_general = [(v_1, v_2, w), (v_2, v_3, w), ...]
        self.edges_general =  []
        # edges contains all edges of a node, edges[v1][v2] = weight between v1 and v2 = edges[v1][v2]
        self.edges = {i+1: {} for i in range(n)}
        self.mst = {i+1: {} for i in range(n)}
        self.mst_UF = UnionFind()
        self.depth_mp = {}
        self.ancestors_mp = {}

        self.n = n
        self.m = m
        self.mst_UF = UnionFind(n)

    def countEdges(self):
        return len(self.edges_general)

    def addEdge(self, v1, v2, w):
        if v2 not in self.edges[v1].keys:
            self.edges[v2][v1] = w
            self.edges[v1][v2] = w
        else:
            self.edges[v2][v1] = min(w, self.edges[v2][v1])
            self.edges[v1][v2] = min(w, self.edges[v1][v2])
        self.edges_general.append((v1, v2, w))


    def make_mst(self):
        """
            make_mst: mst will follow the same structure of edges
        """
        if self.m == self.n - 1:
            self.mst = self.edges
            return
        
        priority_queue = sorted(self.edges_general, key=lambda x: x[2])

        count = 0
        x = 0
        while count < self.n - 1:
            curr_edge = priority_queue[x]
            if self.mst_UF.find_parent(curr_edge[0]) != self.mst_UF.find_parent(curr_edge[1]):
                # self.mst[curr_edge[0]].append((curr_edge[0], curr_edge[1], curr_edge[2]))
                self.mst[curr_edge[0]][curr_edge[1]] = curr_edge[2]
                self.mst[curr_edge[1]][curr_edge[0]] = curr_edge[2]
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
            
            for neighbor in self.mst[curr].keys():
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
    
    
    def get_depth_map(self):
        bfs = deque([1])
        curr_level = 0
        next_child_counter = 0
        curr_child_counter = 1

        while bfs:
            curr_node = bfs.popleft()
            self.depth_mp[curr_node] = curr_level
            curr_child_counter -= 1

            for child_node in self.mst[curr_node].keys():
                if child_node in self.depth_mp:
                    continue
                bfs.append(child_node)
                next_child_counter += 1

            if not curr_child_counter:
                curr_child_counter = next_child_counter
                next_child_counter = 0
                curr_level += 1

    