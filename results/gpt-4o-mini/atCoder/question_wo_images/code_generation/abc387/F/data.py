def count_sequences(N, M, A):
    MOD = 998244353

    # Initialize an array to keep track of the maximum x_i that can be chosen
    max_x = [0] * N
    
    # Calculate the maximum allowed value for each x_i
    for i in range(N):
        max_x[i] = max(max_x[i], max_x[A[i] - 1])

    # Count how many indices can take each value from 1 to M
    counts = [0] * (M + 1)
    for value in max_x:
        if value <= M:
            counts[value] += 1

    # Calculate the total number of sequences
    result = 1
    for i in range(1, M + 1):
        if counts[i] > 0:
            result *= (counts[i] + 1)
            result %= MOD

    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
A = list(map(int, data[2:]))

# Compute the result
result = count_sequences(N, M, A)

# Output the result
print(result)