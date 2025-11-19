import sys
from collections import deque

input = sys.stdin.readline

def bfs(X, Y):
    queue = deque([X])
    parent = {X: None}
    
    while queue:
        node = queue.popleft()
        
        if node == Y:
            break
        
        for neighbor in graph[node]:
            if neighbor not in parent:  # Only visit unvisited nodes
                parent[neighbor] = node
                queue.append(neighbor)

    # Reconstruct the path from Y to X
    path = []
    curr = Y
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    
    return path[::-1]  # Reverse to get from X to Y

for _ in range(int(input())):
    N, M, X, Y = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for neighbors in graph:
        neighbors.sort()

    result_path = bfs(X, Y)
    print(*result_path)