class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


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
viewed = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] == 1:
            if not viewed[i][j]:
                viewed[i][j] = True
                uf.union(i, j)
                stack = [(i, j), (direction[i][j], direction[j][i])]
                while stack:
                    x, y = stack.pop()
                    if x != y:
                        next_direction_x = direction[x][y]
                        next_direction_y = direction[y][x]
                        if not viewed[x][y]:
                            viewed[x][y] = True
                            uf.union(x, y)
                            if next_direction_x != y: 
                                stack.append((next_direction_x, next_direction_y))

flag = [[None] * n for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(i, n):
        if flag[i][j] is None:
            if i == j:
                flag[i][j] = True
                ans += 1
            elif uf.find(i) == uf.find(j):
                if direction[i][j] == j:
                    flag[i][j] = True
                    ans += 1
                else:
                    flag[i][j] = False

print(ans)