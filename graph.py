from union_find import UnionFind
from collections import deque
import json


def max_power2_jump(n, m):
    power = 0
    dist = max(n, m) - min(n, m)
    while (2**power) <= dist:
        power += 1
    return power - 1


class Graph:
    def __init__(self, n, m):
        # edges_general contains triplets edges_general = [(v_1, v_2, w), (v_2, v_3, w), ...]
        self.edges_general = []
        # edges contains all edges of a node, edges[v1][v2] = weight between v1 and v2 = edges[v1][v2]
        self.edges = {i + 1: {} for i in range(n)}
        self.mst = None
        self.depth_mp = {}
        self.ancestors_mp = {}

        self.n = n
        self.m = m
        self.mst_UF = UnionFind(n)

    def countEdges(self):
        return len(self.edges_general)

    def addEdges(self, edges):
        for i in edges:
            self.addEdge(i[0], i[1], i[2])

    def addEdge(self, v1, v2, w):
        if v2 not in self.edges[v1].keys():
            self.edges[v2][v1] = w
            self.edges[v1][v2] = w
        else:
            self.edges[v2][v1] = min(w, self.edges[v2][v1])
            self.edges[v1][v2] = min(w, self.edges[v1][v2])
        self.edges_general.append((v1, v2, w))

    def printGraph(self):
        print(json.dumps(self.edges, indent=4))
    def printMST(self):
        print(json.dumps(self.mst, indent=4))

    def make_mst(self):
        """
        make_mst: mst will follow the same structure of edges
        """
        if self.m == self.n - 1:
            self.mst = self.edges
            return
        self.mst = {i + 1: {} for i in range(self.n)}
        priority_queue = sorted(self.edges_general, key=lambda x: x[2])

        count = 0
        x = 0
        while count < self.n - 1:
            curr_edge = priority_queue[x]
            if self.mst_UF.find_parent(curr_edge[0] - 1) != self.mst_UF.find_parent(
                curr_edge[1] - 1
            ):
                self.mst[curr_edge[0]][curr_edge[1]] = curr_edge[2]
                self.mst[curr_edge[1]][curr_edge[0]] = curr_edge[2]
                self.mst_UF.union_vertices(curr_edge[0] - 1, curr_edge[1] - 1)
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
            seen.append(curr)

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

    def get_ancestors(self):
        dfs = deque()
        dfs.appendleft(1)
        curr_parent = 1

        seen = set()
        seen.add(1)
        ancestor_vector = []
        count=0
        while dfs:
            curr_parent = dfs.pop()
            for child_node, weight in self.mst[curr_parent].items():
                if child_node in seen:
                    continue
                
                self.ancestors_mp[child_node] = [(curr_parent, weight)]
                ancestor_vector.clear()
                seen.add(child_node)
                dfs.append(child_node)
            count+=1
        print("asdf")
        log_2_n = max_power2_jump(self.n, 0)
        self.ancestors_mp[1] = [(1, 0)]

        new_ancestor = None
        for j in range(1, log_2_n):
            for v in range(1, self.n+1):
                ancestor, weight = self.ancestors_mp[v][j-1]
                new_ancestor = (
                    self.ancestors_mp[ancestor][j-1][0],
                    max(weight, self.ancestors_mp[ancestor][j-1][1]),
                )

                self.ancestors_mp[v].append(new_ancestor)


    def get_same_level(self, u, v, weight):

        depth_u = self.depth_mp[u]
        depth_v = self.depth_mp[v]

        if depth_u < depth_v:
            u, v = v, u
        if depth_u == depth_v:
            return (u, weight)

        jump = max_power2_jump(depth_u, depth_v)
        print(depth_u, depth_v, u, v)
        weight = max(weight, self.ancestors_mp[u][jump][1])

        return self.get_same_level(self.ancestors_mp[u][jump][0], v, weight)

    def itineraries_v2(self, u, v):
        depth_u = self.depth_mp[u]
        depth_v = self.depth_mp[v]

        if depth_v > depth_u:
            u, v = v, u

        max_weight = 0
        u, max_weight = self.get_same_level(u, v, max_weight)
        if u == 1:
            return max_weight
        if u == v:
            return max_weight

        jump = -1

        while True:
            jump += 1

            if self.ancestors_mp[u][0][0] == self.ancestors_mp[v][0][0]:
                return max(
                    max_weight,
                    max(self.ancestors_mp[u][0][1], self.ancestors_mp[v][0][1]),
                )

            if (
                len(self.ancestors_mp[u]) < jump
                or self.ancestors_mp[u][jump][0] == self.ancestors_mp[v][jump][0]
            ):
                max_weight = max(
                    max_weight,
                    max(
                        self.ancestors_mp[u][jump-1][1],
                        self.ancestors_mp[v][jump-1][1],
                    ),
                )
                u, v = (
                    self.ancestors_mp[u][jump-1][0],
                    self.ancestors_mp[v][jump-1][0],
                )
                jump = -1
