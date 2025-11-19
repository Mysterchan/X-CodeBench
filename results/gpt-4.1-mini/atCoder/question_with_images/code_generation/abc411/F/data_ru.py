import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
Q = int(input())
X = list(map(int, input().split()))

# DSU with edge count tracking
class DSU:
    __slots__ = ['parent', 'size', 'edge_count']
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.edge_count = [0]*n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        # When merging two components, edges between them become internal edges
        # So total edges in merged component = sum of edges in both + 1 (the merged edge)
        # But we must subtract 1 because the merged edge is counted twice in sum
        # Actually, the merged edge is the one we contract, so it disappears as an edge
        # So total edges = sum edges in both - 1 (merged edge removed)
        # But we add 1 edge for the merged edge? No, merged edge disappears.
        # So total edges = sum edges in both - 1
        # But we must add 1 for the merged edge? No, merged edge is removed.
        # So total edges = sum edges in both - 1
        # Wait, we must be careful:
        # Before union: edges_a, edges_b
        # The merged edge is counted once in edges_a or edges_b? No, it's counted once in total edges.
        # Actually, the merged edge is the one connecting a and b, so it is counted once in total edges.
        # After union, this edge disappears (contracted), so total edges decrease by 1.
        # So edges in merged component = edges_a + edges_b - 1
        self.edge_count[a] += self.edge_count[b] - 1
        return True

dsu = DSU(N)
for u,v in edges:
    u -= 1
    v -= 1
    # Initially, each edge connects two different vertices, so add 1 edge to each component
    # But initially each vertex is separate, so edge_count is 0 for each vertex
    # We will add edges after union
    # So we just store edges and add them after union
    # But we can add edges now, and union later
    # Instead, we can add edges after union
    # But initial graph is disconnected, so edge_count is 0 for each vertex
    # We will add edges after union
    # So we just store edges and add them after union
    # Actually, we can add edges now, but union later
    # So we just add edges after union
    # So we do nothing here
    pass

# We need to build initial DSU with edges counted
# So we union all edges and count edges in components
# But initial graph is G0, no contractions yet
# So we union all edges and count edges in components
# But problem states initial graph G0 with N vertices and M edges
# So initially, each vertex is separate, edge_count=0
# We union edges and edge_count += 1 for each edge
# So let's union edges and add edge_count

# Let's do union with edge_count increment
# But union merges components and edge_count sums
# So we need a special union for initial graph

# Let's implement union_init for initial graph
def union_init(dsu, a, b):
    a = dsu.find(a)
    b = dsu.find(b)
    if a == b:
        dsu.edge_count[a] += 1
        return
    if dsu.size[a] < dsu.size[b]:
        a, b = b, a
    dsu.parent[b] = a
    dsu.size[a] += dsu.size[b]
    dsu.edge_count[a] += dsu.edge_count[b] + 1

for i,(u,v) in enumerate(edges):
    union_init(dsu, u-1, v-1)

total_edges = M

res = []
for xi in X:
    xi -= 1
    u, v = edges[xi]
    u -= 1
    v -= 1
    ru = dsu.find(u)
    rv = dsu.find(v)
    if ru != rv:
        # Contract edge between ru and rv
        # total edges decrease by 1 (edge contracted)
        # but also edges inside merged component = sum edges - 1
        # total edges decrease by 1
        dsu.union(ru, rv)
        total_edges -= 1
    # else do nothing
    res.append(str(total_edges))

print('\n'.join(res))