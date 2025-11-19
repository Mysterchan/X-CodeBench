import sys
import collections
input = sys.stdin.readline

def bfs(start, n, g):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = collections.deque([start])
    while q:
        u = q.popleft()
        for w in g[u]:
            if dist[w] == -1:
                dist[w] = dist[u] + 1
                q.append(w)
    farthest_node = dist.index(max(dist[1:]))
    max_dist = max(dist[1:])
    return farthest_node, max_dist

t = int(input())
for _ in range(t):
    n = int(input())
    g = [[] for __ in range(n+1)]
    for __ in range(n-1):
        u,v = map(int,input().split())
        g[u].append(v)
        g[v].append(u)

    # 木の直径を求める
    # 1. 適当な頂点から最も遠い頂点を探す
    u, _ = bfs(1, n, g)
    # 2. uから最も遠い頂点vを探し、その距離が直径
    v, diameter = bfs(u, n, g)

    # 操作回数は (diameter - 1) // 2
    # 直径が1以下なら操作不要
    ans = max(0, (diameter - 1) // 2)
    print(ans)