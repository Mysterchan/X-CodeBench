import sys
import heapq

def dijkstra(N, graph, weights):
    fuel_consumed = [float('inf')] * (N + 1)
    fuel_consumed[1] = 0
    min_heap = [(0, 1)]  # (fuel consumed, vertex)

    while min_heap:
        current_fuel, current_vertex = heapq.heappop(min_heap)

        if current_fuel > fuel_consumed[current_vertex]:
            continue

        current_weight = weights[current_vertex - 1]

        for neighbor in graph[current_vertex]:
            new_fuel = current_fuel + current_weight
            if new_fuel < fuel_consumed[neighbor]:
                fuel_consumed[neighbor] = new_fuel
                heapq.heappush(min_heap, (new_fuel, neighbor))

    return fuel_consumed[1:]

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    N, M = map(int, data[0].split())
    weights = list(map(int, data[1].split()))
    
    graph = [[] for _ in range(N + 1)]
    
    for i in range(2, 2 + M):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)

    result = dijkstra(N, graph, weights)
    
    for fuel in result:
        print(fuel)

if __name__ == "__main__":
    main()