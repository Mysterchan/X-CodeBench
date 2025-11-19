from collections import deque, defaultdict

def bfs(graph, start, n):
    distances = [-1] * (n + 1)
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    return distances

def min_roads_to_porto(n, m, edges):
    graph = defaultdict(list)
    
    for s, t in edges:
        graph[s].append(t)
        graph[t].append(s)
    
    # BFS from Lisbon (1)
    dist_from_start = bfs(graph, 1, n)
    # BFS from Porto (n)
    dist_from_end = bfs(graph, n, n)
    
    min_roads = dist_from_start[n]
    
    for u in range(1, n + 1):
        for v in graph[u]:
            if dist_from_start[u] + 1 + dist_from_end[v] == min_roads:
                # If we block edge u-v, calculate the new distance
                new_distance = dist_from_start[u] + 1 + dist_from_end[v]
                if new_distance < min_roads:
                    min_roads = new_distance
    
    return min_roads if min_roads != -1 else -1

# Input reading
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(min_roads_to_porto(n, m, edges))