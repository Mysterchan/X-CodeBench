def find_min_weight_path(N, weights, ranges, queries):
    from collections import defaultdict, deque
    
    # Create adjacency list for the graph
    graph = defaultdict(list)
    
    # Check for intersections and build the graph
    for i in range(N):
        L_i, R_i = ranges[i]
        for j in range(i + 1, N):
            L_j, R_j = ranges[j]
            if R_i < L_j or R_j < L_i:  # No intersection
                graph[i + 1].append(j + 1)
                graph[j + 1].append(i + 1)
    
    # Function to perform BFS and find the minimum weight path
    def bfs(start, end):
        queue = deque([start])
        visited = {start: weights[start - 1]}  # Store the weight of the path
        
        while queue:
            current = queue.popleft()
            current_weight = visited[current]
            
            if current == end:
                return current_weight
            
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited[neighbor] = current_weight + weights[neighbor - 1]
                    queue.append(neighbor)
        
        return -1
    
    results = []
    for s, t in queries:
        result = bfs(s, t)
        results.append(result)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
weights = list(map(int, data[1].split()))
ranges = [tuple(map(int, line.split())) for line in data[2:N + 2]]
Q = int(data[N + 2])
queries = [tuple(map(int, line.split())) for line in data[N + 3:N + 3 + Q]]

# Get results
results = find_min_weight_path(N, weights, ranges, queries)

# Print results
for res in results:
    print(res)