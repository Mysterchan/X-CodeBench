import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    N, M, X, Y = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, N + 1):
        graph[i].sort()

    dist = [-1] * (N + 1)
    parent = [-1] * (N + 1)
    dist[X] = 0
    q = deque([X])

    while q:
        u = q.popleft()
        if u == Y:
            break
        for w in graph[u]:
            if dist[w] == -1:
                dist[w] = dist[u] + 1
                parent[w] = u
                q.append(w)

    path = []
    cur = Y
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    print(*path[::-1])