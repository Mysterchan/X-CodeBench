import sys

input = lambda: sys.stdin.readline().rstrip()
mi = lambda: map(int, input().split())

MOD = 998244353

def solve(H, W, C):
    N = max(H, W) + 1
    
    # Precompute factorials and inverse factorials
    g1 = [1] * N
    g2 = [1] * N
    for i in range(1, N):
        g1[i] = g1[i-1] * i % MOD
    
    g2[N-1] = pow(g1[N-1], MOD-2, MOD)
    for i in range(N-2, -1, -1):
        g2[i] = g2[i+1] * (i+1) % MOD
    
    # Initialize dp arrays
    dp = [[[0] * (W+1) for _ in range(H+1)] for _ in range(16)]
    
    for h in range(1, H+1):
        for w in range(1, W+1):
            # Compute dp[8]
            t = 1
            for i in range(1, h):
                t = t * C % MOD
                val = g2[i]
                dp[8][h][w] += (t - C) * dp[2][h-i][w] % MOD * val % MOD
                dp[8][h][w] += C * dp[6][h-i][w] % MOD * val % MOD
            dp[8][h][w] %= MOD
            
            # Compute dp[5] and dp[9]
            t = 1
            for i in range(1, h):
                t = t * (C-1) % MOD
                val = g2[i]
                dp[5][h][w] += (t - (C-1)) * dp[2][h-i][w] % MOD * val % MOD
                dp[5][h][w] += (C-1) * dp[6][h-i][w] % MOD * val % MOD
                dp[9][h][w] += (t - (C-1)) * dp[2][h-i][w] % MOD * val % MOD
                dp[9][h][w] += (C-1) * dp[6][h-i][w] % MOD * val % MOD
            dp[5][h][w] %= MOD
            dp[9][h][w] %= MOD
            
            # Compute dp[2]
            t = 1
            for j in range(1, w):
                t = t * C % MOD
                val = g2[j]
                dp[2][h][w] += (t - C) * dp[8][h][w-j] % MOD * val % MOD
                dp[2][h][w] += C * dp[9][h][w-j] % MOD * val % MOD
            dp[2][h][w] %= MOD
            
            # Compute dp[6]
            t = 1
            for j in range(1, w):
                t = t * (C-1) % MOD
                val = g2[j]
                dp[6][h][w] += (t - (C-1)) * dp[8][h][w-j] % MOD * val % MOD
                dp[6][h][w] += (C-1) * dp[9][h][w-j] % MOD * val % MOD
            dp[6][h][w] %= MOD
            
            # Add base cases
            base = g2[h] * g2[w] % MOD
            dp[2][h][w] = (dp[2][h][w] + C * base) % MOD
            dp[6][h][w] = (dp[6][h][w] + (C-1) * base) % MOD
            dp[5][h][w] = (dp[5][h][w] + (C-1) * base) % MOD
            
            dp[2][h][w] = (dp[2][h][w] + (pow(C, h, MOD) - C) * base) % MOD
            dp[5][h][w] = (dp[5][h][w] + (pow(C-1, h, MOD) - (C-1)) * base) % MOD
            dp[9][h][w] = (dp[9][h][w] + (pow(C-1, h, MOD) - (C-1)) * base) % MOD
            
            dp[2][h][w] = (dp[2][h][w] + (pow(C, w, MOD) - C) * base) % MOD
            dp[6][h][w] = (dp[6][h][w] + (pow(C-1, w, MOD) - (C-1)) * base) % MOD
            dp[5][h][w] = (dp[5][h][w] + (pow(C-1, w, MOD) - (C-1)) * base) % MOD
    
    # Compute tmp_g more efficiently
    tmp_g = [[0] * (W+1) for _ in range(H+1)]
    
    for total in range(max(H, W)+1):
        cc = pow(C-1, total, MOD) * C % MOD
        # Precompute sums for this total
        h_sums = [0] * (H+1)
        for h in range(H+1):
            if h <= total:
                h_sums[h] = g2[h]
                for k in range(1, min(h, total)+1):
                    h_sums[h] = (h_sums[h] + h_sums[h-k] * g2[k]) % MOD
        
        for x in range(H+1):
            for y in range(W+1):
                if x + y == total:
                    tmp_g[x][y] = (tmp_g[x][y] + cc * h_sums[x] % MOD * h_sums[y]) % MOD
    
    res = 0
    for i in range(1, H+1):
        for j in range(1, W+1):
            res = (res + dp[5][H-i][W-j] * tmp_g[i][j]) % MOD
    
    return (res * g1[H] % MOD * g1[W] + C) % MOD

H, W, C = mi()
print(solve(H, W, C))