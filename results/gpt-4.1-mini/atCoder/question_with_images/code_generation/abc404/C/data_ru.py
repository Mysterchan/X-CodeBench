import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
if M != N:
    print("No")
    exit()

adj = [[] for _ in range(N+1)]
degree = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    degree[a] += 1
    degree[b] += 1

# Check all degrees == 2
for i in range(1, N+1):
    if degree[i] != 2:
        print("No")
        exit()

# Check connectivity using DFS
visited = [False]*(N+1)

def dfs(u):
    stack = [u]
    visited[u] = True
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if not visited[w]:
                visited[w] = True
                stack.append(w)

dfs(1)

if all(visited[1:]):
    print("Yes")
else:
    print("No")