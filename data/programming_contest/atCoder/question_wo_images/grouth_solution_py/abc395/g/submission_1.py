INF = 1 << 60

N, K = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]

ans = [[0] * N for _ in range(N)]
dp = [[INF] * N for _ in range(1 << K)]
dp[0] = [0] * N

for i in range(K):
    dp[1 << i][i] = 0

for i in range(1, 1 << K):
    bi = i
    while True:
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[bi][j] + dp[i ^ bi][j])
        if bi == 0:
            break
        bi = (bi - 1) & i

    used = [False] * N
    for _ in range(N):
        mi = (INF, -1)
        for v in range(N):
            if not used[v]:
                mi = min(mi, (dp[i][v], v))
        _, v = mi
        used[v] = True
        for u in range(N):
            dp[i][u] = min(dp[i][u], dp[i][v] + C[v][u])

for s in range(K, N):
    ndp = [[INF] * N for _ in range(1 << K)]
    ndp[0][s] = 0

    for i in range(1 << K):
        bi = i
        while True:
            for j in range(N):
                ndp[i][j] = min(ndp[i][j], ndp[bi][j] + dp[i ^ bi][j])
            if bi == 0:
                break
            bi = (bi - 1) & i

        used = [False] * N
        for _ in range(N):
            mi = (INF, -1)
            for v in range(N):
                if not used[v]:
                    mi = min(mi, (ndp[i][v], v))
            _, v = mi
            used[v] = True
            for u in range(N):
                ndp[i][u] = min(ndp[i][u], ndp[i][v] + C[v][u])

    ans[s] = ndp[-1][:]

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    print(ans[s - 1][t - 1])