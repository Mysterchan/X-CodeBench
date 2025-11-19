from collections import deque

def bfs(start, graph, n):
    distances = [-1] * (n + 1)
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == -1:  # Not visited
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    return distances

def min_moves_to_swap(N, M, S, T, edges):
    graph = [[] for _ in range(N + 1)]
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    dist_from_S = bfs(S, graph, N)
    dist_from_T = bfs(T, graph, N)
    
    if dist_from_S[T] == -1:
        return -1
    
    min_moves = float('inf')
    
    for i in range(1, N + 1):
        if i != S and i != T:
            moves = dist_from_S[i] + dist_from_T[i]
            if moves >= 0:
                min_moves = min(min_moves, moves + 2)  # +2 for the final moves to S and T
    
    return min_moves if min_moves != float('inf') else -1

# Input reading
N, M, S, T = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Output the result
print(min_moves_to_swap(N, M, S, T, edges))