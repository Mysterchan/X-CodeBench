import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

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

def dfs(u, parent):
    child_dp = []
    for v in G[u]:
        if v == parent:
            continue
        dfs(v, u)
        child_dp.append(dp[v])
    child_dp.sort(reverse=True)
    deg = len(G[u])
    if deg == 1:
        # Leaf node in original tree: dp[u] = 1
        dp[u] = 1
    elif deg >= 4:
        # To form alkane node with degree 4, pick top 4 children
        if len(child_dp) >= 4:
            dp[u] = 1 + sum(child_dp[:4])
        else:
            dp[u] = 0
    else:
        # For other degrees, dp[u] = 0 (can't be alkane node)
        dp[u] = 0

    global max_size
    if dp[u] >= 5:
        max_size = max(max_size, dp[u])

dfs(0, -1)

print(max_size if max_size >= 5 else -1)