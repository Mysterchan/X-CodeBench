import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
Q = int(input())
X = list(map(int, input().split()))

# Union-Find (Disjoint Set Union) with edge count tracking
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [1]*n
        self.edge_count = [0]*n  # number of edges inside the component

    def find(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            # Adding an edge inside the same component increases edge count by 1
            self.edge_count[x] += 1
            return False
        # Union by size
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.par[y] = x
        self.size[x] += self.size[y]
        # When merging two components, total edges = sum of edges + 1 (the new edge)
        self.edge_count[x] += self.edge_count[y] + 1
        return True

    def get_edge_count(self, x):
        return self.edge_count[self.find(x)]

uf = UnionFind(N)

# Initially, no edges are contracted, so edge count is 0 for all
# We will process queries in order, contracting edges if possible

# We need to know the current position of each piece (initially piece i on vertex i)
# But since vertices are merged, the piece i is on uf.find(i-1)

# For each query:
# - get edge X_i (1-based)
# - check if the two endpoints are in different components
# - if yes, union them (contract edge)
# - output current total number of edges in the graph

# The total number of edges in the graph after contractions is sum of edges in all components
# But since components are disjoint, total edges = sum of edge_count of all roots
# We can maintain total edges by updating it on each union

total_edges = 0
res = []
for xi in X:
    u, v = edges[xi-1]
    u -= 1
    v -= 1
    ru = uf.find(u)
    rv = uf.find(v)
    if ru != rv:
        # union returns True if merged
        # Before union, total edges = sum of edge_count of all components
        # After union, edge_count of new root = edge_count[ru] + edge_count[rv] + 1
        # So total_edges += 1 (the new edge) and remove old edge counts of ru and rv, add new
        total_edges -= uf.edge_count[ru]
        total_edges -= uf.edge_count[rv]
        uf.union(ru, rv)
        r = uf.find(ru)
        total_edges += uf.edge_count[r]
    else:
        # same component, adding an edge inside increases edge_count by 1
        # so total_edges += 1
        uf.edge_count[ru] += 1
        total_edges += 1
    res.append(total_edges)

print('\n'.join(map(str, res)))