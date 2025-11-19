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

    # dist[v] = (min fuel cost to reach v, weight at v)
    # We want to minimize fuel cost.
    # When moving from u to v:
    # fuel cost += weight[u]
    # weight[v] = weight[u] + W[v]
    # Start at node 0 with fuel=0, weight=W[0]

    INF = 1 << 60
    dist = [INF] * N
    weight = [INF] * N
    dist[0] = 0
    weight[0] = W[0]

    # Priority queue: (fuel_cost, node, weight_at_node)
    # We only store fuel_cost and node in heap, weight_at_node is tracked separately.
    # But since weight_at_node affects cost of next edges, we must track it.
    # To avoid complexity, store (fuel_cost, node, weight_at_node) in heap.
    hq = [(0, 0, W[0])]

    while hq:
        cost, u, w_u = heapq.heappop(hq)
        if dist[u] < cost:
            continue
        if dist[u] == cost and weight[u] < w_u:
            continue
        for v in graph[u]:
            # cost to go from u to v
            new_cost = cost + w_u
            new_weight = w_u + W[v]
            # Update if better cost or same cost but smaller weight (to allow better future edges)
            if new_cost < dist[v] or (new_cost == dist[v] and new_weight < weight[v]):
                dist[v] = new_cost
                weight[v] = new_weight
                heapq.heappush(hq, (new_cost, v, new_weight))

    # Output results
    # For node 1 (index 0), cost is 0 as per problem statement
    for i in range(N):
        if i == 0:
            print(0)
        else:
            print(dist[i])

if __name__ == "__main__":
    main()