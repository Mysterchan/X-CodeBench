from collections import deque, defaultdict
import sys

input = sys.stdin.read
data = input().splitlines()

# Read N, M, S, T
N, M, S, T = map(int, data[0].split())
S -= 1  # Convert to 0-indexed
T -= 1  # Convert to 0-indexed

# Build the graph
graph = defaultdict(list)
for i in range(1, M + 1):
    u, v = map(int, data[i].split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

# BFS to find the shortest paths from S and T
def bfs(start):
    distances = [-1] * N
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == -1:  # Not visited
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    return distances

dist_from_S = bfs(S)
dist_from_T = bfs(T)

# Check if we can reach the goal
if dist_from_S[T] == -1 or dist_from_T[S] == -1:
    print(-1)
    sys.exit()

# Calculate the minimum moves
min_moves = float('inf')
for i in range(N):
    if i != S and i != T:
        moves = max(dist_from_S[i], dist_from_T[i]) + 1
        min_moves = min(min_moves, moves)

print(min_moves)