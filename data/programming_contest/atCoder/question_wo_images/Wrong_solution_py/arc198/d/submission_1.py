class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

n = int(input())
adjacent = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adjacent[u].append(v)
    adjacent[v].append(u)

a = [list(map(int, list(input()))) for _ in range(n)]

direction = [[0]*n for _ in range(n)]
for i in range(n):
    stack = [i]
    visited = [False] * n
    visited[i] = True
    while stack:
        v = stack.pop()
        for u in adjacent[v]:
            if not visited[u]:
                visited[u] = True
                direction[u][i] = v
                stack.append(u)

for i in range(n):
    direction[i][i] = i

uf = UnionFind(n)
stack = [(i,j) for i in range(n) for j in range(i+1, n) if a[i][j] == 1]

while stack:
    i, j = stack.pop()
    if i == j:
        continue
    if uf.find(i) == uf.find(j):
        continue
    uf.union(i, j)
    if direction[i][j] == j:
        continue
    stack.append((direction[i][j], direction[j][i]))

flag = [[None] * n for _ in range(n)]
stack = [(i,j) for i in range(n) for j in range(n)]
ans = 0

while stack:

    i, j = stack.pop()
    if flag[i][j] is not None:
        continue
    if flag[j][i] is not None:
        flag[i][j] = flag[j][i]
        if flag[i][j]:
            ans += 1
        continue
    if i == j:
        flag[i][j] = True
        ans += 1
        continue
    if uf.find(i) != uf.find(j):
        flag[i][j] = False
        continue
    if direction[i][j] == j:
        flag[i][j] = True
        ans += 1
        continue
    if flag[direction[i][j]][direction[j][i]] is not None:
        flag[i][j] = flag[direction[i][j]][direction[j][i]]
        if flag[i][j]:
            ans += 1
        continue
    if flag[direction[j][i]][direction[i][j]] is not None:
        flag[i][j] = flag[direction[j][i]][direction[i][j]]
        if flag[i][j]:
            ans += 1
        continue
    stack.append((i,j))
    stack.append((direction[i][j], direction[j][i]))

print(ans)