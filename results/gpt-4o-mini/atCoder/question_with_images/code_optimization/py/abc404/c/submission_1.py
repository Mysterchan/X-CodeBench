class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

N, M = map(int, input().split())
if M != N:  # A cycle must have exactly N edges
    print("No")
    exit()

uf = UnionFind(N)
degree = [0] * N

for _ in range(M):
    A, B = map(int, input().split())
    uf.union(A - 1, B - 1)
    degree[A - 1] += 1
    degree[B - 1] += 1

# Check if all nodes have degree 2 and there's a single connected component
if all(d == 2 for d in degree) and len(set(uf.find(i) for i in range(N))) == 1:
    print("Yes")
else:
    print("No")