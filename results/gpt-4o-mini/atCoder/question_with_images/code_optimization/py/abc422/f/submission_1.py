import heapq
import sys

input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
m = int(data[index + 1])
index += 2
w = list(map(int, data[index:index + n]))
index += n

# Create adjacency list
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    adj[u].append(v)
    adj[v].append(u)
    index += 2

# Dijkstra's algorithm
def dijkstra(start):
    inf = float('inf')
    # Distances and weights used in the priority queue
    dist = [inf] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (fuel, node)
    
    while pq:
        current_fuel, u = heapq.heappop(pq)
        
        if current_fuel > dist[u]:
            continue
        
        for v in adj[u]:
            next_fuel = current_fuel + dist[u] + w[v - 1]  # current weight + weight of next vertex
            if next_fuel < dist[v]:
                dist[v] = next_fuel
                heapq.heappush(pq, (next_fuel, v))
    
    return dist

result = dijkstra(1)
for u in range(1, n + 1):
    print(result[u])