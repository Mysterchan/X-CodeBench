def solve():
    MOD = 998244353
    N = int(input())
    
    # 预计算阶乘
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i-1] * i % MOD
    
    # 计算每个数字的字符串长度
    lengths = [len(str(i)) for i in range(N + 1)]
    
    # 计算总和
    total = 0
    
    # 对每个位置 i (0-indexed, 即第 i+1 个位置)
    for pos in range(N):
        # 在位置 pos 放置数字 num
        for num in range(1, N + 1):
            # num 在位置 pos 时的贡献
            # 前面有 pos 个位置,后面有 N-1-pos 个位置
            # 前面位置的总长度会影响 num 的权重
            
            # 计算前面所有可能排列的长度总和
            # 前面有 pos 个数字,从剩余 N-1 个数字中选择
            # 每种选择的排列数是 (N-1)! / (N-1-pos)!
            
            # 对于前面的每种长度组合,计算权重
            contrib = 0
            
            # 前面 pos 个位置可以放置的数字是除了 num 之外的 N-1 个数字
            # 考虑所有可能的前缀长度
            
            # 使用动态规划计算前缀长度的期望
            # dp[j] = 前 j 个位置的总长度和,考虑所有可能的排列
            
            # 简化:前面 pos 个位置,每个数字(除num外)出现的次数相同
            # 每个数字出现 pos * (N-2)! 次
            total_len_before = 0
            for other in range(1, N + 1):
                if other != num:
                    total_len_before = (total_len_before + lengths[other]) % MOD
            
            # 前面 pos 个位置,每个可选数字出现次数: pos * fact[N-2]
            # 总的排列数: pos * fact[N-1]
            if pos > 0:
                avg_len = total_len_before * pow(N - 1, MOD - 2, MOD) % MOD
                total_prefix_len = avg_len * pos % MOD
            else:
                total_prefix_len = 0
            
            # num 的权重 = 10^(后面所有数字的总长度)
            # 后面 N-1-pos 个位置
            total_len_after = 0
            for other in range(1, N + 1):
                if other != num:
                    total_len_after = (total_len_after + lengths[other]) % MOD
            
            if N - 1 - pos > 0:
                avg_len_after = total_len_after * pow(N - 1, MOD - 2, MOD) % MOD
                total_suffix_len = avg_len_after * (N - 1 - pos) % MOD
            else:
                total_suffix_len = 0
            
            # num 的贡献
            weight = pow(10, int(total_prefix_len + total_suffix_len), MOD)
            num_contrib = num * weight % MOD
            
            # 排列数: fact[pos] * fact[N-1-pos]
            arrangements = fact[pos] * fact[N - 1 - pos] % MOD
            
            contrib = num_contrib * arrangements % MOD
            total = (total + contrib) % MOD
    
    print(total)

solve()