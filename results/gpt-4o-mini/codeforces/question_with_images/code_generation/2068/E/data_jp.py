from collections import deque, defaultdict

def min_edges_to_portugal(n, m, roads):
    graph = defaultdict(list)
    
    for s, t in roads:
        graph[s].append(t)
        graph[t].append(s)

    def bfs(start, end):
        queue = deque([start])
        visited = {start: 0}
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited[neighbor] = visited[node] + 1
                    queue.append(neighbor)
                    if neighbor == end:
                        return visited[neighbor]
        return float('inf')

    shortest_path_length = bfs(1, n)
    
    if shortest_path_length == float('inf'):
        return -1

    # Check if there is a critical edge
    critical_edges = 0
    for s, t in roads:
        # Temporarily remove the edge
        graph[s].remove(t)
        graph[t].remove(s)
        
        # Check if there's still a path from 1 to n
        if bfs(1, n) > shortest_path_length:
            critical_edges += 1
        
        # Restore the edge
        graph[s].append(t)
        graph[t].append(s)

    if critical_edges == 0:
        return -1
    
    return shortest_path_length + critical_edges

# Input reading
n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(min_edges_to_portugal(n, m, roads))