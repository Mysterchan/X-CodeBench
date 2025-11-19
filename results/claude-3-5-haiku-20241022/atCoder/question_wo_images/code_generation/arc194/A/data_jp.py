N = int(input())
A = list(map(int, input().split()))

# dp[i][j] = i番目まで処理して、スタックのサイズがjのときの最大和
# jは0からNまで可能
INF = float('-inf')
dp = [[INF] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(N + 1):
        if dp[i][j] == INF:
            continue
        
        # 操作1: A[i]を追加
        if j + 1 <= N:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + A[i])
        
        # 操作2: 末尾を削除（j > 0のとき）
        if j > 0:
            dp[i + 1][j - 1] = max(dp[i + 1][j - 1], dp[i][j])

# 最大値を求める
ans = INF
for j in range(N + 1):
    ans = max(ans, dp[N][j])

print(ans)