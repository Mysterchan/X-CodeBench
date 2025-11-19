class Graph:
    def __init__(self, n, edges):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
        self.edges = edges
        self.edge_count = len(edges)
        self.current_edges = set((min(u, v), max(u, v)) for u, v in edges)
        self.chips = list(range(n + 1))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

    def compress_edge(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return 0

        new_vertex = max(self.parent) + 1
        self.parent.append(new_vertex)
        self.rank.append(1)

        # Merge chips
        chips_u = [i for i in range(1, len(self.chips)) if self.find(i) == root_u]
        chips_v = [i for i in range(1, len(self.chips)) if self.find(i) == root_v]

        for chip in chips_u + chips_v:
            self.chips[chip] = new_vertex

        # Count new edges
        new_edges = set()
        for (x, y) in self.current_edges:
            if self.find(x) == root_u or self.find(x) == root_v:
                if self.find(y) != new_vertex:
                    new_edges.add((min(new_vertex, y), max(new_vertex, y)))
            else:
                new_edges.add((x, y))

        self.current_edges = new_edges
        return len(self.current_edges)

import sys
input = sys.stdin.read

data = input().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]
q = int(data[m + 1])
queries = list(map(int, data[m + 2].split()))

graph = Graph(n, edges)
results = []

for x in queries:
    u, v = edges[x - 1]
    if graph.find(u) != graph.find(v):
        graph.compress_edge(u, v)
    results.append(len(graph.current_edges))

print("\n".join(map(str, results)))