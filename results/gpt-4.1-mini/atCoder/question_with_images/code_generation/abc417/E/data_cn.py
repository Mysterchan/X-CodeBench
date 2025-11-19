import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(u):
    if u == Y:
        path.append(u)
        return True
    visited[u] = True
    path.append(u)
    for v in graph[u]:
        if not visited[v]:
            if dfs(v):
                return True
    path.pop()
    return False

T = int(input())
for _ in range(T):
    N, M, X, Y = map(int, input().split())
    graph = [[] for __ in range(N+1)]
    for __ in range(M):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, N+1):
        graph[i].sort()
    visited = [False]*(N+1)
    path = []
    dfs(X)
    print(*path)