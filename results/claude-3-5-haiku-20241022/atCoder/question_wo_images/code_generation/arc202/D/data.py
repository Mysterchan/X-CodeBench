def count_adjacent(i, j, H, W):
    """Count valid adjacent squares and return them"""
    adjacent = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 1 <= ni <= H and 1 <= nj <= W:
                adjacent.append((ni, nj))
    return adjacent

H, W, T, A, B, C, D = map(int, input().split())

MOD = 998244353

# Use dictionary for sparse representation
# dp[position] = number of ways to reach this position
current = {(A, B): 1}

for t in range(T):
    next_dp = {}
    
    for (i, j), count in current.items():
        # Try all 8 directions
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 1 <= ni <= H and 1 <= nj <= W:
                    if (ni, nj) not in next_dp:
                        next_dp[(ni, nj)] = 0
                    next_dp[(ni, nj)] = (next_dp[(ni, nj)] + count) % MOD
    
    current = next_dp

# Get answer
answer = current.get((C, D), 0)
print(answer)