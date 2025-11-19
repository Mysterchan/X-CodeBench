mod = 998244353

N, M = map(int, input().split())
ok = [[True] * (N + 1) for _ in range(N)]
inv = [0] * N

for i in range(M):
    P = list(map(lambda x: int(x) - 1, input().split()))
    if i == 0:
        for j in range(N):
            inv[P[j]] = j
    Q = [(P[inv[j]] - P[inv[0]]) % N for j in range(N)]

    for l in range(N):
        mn, mx = float('inf'), float('-inf')
        for r in range(l, N):
            mn = min(mn, Q[r])
            mx = max(mx, Q[r])
            ok[l][r + 1] &= r - l == mx - mn

dp1 = [[0] * (N + 1) for _ in range(N + 1)]
dp2 = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp2[i][i] = 1

for r in range(1, N + 1):
    for l in range(r - 1, 0, -1):
        if ok[l][r]:
            for m in range(l, r):
                dp1[l][r] = (dp1[l][r] + dp2[l][m] * dp2[m + 1][r]) % mod
        for m in range(l, r):
            dp2[l][r] = (dp2[l][r] + dp2[l][m] * dp1[m][r]) % mod

print(dp2[1][N])