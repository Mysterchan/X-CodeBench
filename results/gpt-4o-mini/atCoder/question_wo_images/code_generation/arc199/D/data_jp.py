def calculate_sum(H, W):
    MOD = 998244353
    
    # 2^(H + W) - 1
    total_matrices = pow(2, H + W, MOD) - 1
    
    # Each matrix contributes to the sum of its elements
    # The contribution of each matrix is the number of 1s in it
    # The number of 1s in a matrix can be calculated as:
    # (r * c) for all possible r and c
    # where r is the number of rows filled and c is the number of columns filled
    # The total contribution is:
    # Sum of (r * c) for r in [1, H] and c in [1, W]
    
    total_sum = 0
    for r in range(1, H + 1):
        for c in range(1, W + 1):
            total_sum += r * c
    
    # Each configuration contributes to the total sum
    total_sum = (total_sum * total_matrices) % MOD
    
    return total_sum

# Read input
H, W = map(int, input().split())
# Calculate and print the result
print(calculate_sum(H, W))