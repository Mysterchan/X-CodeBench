import sys
import heapq

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
W = list(map(int, data[2:N+2]))

edges = [[] for _ in range(N + 1)]
index = N + 2

for _ in range(M):
    u = int(data[index])
    v = int(data[index + 1])
    edges[u].append(v)
    edges[v].append(u)
    index += 2

def dijkstra(start):
    fuel_cost = [float('inf')] * (N + 1)
    fuel_cost[start] = 0
    min_heap = [(0, start)]  # (current fuel cost, vertex)

    while min_heap:
        current_fuel, u = heapq.heappop(min_heap)

        if current_fuel > fuel_cost[u]:
            continue

        current_weight = W[u - 1]  # Weight at vertex u
        for v in edges[u]:
            next_fuel = current_fuel + current_weight
            if next_fuel < fuel_cost[v]:
                fuel_cost[v] = next_fuel
                heapq.heappush(min_heap, (next_fuel, v))

    return fuel_cost

result = dijkstra(1)

for i in range(1, N + 1):
    print(result[i])