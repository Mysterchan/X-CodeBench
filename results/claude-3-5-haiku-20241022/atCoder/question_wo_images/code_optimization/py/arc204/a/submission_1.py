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
dp_in = [[0] * (N + 1) for _ in range(N + 1)]

dp_in[0][0] = 1 if L <= 0 <= R else 0
dp[0][0] = 0 if L <= 0 <= R else 1

for i in range(N + 1):
    for j in range(N + 1):
        if i < j:
            continue
        
        curr_out = dp[i][j]
        curr_in = dp_in[i][j]
        
        if curr_out == 0 and curr_in == 0:
            continue
        
        if i + 1 <= N:
            val = A_sum[i + 1] - B_sum[j]
            if L <= val <= R:
                dp_in[i + 1][j] = (dp_in[i + 1][j] + curr_out) % MOD
            else:
                dp[i + 1][j] = (dp[i + 1][j] + curr_out) % MOD
            
            if val <= R:
                dp_in[i + 1][j] = (dp_in[i + 1][j] + curr_in) % MOD
            else:
                dp[i + 1][j] = (dp[i + 1][j] + curr_in) % MOD
        
        if j + 1 <= i:
            val = A_sum[i] - B_sum[j + 1]
            if L <= val <= R:
                dp_in[i][j + 1] = (dp_in[i][j + 1] + curr_out) % MOD
            else:
                dp[i][j + 1] = (dp[i][j + 1] + curr_out) % MOD
            
            dp_in[i][j + 1] = (dp_in[i][j + 1] + curr_in) % MOD

print(dp_in[N][N])