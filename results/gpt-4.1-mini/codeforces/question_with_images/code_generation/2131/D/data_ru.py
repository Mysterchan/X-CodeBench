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
    return dist

t = int(input())
for _ in range(t):
    n = int(input())
    g = [[] for __ in range(n+1)]
    for __ in range(n-1):
        u,v = map(int,input().split())
        g[u].append(v)
        g[v].append(u)

    # 1) Найдем одну из концов диаметра (farthest from 1)
    dist1 = bfs(1, n, g)
    u = max(range(1,n+1), key=lambda x: dist1[x])

    # 2) Найдем другой конец диаметра (farthest from u)
    distu = bfs(u, n, g)
    v = max(range(1,n+1), key=lambda x: distu[x])
    diameter = distu[v]

    # Минимальный диаметр, которого можно достичь:
    # Если диаметр d:
    # - если d <= 2, то 0 операций
    # - если d > 2, то минимальное количество операций = d//2
    # Это следует из анализа операции: каждое применение операции может уменьшить диаметр примерно на 2,
    # сводя дерево к "звезде" с диаметром 2 или 1.

    if diameter <= 2:
        print(0)
    else:
        print(diameter // 2)