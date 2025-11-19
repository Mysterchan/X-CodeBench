import sys
sys.setrecursionlimit(10**7)

def dfs(u, parent):
    children_dp = []
    for v in G[u]:
        if v == parent:
            continue
        dp_v = dfs(v, u)
        children_dp.append(dp_v)

    if not children_dp:
        dp[u] = 1
        return dp[u]

    children_dp.sort(reverse=True)
    if len(children_dp) >= 3:
        dp[u] = 1 + sum(children_dp[:3])
    else:
        dp[u] = 1
    return dp[u]

n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dp = [0]*n
max_size = 0

for root in range(n):
    dfs(root, -1)

    deg = len(G[root])
    if deg == 1:
        for v in G[root]:
            max_size = max(max_size, dp[v] + 1)
    elif deg >= 4:
        child_dp = []
        for v in G[root]:
            child_dp.append(dp[v])
        child_dp.sort(reverse=True)
        max_size = max(max_size, 1 + sum(child_dp[:4]))

if max_size < 5:
    print(-1)
else:
    print(max_size)