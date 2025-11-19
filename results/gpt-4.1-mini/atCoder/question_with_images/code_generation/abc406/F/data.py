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
heavy = [0]*(N+1)

def dfs(u):
    size = 1
    max_subtree = 0
    for v, _ in edges[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        depth[v] = depth[u] + 1
        sz = dfs(v)
        if sz > max_subtree:
            max_subtree = sz
            heavy[u] = v
        size += sz
    subtree_size[u] = size
    return size

parent[1] = -1
dfs(1)

# HLD arrays
head = [0]*(N+1)
pos = [0]*(N+1)
current_pos = 0

def decompose(u, h):
    nonlocal current_pos
    head[u] = h
    pos[u] = current_pos
    current_pos += 1
    if heavy[u]:
        decompose(heavy[u], h)
    for v, _ in edges[u]:
        if v != parent[u] and v != heavy[u]:
            decompose(v, v)

decompose(1,1)

# Fenwick tree (BIT) for weights
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    def update(self, i, x):
        i += 1
        while i <= self.n:
            self.bit[i] += x
            i += i & (-i)
    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s
    def range_query(self, l, r):
        return self.query(r) - self.query(l-1)

# Initialize Fenwick with all weights = 1
fenw = Fenwick(N)
for i in range(N):
    fenw.update(i, 1)

# We need to identify for each edge which vertex is the child in the rooted tree
# Store for each edge the child vertex (the one with greater depth)
edge_to_child = [0]*(N)  # 1-based edge indexing

for u in range(1, N+1):
    for v, eid in edges[u]:
        if parent[v] == u:
            edge_to_child[eid] = v
        elif parent[u] == v:
            edge_to_child[eid] = u

Q = int(input())
total_weight = N  # sum of all weights, initially all 1

output = []
for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        x = int(query[1])
        w = int(query[2])
        fenw.update(pos[x], w)
        total_weight += w
    else:
        y = int(query[1])
        c = edge_to_child[y]
        # sum of subtree rooted at c
        # subtree nodes are contiguous in pos array from pos[c] to pos[c]+subtree_size[c]-1
        s = fenw.range_query(pos[c], pos[c]+subtree_size[c]-1)
        diff = abs(total_weight - 2*s)
        output.append(str(diff))

print('\n'.join(output))