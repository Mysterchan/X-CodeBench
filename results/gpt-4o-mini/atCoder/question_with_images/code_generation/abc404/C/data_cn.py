def is_cyclic_graph(n, m, edges):
    if m != n:
        return "No"
    
    from collections import defaultdict
    
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    for node in range(1, n + 1):
        if len(graph[node]) != 2:
            return "No"
    
    return "Yes"

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Output result
print(is_cyclic_graph(n, m, edges))