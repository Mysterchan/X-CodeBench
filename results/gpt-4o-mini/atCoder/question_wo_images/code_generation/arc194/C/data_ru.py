def min_cost_to_match_sequences(N, A, B, C):
    total_cost = 0
    cost_to_flip = 0
    
    for i in range(N):
        if A[i] != B[i]:
            cost_to_flip += C[i]
    
    total_cost = cost_to_flip
    
    for i in range(N):
        if A[i] != B[i]:
            # Calculate the cost if we flip A[i]
            new_cost = cost_to_flip - C[i] + (sum(C) - C[i])
            total_cost = min(total_cost, new_cost)
    
    return total_cost

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))
B = list(map(int, data[N+1:2*N+1]))
C = list(map(int, data[2*N+1:3*N+1]))

# Get the result and print it
result = min_cost_to_match_sequences(N, A, B, C)
print(result)