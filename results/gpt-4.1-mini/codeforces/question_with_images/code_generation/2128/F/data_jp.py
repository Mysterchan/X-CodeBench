import sys
import heapq
input = sys.stdin.readline

INF = 10**15

def dijkstra(n, graph, start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        cd, u = heapq.heappop(hq)
        if dist[u] < cd:
            continue
        for v, w in graph[u]:
            nd = cd + w
            if dist[v] > nd:
                dist[v] = nd
                heapq.heappush(hq, (nd, v))
    return dist

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    edges = []
    graph_min = [[] for __ in range(n+1)]
    graph_max = [[] for __ in range(n+1)]
    for __ in range(m):
        u,v,l,r = map(int, input().split())
        edges.append((u,v,l,r))
        graph_min[u].append((v,l))
        graph_min[v].append((u,l))
        graph_max[u].append((v,r))
        graph_max[v].append((u,r))

    # dist_min: shortest distances with all edges at minimal weights
    dist_min_1 = dijkstra(n, graph_min, 1)
    dist_min_k = dijkstra(n, graph_min, k)
    dist_min_n = dijkstra(n, graph_min, n)

    # dist_max: shortest distances with all edges at maximal weights
    dist_max_1 = dijkstra(n, graph_max, 1)
    dist_max_k = dijkstra(n, graph_max, k)
    dist_max_n = dijkstra(n, graph_max, n)

    # Check if for all valid weight assignments, dist(1,n) == dist(1,k)+dist(k,n)
    # If minimal dist(1,n) > maximal dist(1,k)+dist(k,n), then NO
    # If maximal dist(1,n) < minimal dist(1,k)+dist(k,n), then NO
    # Otherwise, YES

    # Because dist(1,n) is monotone in weights (increasing weights increase dist),
    # and dist(1,k)+dist(k,n) is also monotone in weights,
    # the equality dist(1,n) == dist(1,k)+dist(k,n) holds for all weights iff
    # minimal dist(1,n) == minimal dist(1,k)+dist(k,n) == maximal dist(1,n) == maximal dist(1,k)+dist(k,n)

    # So if minimal dist(1,n) == minimal dist(1,k)+dist(k,n) and maximal dist(1,n) == maximal dist(1,k)+dist(k,n),
    # then equality always holds, answer NO.
    # Otherwise, answer YES.

    min_sum = dist_min_1[k] + dist_min_k[n]
    max_sum = dist_max_1[k] + dist_max_k[n]

    if dist_min_1[n] == min_sum and dist_max_1[n] == max_sum:
        print("NO")
    else:
        print("YES")