def sum_of_matrices(H, W):
    MOD = 998244353
    
    # Total number of matrices that can be formed
    total_matrices = (1 << (H + W - 2)) % MOD
    
    # Each cell A[i][j] can be 1 in total_matrices configurations
    # The contribution of each cell to the total sum
    total_sum = (total_matrices * H * W) % MOD
    
    return total_sum

# Read input
H, W = map(int, input().split())
# Output the result
print(sum_of_matrices(H, W))