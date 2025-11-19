import sys
import heapq

input = sys.stdin.readline

n, m, X = map(int, input().split())
graph = [[] for _ in range(n)]
rev_graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    rev_graph[v].append(u)

INF = 1 << 60
dist = [[INF, INF] for _ in range(n)]
dist[0][0] = 0
hq = [(0, 0, 0)]  # (cost, node, parity)

while hq:
    cost, node, parity = heapq.heappop(hq)
    if dist[node][parity] < cost:
        continue
    # Try reversing edges
    nparity = parity ^ 1
    rev_cost = cost + X
    if dist[node][nparity] > rev_cost:
        dist[node][nparity] = rev_cost
        heapq.heappush(hq, (rev_cost, node, nparity))
    # Move along edges according to parity
    edges = rev_graph[node] if parity else graph[node]
    for nxt in edges:
        ncost = cost + 1
        if dist[nxt][parity] > ncost:
            dist[nxt][parity] = ncost
            heapq.heappush(hq, (ncost, nxt, parity))

ans = min(dist[n-1])
print(ans if ans != INF else -1)