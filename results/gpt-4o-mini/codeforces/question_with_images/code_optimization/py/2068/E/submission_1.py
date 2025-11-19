import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())
roads = defaultdict(list)
for _ in range(m):
    s1, s2 = map(int, input().split())
    roads[s1].append(s2)
    roads[s2].append(s1)

# BFS to find the shortest path from 1 to n without blocking
def bfs(start, end, blocked_edge=None):
    q = deque([start])
    distance = {start: 0}
    
    while q:
        node = q.popleft()
        if node == end:
            return distance[node]
        
        for neighbor in roads[node]:
            if (blocked_edge is not None and
                    (node, neighbor) == blocked_edge or
                    (neighbor, node) == blocked_edge):
                continue
            
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                q.append(neighbor)
    
    return float('inf')

# Calculate the best path considering one edge block
def find_minimum_moves():
    initial_distance = bfs(1, n)
    
    if initial_distance == float('inf'):
        return -1

    best_distance = float('inf')
    
    for node in range(1, n + 1):
        for neighbor in roads[node]:
            # Block the edge (node, neighbor) and calculate the distance
            blocked_distance = bfs(1, n, (node, neighbor))
            best_distance = min(best_distance, blocked_distance + 1)
    
    return best_distance if best_distance != float('inf') else -1

print(find_minimum_moves())