def max_sweet_edges(n, edges):
    from collections import defaultdict
    
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node, parent):
        count = 0
        degree[node] = 0
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            count += dfs(neighbor, node)
            if degree[neighbor] < 2:
                count += 1
                degree[node] += 1
        
        return count

    max_edges = 0
    degree = [0] * (n + 1)

    for i in range(1, n + 1):
        if degree[i] < 2:
            degree[i] += dfs(i, -1)

    max_edges = sum(deg for deg in degree) // 2
    return max_edges

import sys
input = sys.stdin.read

data = input().strip().splitlines()
t = int(data[0])
index = 1
results = []

for _ in range(t):
    n, m = map(int, data[index].split())
    edges = [tuple(map(int, data[index + i + 1].split())) for i in range(m)]
    index += m + 1
    
    result = max_sweet_edges(n, edges)
    results.append(str(result))

print("\n".join(results))