def solve():
    MOD = 998244353
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    
    target = 1 << N
    
    # dp[x] = x に到達する方法の数
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for x in range(target):
        if dp[x] == 0:
            continue
        
        for s in S:
            next_x = (x | s) + 1
            if next_x <= target:
                dp[next_x] = (dp[next_x] + dp[x]) % MOD
    
    print(dp[target])

solve()