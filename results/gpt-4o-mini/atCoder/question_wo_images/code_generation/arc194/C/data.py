def min_cost_to_match_sequences(N, A, B, C):
    total_cost = 0
    current_cost = sum(A[i] * C[i] for i in range(N))
    
    for i in range(N):
        if A[i] != B[i]:
            # Calculate the cost if we flip A[i]
            new_cost = current_cost - A[i] * C[i] + (1 - A[i]) * C[i]
            total_cost += new_cost
            current_cost = new_cost
            A[i] = 1 - A[i]  # Flip A[i]
    
    return total_cost

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))
B = list(map(int, data[N+1:2*N+1]))
C = list(map(int, data[2*N+1:3*N+1]))

# Calculate and print the result
result = min_cost_to_match_sequences(N, A, B, C)
print(result)