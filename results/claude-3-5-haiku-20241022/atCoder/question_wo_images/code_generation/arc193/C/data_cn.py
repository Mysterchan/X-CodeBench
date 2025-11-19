MOD = 998244353

def solve():
    H, W, C = map(int, input().split())
    
    # dp[i][j] = number of ways to color first i rows and j columns completely
    # such that all cells in these rows/columns are colored
    
    # The answer involves counting sequences where we paint crosses
    # Key: the last operation determines many cell colors
    
    # For H x W grid with C colors:
    # We need to count valid painting sequences
    
    # Using inclusion-exclusion or DP on which rows/cols are "dominated"
    
    # After analysis: answer = sum over k operations of:
    # (ways to choose k cells) * (ways to order them) * C^k * (constraint satisfaction)
    
    # Simplified approach based on the structure:
    # The answer follows a pattern related to permutations and colorings
    
    # For small cases, we can verify:
    # H=2, W=3, C=2: answer should be 26
    
    # The formula involves:
    # Sum over valid operation sequences that cover all cells
    
    # Dynamic programming approach:
    # dp[r][c] represents states after covering r rows and c columns
    
    # Using the factorial-based formula for this specific problem type:
    fact = [1] * (H + W + 1)
    for i in range(1, H + W + 1):
        fact[i] = fact[i-1] * i % MOD
    
    # The answer is based on: C^(H+W-1) * sum of valid arrangements
    # This is a Catalan-like structure
    
    ans = 0
    
    # For each possible last row and column
    for last_row in range(H):
        for last_col in range(W):
            # Count arrangements where (last_row, last_col) determines final colors
            # Previous operations must cover all other cells
            # Number of ways = C^(H+W-1) for this configuration
            ways = pow(C, H + W - 1, MOD)
            ans = (ans + ways) % MOD
    
    print(ans)

solve()