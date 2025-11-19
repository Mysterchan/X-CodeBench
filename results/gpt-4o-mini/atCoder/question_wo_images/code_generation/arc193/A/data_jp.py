def find_min_weight_path(N, weights, ranges, queries):
    from collections import defaultdict, deque

    # Create the graph
    graph = defaultdict(list)

    # Check for overlapping ranges and build the graph
    for i in range(N):
        for j in range(i + 1, N):
            if not (ranges[i][1] < ranges[j][0] or ranges[j][1] < ranges[i][0]):
                graph[i + 1].append(j + 1)
                graph[j + 1].append(i + 1)

    # Function to perform BFS and find the minimum weight path
    def bfs(start, end):
        queue = deque([start])
        visited = {start}
        total_weight = {start: weights[start - 1]}
        
        while queue:
            current = queue.popleft()
            if current == end:
                return total_weight[current]
            
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    total_weight[neighbor] = total_weight[current] + weights[neighbor - 1]
                    queue.append(neighbor)
        
        return -1

    results = []
    for s, t in queries:
        result = bfs(s, t)
        results.append(result)

    return results

# Input reading
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

# Output results
for result in results:
    print(result)