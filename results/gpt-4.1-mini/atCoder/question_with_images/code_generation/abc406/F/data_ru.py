import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)]
edge_list = [None]*(N)  # 1-based indexing for edges

for i in range(1, N):
    u, v = map(int, input().split())
    edges[u].append((v, i))
    edges[v].append((u, i))

# We root the tree at 1
parent = [0]*(N+1)
depth = [0]*(N+1)
subtree_size = [0]*(N+1)
edge_to_child = [0]*(N)  # edge i connects parent to child edge_to_child[i]

def dfs(u, p):
    subtree_size[u] = 1
    for v, eid in edges[u]:
        if v == p:
            continue
        parent[v] = u
        depth[v] = depth[u] + 1
        dfs(v, u)
        subtree_size[u] += subtree_size[v]
        # edge eid connects u and v, since u is parent of v, store v as child for edge eid
        edge_to_child[eid] = v

dfs(1, 0)

# Fenwick tree (BIT) for weights
# Initially all weights = 1
# We'll store weights per vertex, and support point updates and prefix sums

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.fw = [0]*(n+1)
    def update(self, i, delta):
        while i <= self.n:
            self.fw[i] += delta
            i += i & (-i)
    def query(self, i):
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & (-i)
        return s
    def range_sum(self, l, r):
        return self.query(r) - self.query(l-1)

# We need to map vertices to positions in Fenwick tree.
# Since we only need subtree sums, we can use Euler Tour or DFS order.
# We'll do a DFS order and assign in[u] and out[u] to represent subtree of u.

in_order = [0]*(N+1)
out_order = [0]*(N+1)
time = 0

def dfs_order(u):
    nonlocal time
    time += 1
    in_order[u] = time
    for v, _ in edges[u]:
        if v == parent[u]:
            continue
        dfs_order(v)
    out_order[u] = time

dfs_order(1)

fenw = Fenwick(N)
# Initialize all weights = 1
for i in range(1, N+1):
    fenw.update(in_order[i], 1)

total_weight = N

Q = int(input())
res = []
for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        # 1 x w: increase weight of vertex x by w
        x, w = int(query[1]), int(query[2])
        fenw.update(in_order[x], w)
        total_weight += w
    else:
        # 2 y: remove edge y, split tree into two subtrees
        y = int(query[1])
        c = edge_to_child[y]  # child vertex of edge y
        # subtree weight of c
        w_sub = fenw.range_sum(in_order[c], out_order[c])
        diff = abs(total_weight - 2*w_sub)
        res.append(str(diff))

print('\n'.join(res))