def max_score(H, W, grid):
    total_sum = sum(sum(row) for row in grid)
    dp = [[0] * (W + 1) for _ in range(H + 1)]

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if i > 1:
                dp[i][j] = max(dp[i][j], dp[i - 2][j] + grid[i - 1][j - 1] + grid[i - 2][j - 1])
            if j > 1:
                dp[i][j] = max(dp[i][j], dp[i][j - 2] + grid[i - 1][j - 1] + grid[i - 1][j - 2])

    max_covered_sum = dp[H][W]
    return total_sum - max_covered_sum

import sys
input = sys.stdin.read
data = input().splitlines()

H, W = map(int, data[0].split())
grid = [list(map(int, line.split())) for line in data[1:H + 1]]

print(max_score(H, W, grid))