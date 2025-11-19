import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
Q = int(input())
X = list(map(int, input().split()))

# DSU with edge count tracking
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.edge_count = [0]*n  # edges inside each component

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
        # merge y into x
        self.parent[y] = x
        self.size[x] += self.size[y]
        # When merging two components, edges inside new component:
        # sum of edges in both + 1 (the merged edge)
        self.edge_count[x] += self.edge_count[y] + 1
        return True

dsu = DSU(N)
total_edges = M

# Initially, each edge is between two different components
# So total edges = sum of edge_count in all components
# Initially edge_count = 0 for all, total_edges = M

# We need to know for each edge which vertices it connects
# and for each operation, check if the two vertices are in different components
# If yes, union them and update total_edges accordingly

for i in range(M):
    u, v = edges[i]
    # no union now, just initial graph

res = []
for xi in X:
    u, v = edges[xi-1]
    ru = dsu.find(u-1)
    rv = dsu.find(v-1)
    if ru != rv:
        # union reduces total edges by 1 (the merged edge)
        # but inside union we add 1 to edge_count[x], so total_edges -= 1
        # Actually total_edges = sum of edge_count in all components
        # After union, edge_count[x] = edge_count[x] + edge_count[y] + 1
        # So total_edges = total_edges - 1
        dsu.union(ru, rv)
        total_edges -= 1
    res.append(total_edges)

print('\n'.join(map(str, res)))