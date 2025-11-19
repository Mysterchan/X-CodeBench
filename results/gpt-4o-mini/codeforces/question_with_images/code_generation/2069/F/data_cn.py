class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
        self.component_size = [1] * (n + 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.component_size[root_u] += self.component_size[root_v]
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.component_size[root_v] += self.component_size[root_u]
            else:
                self.parent[root_v] = root_u
                self.component_size[root_u] += self.component_size[root_v]
                self.rank[root_u] += 1

    def size(self, u):
        return self.component_size[self.find(u)]

def min_edges_to_include(A_components, B_components):
    A_sizes = [0] * (len(A_components) + 1)
    for size in A_components:
        A_sizes[size] += 1

    B_sizes = [0] * (len(B_components) + 1)
    for size in B_components:
        B_sizes[size] += 1

    edges_needed = 0
    for size in B_components:
        if A_sizes[size] == 0:
            edges_needed += 1
    return edges_needed

n, q = map(int, input().split())
uf_A = UnionFind(n)
uf_B = UnionFind(n)

edges_A = set()
edges_B = set()

for _ in range(q):
    query = input().split()
    graph = query[0]
    x, y = int(query[1]), int(query[2])

    if graph == 'A':
        if (x, y) in edges_A:
            edges_A.remove((x, y))
            edges_A.remove((y, x))
        else:
            edges_A.add((x, y))
            edges_A.add((y, x))
            uf_A.union(x, y)

    else:  # graph == 'B'
        if (x, y) in edges_B:
            edges_B.remove((x, y))
            edges_B.remove((y, x))
        else:
            edges_B.add((x, y))
            edges_B.add((y, x))
            uf_B.union(x, y)

    A_components = {}
    for i in range(1, n + 1):
        root = uf_A.find(i)
        if root not in A_components:
            A_components[root] = uf_A.size(i)

    B_components = {}
    for i in range(1, n + 1):
        root = uf_B.find(i)
        if root not in B_components:
            B_components[root] = uf_B.size(i)

    edges_needed = min_edges_to_include(A_components.values(), B_components.values())
    print(edges_needed)