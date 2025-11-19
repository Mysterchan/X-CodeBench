MOD = 998244353

H, W = map(int, input().split())
A = []
for _ in range(H):
    row = list(map(int, input().split()))
    A.append(row)

Q, sh, sw = map(int, input().split())
sh -= 1  # Convert to 0-indexed
sw -= 1

def compute_dp():
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = A[0][0]
    
    for h in range(H):
        for w in range(W):
            if h == 0 and w == 0:
                continue
            val = 0
            if h > 0:
                val = (val + dp[h-1][w]) % MOD
            if w > 0:
                val = (val + dp[h][w-1]) % MOD
            dp[h][w] = (A[h][w] * val) % MOD
    
    return dp

def update_dp(dp, start_h, start_w):
    # Recompute DP starting from (start_h, start_w) and all cells that depend on it
    for h in range(start_h, H):
        for w in range(start_w, W):
            if h == 0 and w == 0:
                dp[0][0] = A[0][0]
                continue
            val = 0
            if h > 0:
                val = (val + dp[h-1][w]) % MOD
            if w > 0:
                val = (val + dp[h][w-1]) % MOD
            dp[h][w] = (A[h][w] * val) % MOD

dp = compute_dp()

for _ in range(Q):
    d, a = input().split()
    a = int(a)
    
    # Move Takahashi
    if d == 'U':
        sh -= 1
    elif d == 'D':
        sh += 1
    elif d == 'L':
        sw -= 1
    elif d == 'R':
        sw += 1
    
    # Update the grid
    A[sh][sw] = a
    
    # Update DP from the changed cell
    update_dp(dp, sh, sw)
    
    print(dp[H-1][W-1])