def solve():
    MOD = 998244353
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    
    target = 1 << N  # 2^N
    
    # dp[x] = number of ways to reach value x
    dp = [0] * (target + 1)
    dp[0] = 1  # Start at x = 0
    
    # Process each value from 0 to target-1
    for x in range(target):
        if dp[x] == 0:
            continue
        
        # Try each operation
        for s_i in S:
            # Apply operation: new_x = (x OR s_i) + 1
            new_x = (x | s_i) + 1
            
            if new_x <= target:
                dp[new_x] = (dp[new_x] + dp[x]) % MOD
    
    print(dp[target])

solve()