import sys
import heapq

def main():
    input = sys.stdin.readline
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    rev_graph = [[] for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        rev_graph[v].append(u)

    # We consider states: (vertex, direction)
    # direction = 0 means edges as original
    # direction = 1 means edges reversed
    # Costs:
    # - Move along an edge: cost 1
    # - Reverse all edges: cost X

    # Use Dijkstra on state graph with 2*N nodes
    dist = [[float('inf')] * 2 for _ in range(N+1)]
    dist[1][0] = 0
    pq = [(0, 1, 0)]  # (cost, vertex, direction)

    while pq:
        cost, v, d = heapq.heappop(pq)
        if dist[v][d] < cost:
            continue
        if v == N:
            print(cost)
            return

        # Move along edges in current direction
        if d == 0:
            for nxt in graph[v]:
                ncost = cost + 1
                if dist[nxt][d] > ncost:
                    dist[nxt][d] = ncost
                    heapq.heappush(pq, (ncost, nxt, d))
        else:
            for nxt in rev_graph[v]:
                ncost = cost + 1
                if dist[nxt][d] > ncost:
                    dist[nxt][d] = ncost
                    heapq.heappush(pq, (ncost, nxt, d))

        # Reverse edges
        nd = 1 - d
        ncost = cost + X
        if dist[v][nd] > ncost:
            dist[v][nd] = ncost
            heapq.heappush(pq, (ncost, v, nd))

if __name__ == "__main__":
    main()