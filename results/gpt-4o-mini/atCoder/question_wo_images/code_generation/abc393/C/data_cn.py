def min_edges_to_remove(n, m, edges):
    from collections import defaultdict

    # Dictionary to count occurrences of each edge
    edge_count = defaultdict(int)
    # Set to track self-loops
    self_loops = 0

    for u, v in edges:
        if u == v:
            self_loops += 1
        else:
            # Store edges in a sorted manner to avoid direction issues
            edge = tuple(sorted((u, v)))
            edge_count[edge] += 1

    # Count the number of edges to remove
    edges_to_remove = self_loops  # Start with self-loops
    for count in edge_count.values():
        if count > 1:
            edges_to_remove += count - 1  # Remove duplicates

    return edges_to_remove

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Get the result and print it
result = min_edges_to_remove(n, m, edges)
print(result)