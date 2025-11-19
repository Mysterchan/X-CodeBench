class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

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
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def count_edges_needed(components_a, components_b):
    needed_edges = 0
    for comp_b in components_b:
        found = False
        for comp_a in components_a:
            if set(comp_b).issubset(set(comp_a)):
                found = True
                break
        if not found:
            needed_edges += 1
    return needed_edges

n, q = map(int, input().split())
uf_a = UnionFind(n)
uf_b = UnionFind(n)

edges_a = set()
edges_b = set()

results = []

for _ in range(q):
    query = input().split()
    graph = query[0]
    x, y = int(query[1]) - 1, int(query[2]) - 1

    if graph == 'A':
        if (x, y) in edges_a or (y, x) in edges_a:
            edges_a.remove((x, y))
            edges_a.remove((y, x))
        else:
            edges_a.add((x, y))
            edges_a.add((y, x))
            uf_a.union(x, y)
    else:
        if (x, y) in edges_b or (y, x) in edges_b:
            edges_b.remove((x, y))
            edges_b.remove((y, x))
        else:
            edges_b.add((x, y))
            edges_b.add((y, x))
            uf_b.union(x, y)

    components_a = {}
    for i in range(n):
        root = uf_a.find(i)
        if root not in components_a:
            components_a[root] = []
        components_a[root].append(i)

    components_b = {}
    for i in range(n):
        root = uf_b.find(i)
        if root not in components_b:
            components_b[root] = []
        components_b[root].append(i)

    needed_edges = count_edges_needed(components_a.values(), components_b.values())
    results.append(needed_edges)

print('\n'.join(map(str, results)))