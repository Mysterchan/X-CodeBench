class UnionFind:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self._size = [1] * N
        self.count = 0
    def root(self,a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    def is_same(self,a,b):
        return self.root(a) == self.root(b)
    def unite(self,a,b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return
        if self._size[ra] < self._size[rb]: ra,rb = rb,ra
        self._size[ra] += self._size[rb]
        self.parent[rb] = ra
        self.count += 1
    def size(self,a):
        return self._size[self.root(a)]

import sys
input = sys.stdin.readline
N = int(input())
UV = [tuple(map(int,input().split())) for _ in range(N-1)]
A = [list(map(int,input().rstrip())) for _ in range(N)]

es = [[] for _ in range(N)]
for u,v in UV:
    u,v = u-1,v-1
    es[u].append(v)
    es[v].append(u)

INF = 10**18
dist = [[INF]*N for _ in range(N)]
first = [[-1]*N for _ in range(N)]
from collections import deque
q = deque()
for i in range(N):
    dist[i][i] = 0
    q.append((i,-1))
    while q:
        v,f = q.popleft()
        for u in es[v]:
            if dist[i][u] == INF:
                dist[i][u] = dist[i][v] + 1
                nf = u if f==-1 else f
                first[i][u] = nf
                q.append((u,nf))

edges = [[] for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        d = dist[i][j]
        edges[d].append((i,j))

uf = UnionFind(N)
is_pali = [[0]*N for _ in range(N)]
for i in range(N):
    is_pali[i][i] = 1
for d in range(N-1, 0, -1):
    for u,v in edges[d]:
        if A[u][v]:
            if d >= 2:
                A[first[u][v]][first[v][u]] = A[first[v][u]][first[u][v]] = 1
            uf.unite(u,v)
            is_pali[u][v] = is_pali[v][u] = 1

for d in range(1,N):
    for u,v in edges[d]:
        if A[u][v]: continue
        if uf.is_same(u,v) and (d==1 or is_pali[first[u][v]][first[v][u]]):
            is_pali[u][v] = is_pali[v][u] = 1
print(sum(sum(row) for row in is_pali))