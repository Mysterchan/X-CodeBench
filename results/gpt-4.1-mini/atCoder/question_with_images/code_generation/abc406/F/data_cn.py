import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N-1)]

# 建樹
graph = [[] for _ in range(N+1)]
for i, (u, v) in enumerate(edges, 1):
    graph[u].append((v, i))
    graph[v].append((u, i))

# 父節點與子節點判定（以1為根）
parent = [0]*(N+1)
edge_to_child = [0]*(N)  # edge i 對應的子節點（i從1開始）
visited = [False]*(N+1)

def dfs(u):
    visited[u] = True
    for v, eid in graph[u]:
        if not visited[v]:
            parent[v] = u
            edge_to_child[eid-1] = v
            dfs(v)

dfs(1)

Q = int(input())
weight = [1]*(N+1)
total_weight = N

# Fenwick Tree (BIT) 用於點權重更新與子樹權重查詢
# 先用 dfs 序列化樹，方便用 BIT 查詢子樹權重
in_time = [0]*(N+1)
out_time = [0]*(N+1)
time = 0

def dfs2(u):
    nonlocal time
    time += 1
    in_time[u] = time
    for v, _ in graph[u]:
        if v != parent[u]:
            dfs2(v)
    out_time[u] = time

dfs2(1)

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.fw = [0]*(n+1)
    def update(self, i, v):
        while i <= self.n:
            self.fw[i] += v
            i += i & (-i)
    def query(self, i):
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & (-i)
        return s
    def range_query(self, l, r):
        return self.query(r) - self.query(l-1)

fenw = Fenwick(N)
for i in range(1, N+1):
    fenw.update(in_time[i], 1)

res = []
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        x, w = int(q[1]), int(q[2])
        weight[x] += w
        fenw.update(in_time[x], w)
        total_weight += w
    else:
        y = int(q[1])
        c = edge_to_child[y-1]
        sub_w = fenw.range_query(in_time[c], out_time[c])
        diff = abs(total_weight - 2*sub_w)
        res.append(str(diff))

print('\n'.join(res))