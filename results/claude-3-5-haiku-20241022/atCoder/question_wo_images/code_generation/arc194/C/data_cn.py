def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    # 找出需要翻转的位置
    flips_needed = []
    for i in range(N):
        if A[i] != B[i]:
            flips_needed.append(i)
    
    if not flips_needed:
        print(0)
        return
    
    # 使用动态规划或贪心策略
    # 状态：当前A的状态，哪些位置已经被翻转
    # 由于每次操作后都要支付成本，我们需要找到最优的翻转顺序
    
    # 关键观察：每次翻转一个位置后，成本取决于当前A中所有为1的位置
    # 我们需要决定翻转的顺序以最小化总成本
    
    # 使用位掩码DP
    m = len(flips_needed)
    if m > 20:
        # 对于大的情况，使用贪心或其他策略
        # 但根据约束，我们可以尝试完全搜索
        pass
    
    # 使用DP: dp[mask] = 完成mask中的翻转所需的最小成本
    # mask表示flips_needed中哪些位置已经被翻转
    INF = float('inf')
    dp = [INF] * (1 << m)
    dp[0] = 0
    
    for mask in range(1 << m):
        if dp[mask] == INF:
            continue
        
        # 计算当前A的状态
        current_A = A[:]
        for j in range(m):
            if mask & (1 << j):
                idx = flips_needed[j]
                current_A[idx] = 1 - current_A[idx]
        
        # 尝试翻转每一个还没翻转的位置
        for j in range(m):
            if not (mask & (1 << j)):
                idx = flips_needed[j]
                # 翻转这个位置
                new_A = current_A[:]
                new_A[idx] = 1 - new_A[idx]
                
                # 计算成本
                cost = sum(new_A[k] * C[k] for k in range(N))
                
                new_mask = mask | (1 << j)
                dp[new_mask] = min(dp[new_mask], dp[mask] + cost)
    
    print(dp[(1 << m) - 1])

solve()