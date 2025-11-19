def count_king_moves(H, W, T, A, B, C, D):
    MOD = 998244353
    
    # Shift moves for the king, covering all 8 possible directions
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # Create a DP table
    # dp[step][x][y] = number of ways to reach (x, y) at `step` moves
    dp = [[[0] * (W + 1) for _ in range(H + 1)] for _ in range(2)]
    
    # Initial position
    dp[0][A][B] = 1
    
    # Iterate through each step
    for step in range(1, T + 1):
        current = step % 2
        previous = (step - 1) % 2
        
        # Reset current dp row
        for i in range(1, H + 1):
            for j in range(1, W + 1):
                dp[current][i][j] = 0
        
        # Calculate number of ways to reach each cell
        for i in range(1, H + 1):
            for j in range(1, W + 1):
                if dp[previous][i][j] > 0:
                    for dx, dy in moves:
                        ni, nj = i + dx, j + dy
                        if 1 <= ni <= H and 1 <= nj <= W:
                            dp[current][ni][nj] = (dp[current][ni][nj] + dp[previous][i][j]) % MOD

    return dp[T % 2][C][D]

# Read input
H, W, T, A, B, C, D = map(int, input().split())
# Output result
print(count_king_moves(H, W, T, A, B, C, D))