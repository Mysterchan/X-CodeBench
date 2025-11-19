def matrix_power_sum(N, p, A):
    # Count the number of zeros in the matrix A
    K = sum(1 for i in range(N) for j in range(N) if A[i][j] == 0)
    
    # Initialize the result matrix with zeros
    result = [[0] * N for _ in range(N)]
    
    # Calculate the contribution of each non-zero element
    for i in range(N):
        for j in range(N):
            if A[i][j] != 0:
                # Each non-zero element contributes its value multiplied by (p-1)^K
                result[i][j] = (A[i][j] * pow(p - 1, K, p)) % p
    
    # Calculate the contribution of zeros
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                # Each zero can take values from 1 to p-1
                # The contribution of zeros is (1 + 2 + ... + (p-1)) * (p-1)^(K-1)
                sum_of_ones_to_p_minus_1 = (p - 1) * (p // 2) % p
                contribution = (sum_of_ones_to_p_minus_1 * pow(p - 1, K - 1, p)) % p
                result[i][j] = (result[i][j] + contribution) % p
    
    return result

import sys
input = sys.stdin.read
data = input().splitlines()

# Read N and p
N, p = map(int, data[0].split())
# Read the matrix A
A = [list(map(int, line.split())) for line in data[1:N + 1]]

# Get the result matrix
result = matrix_power_sum(N, p, A)

# Print the result
for row in result:
    print(' '.join(map(str, row)))