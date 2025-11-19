import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, X, Y = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for __ in range(M):
        u,v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    for i in range(1, N+1):
        adj[i].sort()

    visited = [False]*(N+1)
    parent = [-1]*(N+1)
    found = False

    def dfs(u):
        nonlocal found
        if found:
            return
        visited[u] = True
        if u == Y:
            found = True
            return
        for w in adj[u]:
            if not visited[w]:
                parent[w] = u
                dfs(w)
                if found:
                    return

    dfs(X)

    path = []
    cur = Y
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    print(*path)