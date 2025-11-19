N, L, R = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sum = [0] * (N + 1)
B_sum = [0] * (N + 1)

for i in range(N):
    A_sum[i + 1] = A_sum[i] + A[i]
    B_sum[i + 1] = B_sum[i] + B[i]

L += A_sum[N] - B_sum[N]
R += A_sum[N] - B_sum[N]

MOD = 998244353
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N + 1):
    for j in range(i + 1):
        if j + 1 <= i:
            new_val = A_sum[i] - B_sum[j + 1]
            if L <= new_val <= R:
                dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD
            dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD
        if i + 1 <= N:
            new_val = A_sum[i + 1] - B_sum[j]
            if L <= new_val <= R:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
            if new_val <= R:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD

print(dp[N][N])