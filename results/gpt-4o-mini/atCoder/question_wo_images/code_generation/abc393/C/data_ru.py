def min_edges_to_remove(N, M, edges):
    from collections import defaultdict

    # To track the number of edges for each vertex and to check for self-loops
    edge_count = defaultdict(int)
    self_loops = 0

    for u, v in edges:
        if u == v:
            self_loops += 1
        else:
            edge_count[(min(u, v), max(u, v))] += 1

    # Count the number of edges to remove
    edges_to_remove = self_loops  # All self-loops need to be removed

    for count in edge_count.values():
        if count > 1:
            edges_to_remove += count - 1  # Remove (count - 1) edges to keep only one

    return edges_to_remove

import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M+1]]

print(min_edges_to_remove(N, M, edges))