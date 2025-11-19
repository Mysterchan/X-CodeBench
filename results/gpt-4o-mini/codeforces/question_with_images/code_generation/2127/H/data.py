def max_candy_edges(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, edges = case
        # Create an adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Use a greedy approach to select edges that maintain the candy property
        degree = [0] * (n + 1)
        selected_edges = 0
        
        # Function to try to add an edge without violating the degree constraint
        def add_edge(u, v):
            nonlocal selected_edges
            if degree[u] < 2 and degree[v] < 2:
                degree[u] += 1
                degree[v] += 1
                selected_edges += 1
        
        # Attempt to add edges while respecting the degrees
        for u in range(1, n + 1):
            for v in graph[u]:
                if u < v:  # Ensure each edge is considered only once
                    add_edge(u, v)
        
        results.append(selected_edges)
    
    return results


# Input parsing
import sys
input = sys.stdin.read
data = input().splitlines()
t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n, m = map(int, data[index].split())
    edges = []
    for j in range(m):
        u, v = map(int, data[index + 1 + j].split())
        edges.append((u, v))
    test_cases.append((n, m, edges))
    index += 1 + m

# Solve the test cases
results = max_candy_edges(t, test_cases)

# Output the results
for result in results:
    print(result)