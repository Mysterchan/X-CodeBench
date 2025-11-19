def solve():
    MOD = 998244353
    H, W, T, A, B, C, D = map(int, input().split())
    
    # Convert to 0-indexed
    A -= 1
    B -= 1
    C -= 1
    D -= 1
    
    # dp[t][i][j] = number of ways to reach (i, j) after t steps
    # We'll use two arrays to save memory
    prev = [[0] * W for _ in range(H)]
    prev[A][B] = 1
    
    directions = [
        (1, 1), (1, 0), (1, -1),
        (0, 1), (0, -1),
        (-1, 1), (-1, 0), (-1, -1)
    ]
    
    for t in range(T):
        curr = [[0] * W for _ in range(H)]
        
        for i in range(H):
            for j in range(W):
                if prev[i][j] == 0:
                    continue
                    
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < H and 0 <= nj < W:
                        curr[ni][nj] = (curr[ni][nj] + prev[i][j]) % MOD
        
        prev = curr
    
    print(prev[C][D])

solve()