def is_geometric_progression(N, A):
    if N < 2:
        return "No"
    
    # Calculate the common ratio using the first two elements
    r = A[1] / A[0]
    
    # Check if each term follows the property of geometric progression
    for i in range(1, N):
        if A[i] * A[0] != A[1] * A[i - 1]:
            return "No"
    
    return "Yes"

# Reading input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:N + 1]))

# Output the result
print(is_geometric_progression(N, A))