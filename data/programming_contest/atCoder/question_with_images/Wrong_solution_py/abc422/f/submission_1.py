import sys
from collections import defaultdict
from math import inf
import heapq
def solve():
    n, m = map(int, sys.stdin.readline().split())
    w = [0] + list(map(int, sys.stdin.readline().split()))
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges[u].append(v)
        edges[v].append(u)
    dis = [dict() for _ in range(n+1)]
    dis[1][w[1]] = 0
    hp = [(0, w[1], 1)]
    while hp:
        val, weight, u = heapq.heappop(hp)
        for v in edges[u]:
            nw = weight + w[v]
            nval = val + weight

            if any(old_w <= nw or old_val <= nval for old_w, old_val in dis[v].items()):
                continue
            dis[v][nw] = nval
            heapq.heappush(hp, (nval, nw, v))
    for i in range(1, n+1):
        print(min(dis[i].values()))

solve()