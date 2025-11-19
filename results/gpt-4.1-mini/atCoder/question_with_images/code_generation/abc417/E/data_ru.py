import sys
import collections
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, X, Y = map(int, input().split())
    adj = [[] for __ in range(N+1)]
    for __ in range(M):
        u,v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    for i in range(1, N+1):
        adj[i].sort()

    # BFS with lex order: at each step, we process neighbors in ascending order,
    # and keep track of parent to reconstruct path.
    # Since graph is connected and simple, BFS shortest path is minimal length.
    # Among shortest paths, BFS with neighbors sorted ascending gives lex smallest path.

    visited = [False]*(N+1)
    parent = [0]*(N+1)
    queue = collections.deque()
    queue.append(X)
    visited[X] = True

    while queue:
        u = queue.popleft()
        if u == Y:
            break
        for w in adj[u]:
            if not visited[w]:
                visited[w] = True
                parent[w] = u
                queue.append(w)

    # Reconstruct path from Y to X
    path = []
    cur = Y
    while cur != 0:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    print(*path)