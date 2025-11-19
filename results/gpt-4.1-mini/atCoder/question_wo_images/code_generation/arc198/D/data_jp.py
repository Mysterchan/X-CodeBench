import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

A = [list(map(int,list(input().rstrip()))) for _ in range(N)]

# 1. 木のLCA準備
LOG = 20
parent = [[-1]*N for _ in range(LOG)]
depth = [0]*N

def dfs(v,p,d):
    parent[0][v] = p
    depth[v] = d
    for nv in edges[v]:
        if nv == p:
            continue
        dfs(nv,v,d+1)
dfs(0,-1,0)

for k in range(LOG-1):
    for v in range(N):
        if parent[k][v] < 0:
            parent[k+1][v] = -1
        else:
            parent[k+1][v] = parent[k][parent[k][v]]

def lca(u,v):
    if depth[u] > depth[v]:
        u,v = v,u
    diff = depth[v] - depth[u]
    for i in range(LOG):
        if diff & (1<<i):
            v = parent[i][v]
    if u == v:
        return u
    for i in reversed(range(LOG)):
        if parent[i][u] != parent[i][v]:
            u = parent[i][u]
            v = parent[i][v]
    return parent[0][u]

def get_path(u,v):
    # u->vのパスの頂点列を返す
    w = lca(u,v)
    path_u = []
    cur = u
    while cur != w:
        path_u.append(cur)
        cur = parent[0][cur]
    path_v = []
    cur = v
    while cur != w:
        path_v.append(cur)
        cur = parent[0][cur]
    path = path_u + [w] + path_v[::-1]
    return path

# 2. 問題の本質
# xは頂点の値の配列。x_i = x[i]
# (i,j)のパスが回文であるとは、パス上の頂点のxの値が回文であること。
# A[i][j] = 1 かつ (i,j)が回文ペアでないとスコアは10^100
# そうでなければ、スコアは回文ペアの個数

# 3. 重要な観察
# Aは対称行列で、A[i][i] = 1
# (i,j)が回文ペアでないとスコアが巨大になるので、xはA[i][j]=1のペアのパスが回文になるようにしなければならない
# つまり、A[i][j]=1のとき、パス上の頂点のxの値は回文でなければならない

# 4. パス上の回文制約を満たすxの値の割り当て
# パス上の頂点の値が回文であるためには、
# パスのk番目の頂点と(n+1-k)番目の頂点の値が等しい
# つまり、パス上の頂点の対称位置の頂点の値は等しい

# 5. これをグラフの頂点の同値関係として考える
# 各A[i][j]=1のとき、パス上の頂点の対称位置の頂点同士は同じ値を持つべき
# これをUnion-Findで管理する

class UnionFind:
    def __init__(self,n):
        self.par = list(range(n))
        self.rank = [0]*n
    def find(self,x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True
    def same(self,x,y):
        return self.find(x) == self.find(y)

uf = UnionFind(N)

# 6. A[i][j]=1のとき、パス上の頂点の対称位置の頂点同士をunion
for i in range(N):
    for j in range(i+1,N):
        if A[i][j] == 1:
            path = get_path(i,j)
            n = len(path)
            for k in range(n//2):
                uf.union(path[k], path[n-1-k])

# 7. これでxの値はufのグループごとに同じ値を持てばよい
# 8. スコアの計算
# スコアは、(i,j)でA[i][j]=1かつ(i,j)が回文ペアの個数
# (i,j)が回文ペアとは、パス上の頂点の値が回文
# つまり、パス上の頂点の対称位置の頂点は同じグループに属していること

# 9. (i,j)でA[i][j]=1のとき、パス上の頂点の対称位置の頂点が同じグループかチェック
# もし違うグループがあればスコアは10^100
# そうでなければ、その(i,j)は回文ペア

# 10. (i,j)は対称なのでi<=jだけ調べて2倍、対角(i,i)は1個ずつ加算

score = 0
INF = 10**100

for i in range(N):
    for j in range(i,N):
        if A[i][j] == 1:
            path = get_path(i,j)
            n = len(path)
            ok = True
            for k in range(n//2):
                if not uf.same(path[k], path[n-1-k]):
                    ok = False
                    break
            if not ok:
                print(INF)
                sys.exit()
            if i == j:
                score += 1
            else:
                score += 2

print(score)