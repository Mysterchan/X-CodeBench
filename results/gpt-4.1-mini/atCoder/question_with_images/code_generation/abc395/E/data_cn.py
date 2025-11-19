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

    # dist[node][state]: minimal cost to reach node with edge direction state
    # state=0 means original direction, state=1 means reversed direction
    INF = 1 << 60
    dist = [[INF]*2 for _ in range(N+1)]
    dist[1][0] = 0
    hq = [(0, 1, 0)]  # (cost, node, state)

    while hq:
        cost, u, s = heapq.heappop(hq)
        if dist[u][s] < cost:
            continue
        if u == N:
            print(cost)
            return
        # Move along edges in current direction
        if s == 0:
            for v in graph[u]:
                nc = cost + 1
                if dist[v][s] > nc:
                    dist[v][s] = nc
                    heapq.heappush(hq, (nc, v, s))
        else:
            for v in rev_graph[u]:
                nc = cost + 1
                if dist[v][s] > nc:
                    dist[v][s] = nc
                    heapq.heappush(hq, (nc, v, s))
        # Reverse edges direction
        ns = 1 - s
        nc = cost + X
        if dist[u][ns] > nc:
            dist[u][ns] = nc
            heapq.heappush(hq, (nc, u, ns))

if __name__ == "__main__":
    main()