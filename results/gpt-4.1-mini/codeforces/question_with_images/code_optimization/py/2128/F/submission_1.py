import sys
import heapq

INF = 10 ** 18

def dijkstra(n, adj, source, weight):
    dist = [INF] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, eid in adj[u]:
            nd = d + weight(eid)
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

def solve_one(n, m, k, edges):
    # Build adjacency with edge indices
    adj = [[] for _ in range(n)]
    for i, (u, v, l, r) in enumerate(edges):
        u -= 1
        v -= 1
        adj[u].append((v, i))
        adj[v].append((u, i))

    # Weight functions for lower and upper bounds
    def w_lower(eid):
        return edges[eid][2]

    def w_upper(eid):
        return edges[eid][3]

    # Distances with all edges at lower bound
    dist1 = dijkstra(n, adj, 0, w_lower)
    distk = dijkstra(n, adj, k - 1, w_lower)

    dist1n = dist1[n - 1]
    dist1k = dist1[k - 1]
    distkn = distk[n - 1]

    # If no path exists at lower bounds, answer NO
    if dist1n == INF or dist1k == INF or distkn == INF:
        return False

    # Check if equality holds at lower bounds
    if dist1n != dist1k + distkn:
        # Already inequality, answer YES
        return True

    # Distances with all edges at upper bound
    dist1u = dijkstra(n, adj, 0, w_upper)
    distku = dijkstra(n, adj, k - 1, w_upper)

    dist1n_u = dist1u[n - 1]
    dist1k_u = dist1u[k - 1]
    distkn_u = distku[n - 1]

    # If no path exists at upper bounds, answer NO
    if dist1n_u == INF or dist1k_u == INF or distkn_u == INF:
        return False

    # If equality holds at upper bounds and lower bounds, no way to break equality
    if dist1n_u == dist1k_u + distkn_u:
        return False

    # Otherwise, since distances are continuous in weights, 
    # and equality holds at lower bounds but not at upper bounds,
    # there exists an assignment breaking equality
    return True

def solve():
    input = sys.stdin.readline
    t = int(input())
    out = []
    for _ in range(t):
        n, m, k = map(int, input().split())
        edges = [tuple(map(int, input().split())) for __ in range(m)]
        out.append("YES" if solve_one(n, m, k, edges) else "NO")
    print("\n".join(out))

if __name__ == "__main__":
    solve()