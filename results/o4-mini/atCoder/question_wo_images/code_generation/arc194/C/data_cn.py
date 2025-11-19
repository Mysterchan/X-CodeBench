def min_cost_to_match(N, A, B, C):
    total_cost = 0
    for i in range(N):
        if A[i] != B[i]:
            total_cost += C[i]
    return total_cost

# Read input
N = int(input().strip())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
C = list(map(int, input().strip().split()))

# Calculate and print the result
result = min_cost_to_match(N, A, B, C)
print(result)