import sys
import heapq
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

N, M, X = map(int, data[0].split())
graph = defaultdict(list)
reverse_graph = defaultdict(list)

for i in range(1, M + 1):
    u, v = map(int, data[i].split())
    graph[u].append(v)
    reverse_graph[v].append(u)

# Dijkstra's algorithm with a priority queue
def dijkstra(start, end):
    min_cost = [float('inf')] * (N + 1)
    min_cost[start] = 0
    pq = [(0, start)]  # (cost, node)

    while pq:
        cost, node = heapq.heappop(pq)

        if cost > min_cost[node]:
            continue

        # Move to adjacent nodes
        for neighbor in graph[node]:
            new_cost = cost + 1
            if new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

        # Reverse edges operation
        new_cost = cost + X
        for neighbor in reverse_graph[node]:
            if new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return min_cost[end]

result = dijkstra(1, N)
print(result)