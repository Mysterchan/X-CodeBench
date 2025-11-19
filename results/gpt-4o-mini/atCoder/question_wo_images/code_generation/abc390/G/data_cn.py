def sum_of_f(N):
    MOD = 998244353
    
    # 计算每个数字在所有排列中出现的次数
    # 各个数字出现的位权重分配
    total_sum = 0
    factorial = 1
    power_of_10 = 1
    
    for i in range(1, N + 1):
        factorial = (factorial * i) % MOD
        # current number i contributes to all positions
        total_sum = (total_sum + (i * factorial * power_of_10) % MOD) % MOD
        power_of_10 = (power_of_10 * 10) % MOD

    # All permutations contribute equally, so multiply by N!
    total_sum = (total_sum * factorial) % MOD
    
    return total_sum

N = int(input().strip())
print(sum_of_f(N))