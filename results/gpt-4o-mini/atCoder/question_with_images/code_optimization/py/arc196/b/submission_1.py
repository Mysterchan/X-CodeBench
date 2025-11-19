class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_conn_comp = n

    def leader(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.leader(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        x, y = self.leader(x), self.leader(y)
        if x == y:
            return -1
        self.num_conn_comp -= 1
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.size[x] += self.size[y]
        self.parent[y] = x
        return x

    def issame(self, x, y):
        return self.leader(x) == self.leader(y)

    def getsize(self, x):
        return self.size[self.leader(x)]

    def groups(self):
        group_map = {}
        for i in range(len(self.parent)):
            root = self.leader(i)
            if root not in group_map:
                group_map[root] = [0, 0]
            if i < len(self.parent) // 2:
                group_map[root][0] += 1
            else:
                group_map[root][1] += 1
        return list(group_map.values())

import sys

MOD = 998244353
p2 = [1] * (10**6 + 1)
for i in range(1, 10**6 + 1):
    p2[i] = (2 * p2[i - 1]) % MOD

def solve(H, W, b):
    UF = UnionFind(H * W * 4)
    for i in range(H):
        for j in range(W):
            t = 4 * (i * W + j)
            if b[i][j] == "A":
                UF.merge(t, t + 2)
                UF.merge(t + 1, t + 3)
            else:
                UF.merge(t, t + 1)
                UF.merge(t + 2, t + 2 + 1)  # merge with shifted index
                UF.merge(t + 1, t + 3)

            UF.merge(t + 2, (t + 4 * W) if i != H - 1 else 4 * j)
            UF.merge(t + 3, (t + 4 + 1) if j != W - 1 else (4 * (i * W + 0) + 1))
    
    if not (UF.issame(0, 4)) and not (UF.issame(1, 5)):
        return 0

    cnt = UF.num_conn_comp
    return p2[cnt // 2]

input = sys.stdin.read
data = input().splitlines()
T = int(data[0])
results = []
idx = 1
for _ in range(T):
    H, W = map(int, data[idx].split())
    b = data[idx + 1:idx + 1 + H]
    results.append(str(solve(H, W, b)))
    idx += H + 1

print("\n".join(results))