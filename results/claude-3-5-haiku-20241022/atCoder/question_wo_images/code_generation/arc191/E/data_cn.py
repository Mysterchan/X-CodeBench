def calculate_grundy(a, b, x, y):
    """計算單個袋子的Grundy數"""
    if a == 0 and b == 0:
        return 0
    
    # 使用記憶化來計算Grundy數
    memo = {}
    
    def grundy(gold, silver):
        if gold == 0 and silver == 0:
            return 0
        
        if (gold, silver) in memo:
            return memo[(gold, silver)]
        
        reachable = set()
        
        # 操作1: 移除1個金幣，添加x或y個銀幣（取決於誰的回合）
        # 由於遊戲對稱，我們需要考慮兩種情況
        if gold > 0:
            # 當前玩家使用x添加銀幣
            new_silver = silver + x
            if new_silver <= 10**15:  # 防止溢出
                reachable.add(grundy(gold - 1, new_silver))
        
        # 操作2: 移除1個銀幣
        if silver > 0:
            reachable.add(grundy(gold, silver - 1))
        
        # 計算mex (minimum excludant)
        mex = 0
        while mex in reachable:
            mex += 1
        
        memo[(gold, silver)] = mex
        return mex
    
    # 簡化的Grundy數計算
    # 對於這類遊戲，我們需要考慮操作的效果
    if a == 0:
        return b % 2
    
    # 計算總的Grundy數
    # 金幣可以轉換成銀幣，銀幣只能被移除
    total = a * x + b
    
    # 根據X和Y的關係來決定Grundy數
    if x <= y:
        # Takahashi有優勢
        return (a + b) % 2
    else:
        # 需要更仔細的計算
        return (a * (x - y) + b) % 2

def solve():
    MOD = 998244353
    n, x, y = map(int, input().split())
    
    bags = []
    for _ in range(n):
        a, b = map(int, input().split())
        bags.append((a, b))
    
    # 計算每個袋子的Grundy數
    grundy_values = []
    for a, b in bags:
        if a == 0 and b == 0:
            g = 0
        elif a == 0:
            g = b % 2
        else:
            # 計算Grundy數
            # 關鍵觀察: 金幣可以轉換成x個銀幣(Takahashi)或y個銀幣(Aoki)
            # 銀幣只能被移除
            if x == y:
                g = (a + b) % 2
            else:
                # 計算等效的Grundy數
                # 考慮最終會剩下多少銀幣
                total = a * x + b
                g = total % (x + 1) if x < y else (a * (x - y) + b) % 2
        
        grundy_values.append(g)
    
    # 使用動態規劃計算有多少種分配方式使得Takahashi的XOR和為0
    # XOR和為0意味著Takahashi處於必敗態，所以Aoki會贏
    # 我們要計算XOR和非0的情況數
    
    dp = {0: 1}
    
    for g in grundy_values:
        new_dp = {}
        for xor_val, count in dp.items():
            # 不選這個袋子(給Aoki)
            new_xor = xor_val
            new_dp[new_xor] = (new_dp.get(new_xor, 0) + count) % MOD
            
            # 選這個袋子(給Takahashi)
            new_xor = xor_val ^ g
            new_dp[new_xor] = (new_dp.get(new_xor, 0) + count) % MOD
        
        dp = new_dp
    
    # Takahashi贏的情況是XOR和非0
    total = pow(2, n, MOD)
    losing = dp.get(0, 0)
    answer = (total - losing) % MOD
    
    print(answer)

solve()