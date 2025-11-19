def count_valid_graphs(N, P):
    from itertools import combinations
    
    def is_valid_graph(edges):
        # Create adjacency list
        graph = [[] for _ in range(N)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # BFS to determine distances from vertex 0 (1 in 1-based is 0 in 0-based)
        dist = [-1] * N
        dist[0] = 0
        queue = [0]
        while queue:
            n = queue.pop(0)
            for neighbor in graph[n]:
                if dist[neighbor] == -1:  # Not visited
                    dist[neighbor] = dist[n] + 1
                    queue.append(neighbor)

        even_count = sum(1 for d in dist if d % 2 == 0 and d != -1)
        odd_count = sum(1 for d in dist if d % 2 == 1)
        
        return even_count == odd_count

    results = []
    for M in range(N-1, (N * (N - 1)) // 2 + 1):
        count = 0
        # Edge generation
        for edges in combinations(range(N), 2):
            if len(edges) == M:
                if is_valid_graph(edges):
                    count += 1
        
        results.append(count % P)

    return results

# Read input
N, P = map(int, input().split())
results = count_valid_graphs(N, P)

# Output the results
print(' '.join(map(str, results)))