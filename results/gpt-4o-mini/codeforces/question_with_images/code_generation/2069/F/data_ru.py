class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
        self.size = [1] * (n + 1)

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
                self.size[root_u] += self.size[root_v]
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
                self.rank[root_u] += 1

    def get_size(self, u):
        return self.size[self.find(u)]

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, q = map(int, data[0].split())
    queries = data[1:]

    uf_a = UnionFind(n)
    uf_b = UnionFind(n)

    edges_a = set()
    edges_b = set()

    results = []

    for query in queries:
        parts = query.split()
        graph = parts[0]
        x, y = int(parts[1]), int(parts[2])

        if graph == 'A':
            if (x, y) in edges_a:
                edges_a.remove((x, y))
                edges_a.remove((y, x))
            else:
                edges_a.add((x, y))
                edges_a.add((y, x))
                uf_a.union(x, y)

        else:  # graph == 'B'
            if (x, y) in edges_b:
                edges_b.remove((x, y))
                edges_b.remove((y, x))
            else:
                edges_b.add((x, y))
                edges_b.add((y, x))
                uf_b.union(x, y)

        # Count components in A and B
        components_a = {}
        components_b = {}

        for i in range(1, n + 1):
            root_a = uf_a.find(i)
            root_b = uf_b.find(i)
            if root_a not in components_a:
                components_a[root_a] = 0
            components_a[root_a] += 1
            
            if root_b not in components_b:
                components_b[root_b] = 0
            components_b[root_b] += 1

        # Calculate the number of edges needed
        needed_edges = 0
        for root_b in components_b:
            if root_b not in components_a:
                needed_edges += 1
            else:
                needed_edges += max(0, components_b[root_b] - components_a[root_b])

        results.append(str(needed_edges))

    print("\n".join(results))

if __name__ == "__main__":
    main()