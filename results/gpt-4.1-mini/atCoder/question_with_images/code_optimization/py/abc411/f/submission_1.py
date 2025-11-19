import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
UV = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
Q = int(input())
X = list(map(lambda x: int(x)-1, input().split()))

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.edge_count = [0]*n  # number of edges inside each component
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.edge_count[x] += self.edge_count[y] + 1
        return True
    def add_edge(self, x):
        x = self.find(x)
        self.edge_count[x] += 1
    def get_edge_count(self, x):
        return self.edge_count[self.find(x)]

uf = UnionFind(N)
for u,v in UV:
    uf.add_edge(u)
    uf.add_edge(v)

total_edges = M
res = []
for x in X:
    u,v = UV[x]
    ru, rv = uf.find(u), uf.find(v)
    if ru != rv:
        # Check if edge exists between ru and rv: since edges are unique and given,
        # and we only contract edges that exist between pieces' vertices,
        # the edge x connects ru and rv if ru != rv.
        # So we can union and update total_edges accordingly.
        # When merging two components, the new edge count is:
        # edge_count[ru] + edge_count[rv] + 1 (the contracted edge)
        # But total edges decrease by 1 because the contracted edge disappears,
        # and multi-edges are merged, so total edges = total_edges - 1
        # Actually, total edges after union = sum of edges in components - 1 (contracted edge)
        # So total_edges = total_edges - 1
        uf.union(u,v)
        total_edges -= 1
    res.append(total_edges)

print('\n'.join(map(str,res)))