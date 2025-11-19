from collections import deque, defaultdict
import sys
import heapq

input = sys.stdin.read
data = input().splitlines()

# Read N, M, X
N, M, X = map(int, data[0].split())

# Build the graph
graph = defaultdict(list)
for i in range(1, M + 1):
    u, v = map(int, data[i].split())
    graph[u].append(v)

# Dijkstra's algorithm to find the minimum cost
def dijkstra(start, end):
    # Priority queue for the minimum cost
    pq = [(0, start)]  # (cost, vertex)
    min_cost = {i: float('inf') for i in range(1, N + 1)}
    min_cost[start] = 0

    while pq:
        current_cost, current_vertex = heapq.heappop(pq)

        if current_cost > min_cost[current_vertex]:
            continue

        # Move along directed edges
        for neighbor in graph[current_vertex]:
            new_cost = current_cost + 1
            if new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

        # Reverse the edges
        for neighbor in range(1, N + 1):
            if current_vertex in graph[neighbor]:  # If there's a reverse edge
                new_cost = current_cost + X
                if new_cost < min_cost[current_vertex]:
                    min_cost[current_vertex] = new_cost
                    heapq.heappush(pq, (new_cost, current_vertex))

    return min_cost[end]

# Get the minimum cost to reach vertex N from vertex 1
result = dijkstra(1, N)
print(result)