def max_total_score(N, A):
    # Sort the array to maximize the score
    A.sort()
    
    # The maximum score is the sum of absolute differences between adjacent elements
    total_score = 0
    for i in range(1, N):
        total_score += A[i] - A[i - 1]
    
    return total_score

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N + 1]))

# Calculate and print the result
result = max_total_score(N, A)
print(result)