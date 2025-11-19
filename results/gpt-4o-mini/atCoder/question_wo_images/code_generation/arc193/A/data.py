import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

# Read number of vertices
index = 0
N = int(data[index])
index += 1

# Read weights
weights = list(map(int, data[index].split()))
index += 1

# Read intervals
intervals = []
for _ in range(N):
    L, R = map(int, data[index].split())
    intervals.append((L, R))
    index += 1

# Read number of queries
Q = int(data[index])
index += 1

# Read queries
queries = []
for _ in range(Q):
    s, t = map(int, data[index].split())
    queries.append((s - 1, t - 1))  # Convert to 0-based index
    index += 1

# Build the graph based on the intervals
graph = [[] for _ in range(N)]

for i in range(N):
    L_i, R_i = intervals[i]
    for j in range(i + 1, N):
        L_j, R_j = intervals[j]
        if R_i < L_j or R_j < L_i:  # No intersection
            graph[i].append(j)
            graph[j].append(i)

# Function to find the minimum weight path using BFS
def min_weight_path(s, t):
    if s == t:
        return weights[s]
    
    queue = deque([s])
    visited = [False] * N
    visited[s] = True
    min_weight = [float('inf')] * N
    min_weight[s] = weights[s]
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                min_weight[neighbor] = min(min_weight[neighbor], min_weight[current] + weights[neighbor])
                queue.append(neighbor)
    
    return min_weight[t] if visited[t] else -1

# Process each query and print results
results = []
for s, t in queries:
    result = min_weight_path(s, t)
    results.append(result)

print('\n'.join(map(str, results)))