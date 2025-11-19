def min_edges_to_remove(N, M, edges):
    from collections import defaultdict

    # Dictionary to count occurrences of each edge
    edge_count = defaultdict(int)
    self_loops = 0

    for u, v in edges:
        if u == v:
            self_loops += 1
        else:
            # Store edges in a sorted manner to avoid direction issues
            edge = (min(u, v), max(u, v))
            edge_count[edge] += 1

    # Count the number of edges to remove
    multi_edges = sum(count - 1 for count in edge_count.values() if count > 1)
    
    # Total edges to remove is the sum of self-loops and multi-edges
    return self_loops + multi_edges

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M+1]]

# Get the result and print it
result = min_edges_to_remove(N, M, edges)
print(result)