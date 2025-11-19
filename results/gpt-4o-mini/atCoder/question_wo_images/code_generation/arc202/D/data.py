def king_moves(H, W, T, A, B, C, D):
    MOD = 998244353

    # Adjust to zero-indexed
    A -= 1
    B -= 1
    C -= 1
    D -= 1

    dp = [[[0] * W for _ in range(H)] for _ in range(T + 1)]
    dp[0][A][B] = 1

    moves = [(1, 1), (1, 0), (1, -1),
             (0, 1),         (0, -1),
             (-1, 1), (-1, 0), (-1, -1)]

    for t in range(T):
        for x in range(H):
            for y in range(W):
                if dp[t][x][y] > 0:
                    for dx, dy in moves:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < H and 0 <= ny < W:
                            dp[t + 1][nx][ny] = (dp[t + 1][nx][ny] + dp[t][x][y]) % MOD

    return dp[T][C][D]

# Input read
H, W, T, A, B, C, D = map(int, input().split())
print(king_moves(H, W, T, A, B, C, D))