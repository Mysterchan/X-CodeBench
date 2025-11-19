mod = 998244353

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ok = [[1] * (N + 1) for _ in range(N)]

for _ in range(M):
    P = list(map(lambda x: int(x) - 1, input().split()))
    inv = [0] * N
    for j, p in enumerate(P):
        inv[p] = j
    base = P[inv[0]]
    Q = [(P[inv[j]] - base) % N for j in range(N)]

    pos = Q
    for l in range(N):
        mn = pos[l]
        mx = pos[l]
        for r in range(l, N):
            if pos[r] < mn:
                mn = pos[r]
            elif pos[r] > mx:
                mx = pos[r]
            if r - l != mx - mn:
                ok[l][r + 1] = 0

dp1 = [[0] * (N + 1) for _ in range(N + 1)]
dp2 = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dp2[i][i] = 1

for length in range(2, N + 1):
    for l in range(1, N - length + 2):
        r = l + length - 1
        if ok[l - 1][r]:
            s = 0
            for m in range(l, r + 1):
                s += dp2[l][m - 1] * dp2[m][r]
            dp1[l][r] = s % mod
        s = 0
        for m in range(l, r):
            s += dp2[l][m] * dp1[m + 1][r]
        dp2[l][r] = s % mod

print(dp2[1][N])