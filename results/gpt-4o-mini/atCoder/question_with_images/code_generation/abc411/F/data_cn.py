class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.edges = [set() for _ in range(n)]
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
                self.edges[root_u].update(self.edges[root_v])
                self.edges[root_u].add((u, v))
                self.edges[root_u].add((v, u))
                self.edges[root_v] = set()
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.edges[root_v].update(self.edges[root_u])
                self.edges[root_v].add((u, v))
                self.edges[root_v].add((v, u))
                self.edges[root_u] = set()
            else:
                self.parent[root_v] = root_u
                self.edges[root_u].update(self.edges[root_v])
                self.edges[root_u].add((u, v))
                self.edges[root_u].add((v, u))
                self.edges[root_v] = set()
                self.rank[root_u] += 1
            return True
        return False

    def add_edge(self, u, v):
        if (u, v) not in self.edges[self.find(u)]:
            self.edges[self.find(u)].add((u, v))
            self.edges[self.find(v)].add((v, u))
            self.edge_count += 1

    def get_edge_count(self):
        return self.edge_count


import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]
Q = int(data[M + 1])
queries = list(map(int, data[M + 2].split()))

uf = UnionFind(N)

for u, v in edges:
    uf.add_edge(u - 1, v - 1)

results = []
for x in queries:
    u, v = edges[x - 1]
    u -= 1
    v -= 1
    if uf.find(u) != uf.find(v):
        if (u, v) in uf.edges[uf.find(u)] or (v, u) in uf.edges[uf.find(v)]:
            uf.union(u, v)
    results.append(uf.get_edge_count())

print("\n".join(map(str, results)))