from collections import defaultdict

class UnionFind():

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def __str__(self):
        return '\n'.join(f'{r}:{m}' in self.all_group_members().items())

N, M = list(map(int, input().split()))
uf = UnionFind(N)
G = [list() for _ in range(N)]
for i in range(M):
    A, B = list(map(int, input().split()))
    uf.union(A-1, B-1)
    G[A-1].append(B-1)
    G[B-1].append(A-1)

ans = 'Yes'
for g in G:
    if len(g)!=2 or not uf.group_count()==1:
        ans = 'No'
print(ans)