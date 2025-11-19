mod = 998244353

N, M = map(int, input().split())
ok = [[1] * (N + 1) for _ in range(N)]
for i in range(M):
    P = list(map(lambda x: int(x) - 1, input().split()))
    if i == 0:
        inv = [0] * N
        for j, p in enumerate(P):
            inv[p] = j
    Q = [(P[inv[j]] - P[inv[0]]) % N for j in range(N)]

    pos = Q
    for l in range(N):
        mn, mx = N, -1
        for r in range(l, N):
            mn = min(mn, pos[r])
            mx = max(mx, pos[r])
            ok[l][r + 1] &= r - l == mx - mn

dp1 = [[0] * (N + 1) for i in range(N + 1)]
dp2 = [[int(i == j) for j in range(N + 1)] for i in range(N + 1)]
for r in range(N + 1):
    for l in range(r - 1, 0, -1):
        if ok[l][r]:
            for m in range(l, r):
                dp1[l][r] = (dp1[l][r] + dp2[l][m] * dp2[m + 1][r]) % mod
        for m in range(l, r):
            dp2[l][r] = (dp2[l][r] + dp2[l][m] * dp1[m][r]) % mod

print(dp2[1][N])