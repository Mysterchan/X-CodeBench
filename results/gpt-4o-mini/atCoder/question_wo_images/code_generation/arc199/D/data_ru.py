def calculate_sum(H, W):
    MOD = 998244353
    
    # Total number of matrices that can be formed
    total_matrices = (1 << (H + W - 1)) % MOD
    
    # Each matrix contributes to the sum based on the number of 1s
    # The contribution of each cell A[i][j] is determined by the number of ways to fill it
    # A[i][j] can be filled if we have at least one operation affecting its row or column
    # The number of ways to fill A[i][j] is (2^(i-1) * 2^(H-i)) * (2^(j-1) * 2^(W-j))
    # This simplifies to 2^(H + W - 2)
    
    # The total contribution of all cells is:
    # total_matrices * (H * W) * 2^(H + W - 2)
    
    # Calculate the power of 2
    power_of_2 = pow(2, H + W - 2, MOD)
    
    # Calculate the final result
    result = (total_matrices * (H * W) % MOD) * power_of_2 % MOD
    
    return result

# Read input
H, W = map(int, input().split())
# Calculate and print the result
print(calculate_sum(H, W))