def max_score(N, A):
    total_score = 0
    # Sort the array to maximize the absolute differences
    A.sort()
    
    # Calculate the score by pairing the largest and smallest elements
    for i in range(N // 2):
        total_score += A[N - 1 - i] - A[i]
    
    return total_score

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N + 1]))

# Get the result and print it
result = max_score(N, A)
print(result)