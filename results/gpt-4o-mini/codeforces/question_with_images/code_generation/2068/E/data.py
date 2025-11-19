from collections import deque, defaultdict

def min_roads_to_porto(n, m, edges):
    graph = defaultdict(list)
    
    # Build the graph
    for s, t in edges:
        graph[s].append(t)
        graph[t].append(s)
    
    # BFS to find the shortest path from 1 to n
    def bfs(start, end):
        queue = deque([start])
        distances = {start: 0}
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in distances:
                    distances[neighbor] = distances[node] + 1
                    queue.append(neighbor)
                    if neighbor == end:
                        return distances[neighbor]
        return float('inf')
    
    # Find the shortest path from 1 to n
    shortest_path_length = bfs(1, n)
    
    # If the shortest path length is infinity, it means there's no path
    if shortest_path_length == float('inf'):
        return -1
    
    # Check if the police can block a road to make it impossible to reach Porto
    for s, t in edges:
        # Temporarily remove the edge
        graph[s].remove(t)
        graph[t].remove(s)
        
        # Check if there's still a path from 1 to n
        if bfs(1, n) == float('inf'):
            # If no path exists, police can block this edge
            return -1
        
        # Restore the edge
        graph[s].append(t)
        graph[t].append(s)
    
    # If police cannot block any edge to prevent reaching Porto
    return shortest_path_length + 1

# Read input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Get the result and print it
result = min_roads_to_porto(n, m, edges)
print(result)