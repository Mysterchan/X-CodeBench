def calculate_sum(H, W):
    MOD = 998244353
    total_sum = 0
    
    # The number of ways to choose rows and columns
    row_choices = (1 << H) - 1  # 2^H - 1
    col_choices = (1 << W) - 1  # 2^W - 1
    
    # Each configuration contributes to the sum
    for r in range(1, H + 1):
        for c in range(1, W + 1):
            total_sum += r * c * (row_choices * col_choices) % MOD
            total_sum %= MOD
            
    return total_sum

H, W = map(int, input().split())
result = calculate_sum(H, W)
print(result)