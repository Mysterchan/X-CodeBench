import sys
import heapq

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    # dist[v] = minimal fuel to reach v
    dist = [float('inf')] * N
    dist[0] = 0  # starting at vertex 1, fuel cost 0

    # weight[v] = Takahashi's weight after visiting v
    # weight after visiting v = sum of W on path from 1 to v
    # We will store weight[v] as we relax edges
    weight = [float('inf')] * N
    weight[0] = W[0]

    # Priority queue: (fuel_cost, vertex)
    # We store dist[v] as fuel_cost
    # When we relax edges, cost to go from u to v:
    # fuel_cost_new = dist[u] + weight[u]
    # weight_new = weight[u] + W[v]
    pq = [(0, 0)]  # start from vertex 0 with fuel 0

    while pq:
        cur_fuel, u = heapq.heappop(pq)
        if dist[u] < cur_fuel:
            continue
        for v in graph[u]:
            # cost to move from u to v:
            # fuel cost = current fuel + weight[u]
            new_fuel = dist[u] + weight[u]
            new_weight = weight[u] + W[v]
            if new_fuel < dist[v] or (new_fuel == dist[v] and new_weight < weight[v]):
                dist[v] = new_fuel
                weight[v] = new_weight
                heapq.heappush(pq, (new_fuel, v))

    for d in dist:
        print(d)

if __name__ == "__main__":
    main()