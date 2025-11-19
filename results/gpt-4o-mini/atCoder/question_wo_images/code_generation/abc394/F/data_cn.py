def is_alkane_subgraph(n, edges):
    from collections import defaultdict
    
    if n < 5:  # A tree cannot have a valid alkane subgraph if it has less than 5 vertices
        return -1

    graph = defaultdict(list)
    degree = [0] * (n + 1)

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1

    # We need at least one vertex with degree 4
    if all(d not in (1, 4) for d in degree[1:]) or not any(d == 4 for d in degree[1:]):
        return -1

    visited = [False] * (n + 1)
    max_size = 0

    def dfs(node):
        stack = [node]
        size = 0
        found_four = False
        
        while stack:
            u = stack.pop()
            if visited[u]:
                continue
            visited[u] = True
            size += 1
            
            if degree[u] == 4:
                found_four = True
            
            for v in graph[u]:
                if not visited[v] and degree[v] in (1, 4):
                    stack.append(v)

        return size if found_four else 0

    for i in range(1, n + 1):
        if not visited[i] and degree[i] in (1, 4):
            size_of_subgraph = dfs(i)
            max_size = max(max_size, size_of_subgraph)

    return max_size if max_size > 0 else -1


import sys
input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
edges = [tuple(map(int, line.split())) for line in data[1:n]]

result = is_alkane_subgraph(n, edges)
print(result)