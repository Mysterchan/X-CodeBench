class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
        self.edge_count = 0

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
                self.size[root_u] += self.size[root_v]
                self.edge_count -= 1
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
                self.edge_count -= 1
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
                self.rank[root_u] += 1
                self.edge_count -= 1

    def add_edge(self):
        self.edge_count += 1

    def get_edge_count(self):
        return self.edge_count


import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]
Q = int(data[M + 1])
queries = list(map(int, data[M + 2].split()))

uf = UnionFind(N)
graph = defaultdict(set)

for u, v in edges:
    graph[u - 1].add(v - 1)
    graph[v - 1].add(u - 1)
    uf.add_edge()

positions = list(range(N))

results = []

for x in queries:
    u, v = edges[x - 1]
    u -= 1
    v -= 1

    pos_u = positions[u]
    pos_v = positions[v]

    if pos_u != pos_v and v in graph[pos_u]:
        new_vertex = N
        N += 1

        for neighbor in graph[pos_u].union(graph[pos_v]):
            if neighbor != pos_u and neighbor != pos_v:
                graph[new_vertex].add(neighbor)
                graph[neighbor].add(new_vertex)

        graph[new_vertex].add(new_vertex)
        graph[new_vertex].discard(pos_u)
        graph[new_vertex].discard(pos_v)

        positions.append(new_vertex)
        uf.union(pos_u, pos_v)

        del graph[pos_u]
        del graph[pos_v]

    results.append(uf.get_edge_count())

print("\n".join(map(str, results)))