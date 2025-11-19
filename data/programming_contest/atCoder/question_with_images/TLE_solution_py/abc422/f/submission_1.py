import heapq

n, m = map(int, input().split())
w = list(map(int, input().split()))
assert len(w) == n
adj = {u: set() for u in range(1, n + 1)}
for i in range(m):
    u, v = map(int, input().split())
    adj[u].add(v)
    adj[v].add(u)

inf = float('inf')

def dijkstra(start):

    vnew = set()
    d = {u: {i: inf for i in range(n + 1)} for u in range(1, n + 1)}

    heap = [(0, i, start) for i in range(n + 1)]

    while len(heap) > 0:
        dui, i, u = heapq.heappop(heap)
        if (u, i) in vnew:
            continue
        vnew.add((u, i))
        d[u][i] = dui
        if i > 0:
            for v in adj[u]:
                if (v, i - 1) not in vnew:
                    heapq.heappush(heap,
                        (dui + i * w[u - 1], i - 1, v))
    return d

d = dijkstra(1)
for u in range(1, n + 1):
    print(d[u][0])