def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print(0)
        return
    
    # dp[i][j] = 区间 [i, j] 内配对后的最大得分
    # 区间长度必须是偶数才能完全配对
    dp = [[0] * n for _ in range(n)]
    
    # 枚举区间长度
    for length in range(2, n + 1):
        # 只处理偶数长度的区间
        if length % 2 == 1:
            continue
        
        # 枚举起点
        for i in range(n - length + 1):
            j = i + length - 1
            
            # 尝试将 a[i] 与区间内的某个元素配对
            for k in range(i + 1, j + 1, 2):
                # a[i] 与 a[k] 配对
                # [i+1, k-1] 和 [k+1, j] 必须都能完全配对
                score = abs(a[i] - a[k])
                
                # [i+1, k-1] 的得分
                if k - 1 >= i + 1:
                    score += dp[i + 1][k - 1]
                
                # [k+1, j] 的得分
                if j >= k + 1:
                    score += dp[k + 1][j]
                
                dp[i][j] = max(dp[i][j], score)
    
    print(dp[0][n - 1])

solve()