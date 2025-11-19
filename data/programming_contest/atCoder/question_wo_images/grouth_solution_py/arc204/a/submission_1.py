from itertools import accumulate

MOD = 998244353
N, L, R = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sa = [0] + list(accumulate(A))
sb = [0] + list(accumulate(B))

def f(X):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N + 1):
        for j in range(N + 1):
            if i + 1 >= j and i < N and sa[i + 1] - sb[j] <= X:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= MOD
            if i >= j + 1 and j < N:
                dp[i][j + 1] += dp[i][j]
                dp[i][j + 1] %= MOD
    return dp[-1][-1]

S = sa[-1] - sb[-1]
ans = (f(R + S) - f(L - 1 + S)) % MOD
print(ans)