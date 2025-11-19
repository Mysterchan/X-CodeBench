class UnionFind():
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.edge_count = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
            return True
        return False

N, M = map(int, input().split())
edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
Q = int(input())
X = list(map(lambda x: int(x) - 1, input().split()))

uf = UnionFind(N)

# Initialize edges count
uf.edge_count = M

# This will store the graph as adjacency lists
# Initially each edge is an edge in the graph
graph = [set() for _ in range(N)]
for u, v in edges:
    graph[u].add(v)
    graph[v].add(u)

answers = []

for x in X:
    u, v = edges[x]
    root_u = uf.find(u)
    root_v = uf.find(v)
    
    if root_u != root_v:
        # Before union, count the edges connected to u and v
        edges_before = len(graph[root_u]) + len(graph[root_v])
        
        # Perform union
        if uf.union(root_u, root_v):
            root_new = uf.find(root_u)
            # Merge the two components
            graph[root_new].update(graph[root_u])
            graph[root_new].update(graph[root_v])
            graph[root_new].discard(root_u)
            graph[root_new].discard(root_v)
            
            # Update the graph sizes
            del graph[root_u]
            del graph[root_v]
            edges_after = len(graph[root_new])
            
            # Update the total edge count
            uf.edge_count -= (len(graph[root_u]) + len(graph[root_v])) - edges_after
            
    # Record the current edge count
    answers.append(uf.edge_count)

# Output the results
print('\n'.join(map(str, answers)))