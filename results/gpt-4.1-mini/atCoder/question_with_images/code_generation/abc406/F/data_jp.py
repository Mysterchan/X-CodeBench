import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N-1)]

Q = int(input())
queries = [input().split() for _ in range(Q)]

# 木の構造を作成
graph = [[] for _ in range(N+1)]
for i, (u, v) in enumerate(edges, 1):
    graph[u].append((v, i))
    graph[v].append((u, i))

# 親子関係を決めるためにDFSで根を1に固定して探索
parent = [0]*(N+1)
edge_to_child = [0]*(N)  # 辺iが親->子の向きで子の頂点を記録（1-indexed）
def dfs(u):
    for v, ei in graph[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        edge_to_child[ei-1] = v
        dfs(v)
parent[1] = -1
dfs(1)

# 各頂点の重みは初期値1
weights = [1]*(N+1)
total_weight = N  # 全頂点の重みの合計

# BIT(Fenwick Tree)で頂点の重みを管理
# 頂点の重みの増減を高速に行い、部分木の重み和を求めるために
# 頂点のin-time順に重みを管理する方法があるが、
# 今回は部分木の重み和は使わず、辺を切ったときの部分木の重み和を
# 頂点の重みの合計から部分木の重みを引く形で求めるため、
# 部分木の重み和を求める必要がある。
# そこで、親子関係を決めた木で、頂点のin-timeを求めて部分木の重み和をBITで管理する。

# DFSで頂点のin-timeとout-timeを求める
in_time = [0]*(N+1)
out_time = [0]*(N+1)
time = 0
def dfs_time(u):
    nonlocal time
    time += 1
    in_time[u] = time
    for v, _ in graph[u]:
        if v == parent[u]:
            continue
        dfs_time(v)
    out_time[u] = time
dfs_time(1)

# BIT実装
class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & (-i)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l-1)

bit = BIT(N)
for v in range(1, N+1):
    bit.add(in_time[v], 1)

output = []
for query in queries:
    if query[0] == '1':
        x, w = int(query[1]), int(query[2])
        weights[x] += w
        total_weight += w
        bit.add(in_time[x], w)
    else:
        y = int(query[1])
        c = edge_to_child[y-1]
        # cの部分木の重み和
        sub_w = bit.range_sum(in_time[c], out_time[c])
        diff = abs(total_weight - 2*sub_w)
        output.append(str(diff))

print('\n'.join(output))