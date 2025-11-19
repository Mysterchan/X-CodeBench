import heapq
from collections import defaultdict

def dijkstra(graph, start, n, use_max=False):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, l, r in graph[u]:
            w = r if use_max else l
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist

def solve():
    n, m, k = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        u, v, l, r = map(int, input().split())
        graph[u].append((v, l, r))
        graph[v].append((u, l, r))

    dist_min_from_1 = dijkstra(graph, 1, n, use_max=False)
    dist_min_from_k = dijkstra(graph, k, n, use_max=False)

    if dist_min_from_1[n] < dist_min_from_1[k] + dist_min_from_k[n]:
        print("YES")
        return

    dist_max_from_1 = dijkstra(graph, 1, n, use_max=True)
    dist_max_from_k = dijkstra(graph, k, n, use_max=True)

    if dist_max_from_1[n] < dist_max_from_1[k] + dist_max_from_k[n]:
        print("YES")
        return

    print("NO")

t = int(input())
for _ in range(t):
    solve()
