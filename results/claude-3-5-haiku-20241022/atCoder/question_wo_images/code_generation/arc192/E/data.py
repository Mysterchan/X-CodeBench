MOD = 998244353

W, H, L, R, D, U = map(int, input().split())

def is_block(x, y):
    if not (0 <= x <= W and 0 <= y <= H):
        return False
    if L <= x <= R and D <= y <= U:
        return False
    return True

# dp[x][y] = number of paths starting from (x, y)
dp = {}

def solve(x, y):
    if not is_block(x, y):
        return 0
    
    if (x, y) in dp:
        return dp[(x, y)]
    
    result = 1  # The path containing only this point
    
    # Try moving right
    if x + 1 <= W and is_block(x + 1, y):
        result = (result + solve(x + 1, y)) % MOD
    
    # Try moving up
    if y + 1 <= H and is_block(x, y + 1):
        result = (result + solve(x, y + 1)) % MOD
    
    dp[(x, y)] = result
    return result

# Compute dp values from top-right to bottom-left
for x in range(W, -1, -1):
    for y in range(H, -1, -1):
        if is_block(x, y):
            solve(x, y)

# Sum all paths
answer = 0
for x in range(W + 1):
    for y in range(H + 1):
        if is_block(x, y):
            answer = (answer + dp.get((x, y), 0)) % MOD

print(answer)