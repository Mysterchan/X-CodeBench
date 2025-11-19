import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
if M != N:
    print("No")
    exit()

adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# 每個頂點度數必須是2
for i in range(1, N+1):
    if len(adj[i]) != 2:
        print("No")
        exit()

visited = [False]*(N+1)

def dfs(u, p):
    visited[u] = True
    for w in adj[u]:
        if w == p:
            continue
        if visited[w]:
            continue
        dfs(w, u)

dfs(1, -1)

if all(visited[1:]):
    print("Yes")
else:
    print("No")