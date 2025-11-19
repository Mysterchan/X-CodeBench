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

    # dist[v] = minimal fuel consumed to reach v
    dist = [float('inf')] * N
    dist[0] = 0  # starting at vertex 1, fuel consumed is 0

    # weight[v] = sum of W on path from 1 to v (including v)
    # We will keep track of weight to calculate edge cost
    weight = [float('inf')] * N
    weight[0] = W[0]

    # Priority queue: (fuel_consumed, vertex, current_weight)
    # We only store fuel_consumed and vertex in the queue,
    # but we need weight[v] to calculate next edge cost.
    # Since weight[v] is updated only when dist[v] is updated,
    # we can rely on weight[v] for current weight.
    pq = [(0, 0)]  # (fuel, vertex)

    while pq:
        fuel, v = heapq.heappop(pq)
        if dist[v] < fuel:
            continue
        cur_weight = weight[v]
        for nv in graph[v]:
            # cost to move from v to nv is current weight at v
            new_fuel = fuel + cur_weight
            new_weight = cur_weight + W[nv]
            if dist[nv] > new_fuel:
                dist[nv] = new_fuel
                weight[nv] = new_weight
                heapq.heappush(pq, (new_fuel, nv))

    for d in dist:
        print(d)

if __name__ == "__main__":
    main()