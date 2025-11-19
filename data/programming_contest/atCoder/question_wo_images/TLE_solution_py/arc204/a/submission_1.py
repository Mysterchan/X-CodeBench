N, L, R = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
def prefix_sum(A):
  ret = [0] * (len(A) + 1)
  for i in range(len(A)):
    ret[i + 1] = ret[i] + A[i]
  return ret
A_sum = prefix_sum(A)
B_sum = prefix_sum(B)
L += A_sum[N] - B_sum[N]
R += A_sum[N] - B_sum[N]

MOD = 998244353
dp = [[[0, 0] for i in range(N + 1)] for j in range(N + 1)]
dp[0][0] = [0, 1] if L <= 0 <= R else [1, 0]
for i in range(N + 1):
  for j in range(N + 1):
    dp[i][j][0] %= MOD
    dp[i][j][1] %= MOD
    if i < j: continue

    if i + 1 <= N:
      dp[i + 1][j][1 if L <= A_sum[i + 1] - B_sum[j] <= R else 0] += dp[i][j][0]
      if A_sum[i + 1] - B_sum[j] <= R:
        dp[i + 1][j][1] += dp[i][j][1]
    if j + 1 <= i:
      dp[i][j + 1][1 if L <= A_sum[i] - B_sum[j + 1] <= R else 0] += dp[i][j][0]
      dp[i][j + 1][1] += dp[i][j][1]
print(dp[N][N][1])