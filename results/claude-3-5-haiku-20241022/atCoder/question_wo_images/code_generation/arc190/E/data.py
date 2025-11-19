def solve(B):
    n = len(B)
    if n == 0:
        return 0
    if n == 1:
        return 0
    
    # dp[i] = max operations using elements up to index i
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # Don't use element i-1
        dp[i] = dp[i-1]
        
        # Pair with previous element (distance 1)
        if i >= 2:
            pairs = min(B[i-2], B[i-1])
            dp[i] = max(dp[i], dp[i-2] + pairs)
        
        # Pair with element 2 positions back (distance 2)
        if i >= 3:
            pairs = min(B[i-3], B[i-1])
            dp[i] = max(dp[i], dp[i-3] + pairs)
    
    return dp[n]