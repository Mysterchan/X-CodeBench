from collections import deque, defaultdict

def min_roads_to_porto(n, m, edges):
    graph = defaultdict(list)
    
    for s, t in edges:
        graph[s].append(t)
        graph[t].append(s)

    def bfs(start, blocked_edge=None):
        visited = [False] * (n + 1)
        queue = deque([(start, 0)])  # (current_node, current_distance)
        visited[start] = True
        min_distance = float('inf')

        while queue:
            node, distance = queue.popleft()
            if node == n:
                min_distance = min(min_distance, distance)
                continue
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if blocked_edge and (node, neighbor) == blocked_edge:
                        continue
                    visited[neighbor] = True
                    queue.append((neighbor, distance + 1))
        
        return min_distance

    # First, find the shortest path without any block
    shortest_path = bfs(1)

    # If the shortest path is infinite, return -1
    if shortest_path == float('inf'):
        return -1

    # Now, check for each edge if blocking it increases the path length
    max_distance = shortest_path

    for s, t in edges:
        blocked_edge = (s, t)
        new_distance = bfs(1, blocked_edge)
        if new_distance != float('inf'):
            max_distance = max(max_distance, new_distance)

    return max_distance

# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Get the result
result = min_roads_to_porto(n, m, edges)

# Print the result
print(result)