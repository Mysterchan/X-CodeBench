class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.num_conn_comp = n

    def leader(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def merge(self, x, y):
        x, y = self.leader(x), self.leader(y)
        if x == y: return -1
        self.num_conn_comp -= 1
        if self.size[x] < self.size[y]:
            x,y=y,x

        self.size[x] += self.size[y]
        self.parent[y] = x
        return x

    def issame(self, x, y):
        return self.leader(x) == self.leader(y)

    def getsize(self,x):
        return self.size[self.leader(x)]

    def all_leaders(self):
        return [i for i,v in enumerate(self.parent) if i==v]

    def groups(self):
        n = len(self.parent)
        gp = [[] for _ in range(n)]
        for v in range(n):
            gp[self.leader(v)].append(v)
        return [lst for lst in gp if lst]

class bipartite():
    def __init__(self, n):
        self.n = n
        self.UF = UnionFind(2*n)
        self.is_bipartite = True

    def add_edge(self,u,v):
        self.UF.merge(u,v+self.n)
        self.UF.merge(u+self.n,v)
        if self.UF.issame(u,u+self.n):
            self.is_bipartite = False

    def add_same(self,u,v):
        self.UF.merge(u,v)
        self.UF.merge(u+self.n,v+self.n)
        if self.UF.issame(u,u+self.n):
            self.is_bipartite = False

    def all_connected_components(self):
        res = []
        used = [0]*self.n
        for lst in self.UF.groups():
            v = lst[0]%self.n
            if used[v]: continue
            x = y = 0
            for v in lst:
                if v < self.n:
                    x += 1
                else:
                    y += 1
                    v -= self.n
                used[v] = 1
            res.append((x,y))
        return res

import sys
readline = sys.stdin.readline

MOD = 998244353
p2 = [1]
for _ in range(10**6):
    p2.append(2*p2[-1]%MOD)

def solve(H,W,b):
    UF = bipartite(H*W*4)

    for i in range(H):
        for j in range(W):
            t = 4*(i*W+j)
            if b[i][j] == "A":
                UF.add_edge(t,t+2)
                UF.add_edge(t+1,t+3)
            else:
                UF.add_edge(t,t+1)

                UF.add_same(t,t+2)
                UF.add_same(t+1,t+3)

            UF.add_same(t+2,(t+4*W) if i != H-1 else 4*j)
            UF.add_same(t+3,(t+4+1) if j != W-1 else (4*(i*W+0)+1) )

    if not UF.is_bipartite:
        return 0
    cnt = UF.UF.num_conn_comp
    return p2[cnt//2]

T = int(readline())
for _ in range(T):
    H,W = map(int,readline().split())
    b = [readline().strip() for _ in range(H)]
    ans = solve(H,W,b)
    print(ans)