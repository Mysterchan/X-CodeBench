def max_sum_after_operations(N, A):
    S = []
    for i in range(N):
        if A[i] > 0:
            S.append(A[i])
        elif S and A[i] < 0:
            S.pop()
    return sum(S)

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:N+1]))

# Get the result and print it
result = max_sum_after_operations(N, A)
print(result)