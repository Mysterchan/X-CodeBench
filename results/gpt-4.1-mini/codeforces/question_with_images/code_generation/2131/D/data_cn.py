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
    max_dist = dist[farthest_node]
    return farthest_node, max_dist

t = int(input())
for _ in range(t):
    n = int(input())
    g = [[] for __ in range(n+1)]
    for __ in range(n-1):
        u,v = map(int,input().split())
        g[u].append(v)
        g[v].append(u)

    # 找直徑：先從任意點(1) BFS 找最遠點 x
    x, _ = bfs(1, n, g)
    # 再從 x BFS 找最遠點 y 與距離 d (直徑長度)
    y, d = bfs(x, n, g)

    # 根據題意，最小直徑為 1 或 2
    # 操作次數 = max(0, d - 2)
    # 因為每次操作可將直徑減少 1，直到直徑 <= 2
    print(max(0, d - 2))