MOD = 998244353

H, W, T, A, B, C, D = map(int, input().split())

# dp[t][i][j] = t回の操作後に(i,j)にいる方法の数
dp = [[[0] * (W + 1) for _ in range(H + 1)] for _ in range(2)]

# 初期状態
dp[0][A][B] = 1

# 8方向の移動
directions = [
    (1, 1), (1, 0), (1, -1),
    (0, 1), (0, -1),
    (-1, 1), (-1, 0), (-1, -1)
]

# T回の操作
for t in range(T):
    curr = t % 2
    next_t = 1 - curr
    
    # 次の状態をクリア
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            dp[next_t][i][j] = 0
    
    # 現在の状態から次の状態へ遷移
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if dp[curr][i][j] == 0:
                continue
            
            count = dp[curr][i][j]
            
            # 8方向に移動
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                # 盤面内かチェック
                if 1 <= ni <= H and 1 <= nj <= W:
                    dp[next_t][ni][nj] = (dp[next_t][ni][nj] + count) % MOD

print(dp[T % 2][C][D])