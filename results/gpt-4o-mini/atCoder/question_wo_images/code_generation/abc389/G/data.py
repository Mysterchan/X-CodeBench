def count_graphs(N, P):
    from itertools import combinations
    
    if N < 2 or N > 30 or P < 10**8 or P > 10**9 or N % 2 != 0:
        return []

    # Helper function to check if a graph has a balanced bipartition based on distances
    def has_balanced_distances(adj):
        visited = [-1] * N
        queue = [0]  # Start from vertex 1 (index 0)
        visited[0] = 0  # Distance from vertex 1 is 0

        while queue:
            v = queue.pop(0)
            current_distance = visited[v]
            for u in range(N):
                if adj[v][u] and visited[u] == -1:  # If there is an edge and u is unvisited
                    visited[u] = current_distance + 1
                    queue.append(u)

        even_count = sum(1 for d in visited if d % 2 == 0)
        odd_count = N - even_count
        return even_count == odd_count

    result = []
    max_edges = (N * (N - 1)) // 2

    for M in range(N - 1, max_edges + 1):
        edges = list(combinations(range(N), 2))
        valid_graph_count = 0

        for edge_set in combinations(edges, M):
            # Create adjacency matrix
            adj = [[0] * N for _ in range(N)]
            for u, v in edge_set:
                adj[u][v] = adj[v][u] = 1
            
            # Check if the graph is connected and has balanced distances
            if has_balanced_distances(adj):
                valid_graph_count += 1

        result.append(valid_graph_count % P)

    return result


# Input reading
import sys
input = sys.stdin.read
data = input().strip().split()
N = int(data[0])
P = int(data[1])

# Calculate results
results = count_graphs(N, P)

# Output results
print(" ".join(map(str, results)))