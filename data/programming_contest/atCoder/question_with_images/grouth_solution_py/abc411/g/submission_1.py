N,M=map(int,input().split())
edgec = [[0]*N for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    edgec[a][b] += 1
    edgec[b][a] += 1
mod = 998244353

dp = [[0 for _ in range(N)] for _ in range(2**N)]
ans=0
for i in range(N):
    dp[1<<i][i] = 1
for i in range(1,2**N):
    d = []
    first = -1
    for j in range(N):
        if (i>>j)&1:
            if first == -1:
                first = j
        elif first != -1:
            d.append(j)
    for j in range(N):
        for k in d:
            dp[i|(1<<k)][k] += dp[i][j]*edgec[j][k]
            dp[i|(1<<k)][k] %= mod
        ans += dp[i][j]*edgec[j][first]
        ans %= mod
ans -= M
ans *= pow(2, -1, mod)
ans %= mod
print(ans%mod)