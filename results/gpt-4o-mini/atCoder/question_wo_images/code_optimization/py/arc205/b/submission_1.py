n, m = map(int, input().split())
edge_set = set()

# Read edges and store in a set
for _ in range(m):
    u, v = map(int, input().split())
    edge_set.add((min(u, v), max(u, v)))

# The number of edges in a complete graph with n vertices
total_edges = n * (n - 1) // 2

# The number of edges that are initially black
initial_black_edges = len(edge_set)

# The maximum black edges we can achieve with operations
max_black_edges = total_edges - (initial_black_edges % 3)

print(max_black_edges)