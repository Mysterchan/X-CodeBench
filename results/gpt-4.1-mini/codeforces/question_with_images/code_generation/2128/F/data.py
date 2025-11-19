import sys
import heapq

input = sys.stdin.readline

def dijkstra(n, graph, start, use_lower_bound):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cur_d, u = heapq.heappop(heap)
        if cur_d > dist[u]:
            continue
        for v, l, r in graph[u]:
            w = l if use_lower_bound else r
            nd = cur_d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    graph = [[] for __ in range(n + 1)]
    edges = []
    for __ in range(m):
        u, v, l, r = map(int, input().split())
        graph[u].append((v, l, r))
        graph[v].append((u, l, r))
        edges.append((u, v, l, r))

    # Compute shortest distances using lower bounds
    dist1_lower = dijkstra(n, graph, 1, True)
    distk_lower = dijkstra(n, graph, k, True)
    distn_lower = dijkstra(n, graph, n, True)

    # Compute shortest distances using upper bounds
    dist1_upper = dijkstra(n, graph, 1, False)
    distk_upper = dijkstra(n, graph, k, False)
    distn_upper = dijkstra(n, graph, n, False)

    # Check if for all assignments dist(1,n) == dist(1,k) + dist(k,n)
    # If for lower bounds equality holds and for upper bounds equality holds,
    # then no assignment can break the equality.
    # Otherwise, answer YES.

    # Check equality for lower bounds
    eq_lower = (dist1_lower[n] == dist1_lower[k] + distk_lower[n])
    # Check equality for upper bounds
    eq_upper = (dist1_upper[n] == dist1_upper[k] + distk_upper[n])

    # If equality holds for both extremes, answer NO, else YES
    if eq_lower and eq_upper:
        print("NO")
    else:
        print("YES")