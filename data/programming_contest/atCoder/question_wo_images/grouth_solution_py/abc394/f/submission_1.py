N = int(input())
G = [set() for _ in range(N+1)]
edges = [0]*(N+1)
for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].add(v)
    G[v].add(u)
    edges[u] += 1
    edges[v] += 1

from collections import deque
center = [False]*(N+1)
q = deque()
dp = [1]*(N+1)
L = [[] for _ in range(N+1)]
for i in range(1, N+1):
    if edges[i] >= 4:
        center[i] = True
    elif edges[i] == 1:
        q.append(i)

ans = 0
while q:
    pos = q.popleft()
    if not G[pos]:
        if center[pos]:
            L[pos].sort(reverse=True)
            ans = max(ans, sum(L[pos][:4])+1)
        continue
    nex = G[pos].pop()
    if center[pos]:
        L[pos].sort(reverse=True)
        dp[pos] += sum(L[pos][:3])
        if center[nex]:
            L[nex].append(dp[pos])
        else:
            ans = max(ans, dp[pos]+1)
    elif center[nex]:
        L[nex].append(1)
    G[nex].remove(pos)
    edges[nex] -= 1
    if edges[nex] == 1:
        q.append(nex)
print(ans if ans != 0 else -1)