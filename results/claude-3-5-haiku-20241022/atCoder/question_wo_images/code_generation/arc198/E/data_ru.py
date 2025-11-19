def solve():
    MOD = 998244353
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    
    target = 1 << N
    
    # dp[x] = количество способов достигнуть x
    dp = {}
    dp[0] = 1
    
    # Обрабатываем все возможные значения x от 0 до target-1
    for x in range(target):
        if x not in dp:
            continue
        
        ways = dp[x]
        
        # Пробуем все элементы из S
        for s in S:
            next_x = (x | s) + 1
            
            if next_x <= target:
                if next_x not in dp:
                    dp[next_x] = 0
                dp[next_x] = (dp[next_x] + ways) % MOD
    
    print(dp.get(target, 0))

solve()