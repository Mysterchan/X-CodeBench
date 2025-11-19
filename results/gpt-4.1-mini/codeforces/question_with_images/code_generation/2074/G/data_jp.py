import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # dp[i][j]: 頂点iからjまでの多角形の最大スコア
    # i < j かつ j - i >= 2 の範囲で考える
    dp = [[0]*(n) for __ in range(n)]

    # 長さ3以上の区間で三角形を作る
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            # i,j間の多角形を三角形分割する
            for k in range(i+1, j):
                val = dp[i][k] + dp[k][j] + a[i]*a[j]*a[k]
                if val > dp[i][j]:
                    dp[i][j] = val

    print(dp[0][n-1])