import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
if M != N:
    print("No")
    exit()

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

def dfs(u, p):
    visited[u] = True
    for v in graph[u]:
        if v == p:
            continue
        if visited[v]:
            continue
        dfs(v, u)

# すべての頂点の次数が2であることを確認
for i in range(1, N+1):
    if len(graph[i]) != 2:
        print("No")
        exit()

# 連結性の確認
dfs(1, -1)
if all(visited[1:]):
    print("Yes")
else:
    print("No")