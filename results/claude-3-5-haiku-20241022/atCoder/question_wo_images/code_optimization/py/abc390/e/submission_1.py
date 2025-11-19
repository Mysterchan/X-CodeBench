N, X = map(int, input().split())

v1, v2, v3 = [], [], []
for _ in range(N):
    v, a, c = map(int, input().split())
    if v == 1:
        v1.append((a, c))
    elif v == 2:
        v2.append((a, c))
    else:
        v3.append((a, c))

def dpv(V):
    dp = [0] * (X + 1)
    for a, c in V:
        for cal in range(X, c - 1, -1):
            dp[cal] = max(dp[cal], dp[cal - c] + a)
    return dp

dp1 = dpv(v1)
dp2 = dpv(v2)
dp3 = dpv(v3)

ans = 0
for c1 in range(X + 1):
    for c2 in range(X + 1 - c1):
        c3 = X - c1 - c2
        ans = max(ans, min(dp1[c1], dp2[c2], dp3[c3]))

print(ans)