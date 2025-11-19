import sys
import heapq

input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
weights = list(map(int, data[1].split()))
graph = [[] for _ in range(N + 1)]

for i in range(2, M + 2):
    u, v = map(int, data[i].split())
    graph[u].append(v)
    graph[v].append(u)

def dijkstra(start):
    min_fuel = [float('inf')] * (N + 1)
    min_fuel[start] = 0
    pq = [(0, start)]  # (fuel, vertex)

    while pq:
        current_fuel, current_vertex = heapq.heappop(pq)

        if current_fuel > min_fuel[current_vertex]:
            continue

        current_weight = sum(weights[v - 1] for v in range(1, current_vertex + 1))

        for neighbor in graph[current_vertex]:
            fuel_cost = current_fuel + current_weight
            if fuel_cost < min_fuel[neighbor]:
                min_fuel[neighbor] = fuel_cost
                heapq.heappush(pq, (fuel_cost, neighbor))

    return min_fuel

result = dijkstra(1)

for i in range(1, N + 1):
    print(result[i])