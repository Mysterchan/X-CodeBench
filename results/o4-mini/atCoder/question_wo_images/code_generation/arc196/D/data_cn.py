def can_satisfy(N, M, queries, people):
    # Initialize the strength requirements for each road
    strength = [0] * (N - 1)
    
    # Calculate the required strength changes for each person
    for S, T in people:
        if S < T:
            start, end = S - 1, T - 1
        else:
            start, end = T - 1, S - 1
        
        strength[start] += 1
        if end < N - 1:
            strength[end] -= 1
    
    # Calculate the prefix sums to determine the strength requirements
    for i in range(1, N - 1):
        strength[i] += strength[i - 1]
    
    # Check if all strength requirements are valid (must be positive)
    valid_strength = all(s > 0 for s in strength)
    
    # Prepare results for each query
    results = []
    for L, R in queries:
        if valid_strength:
            results.append("Yes")
        else:
            results.append("No")
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, M, Q = map(int, data[0].split())
people = [tuple(map(int, data[i + 1].split())) for i in range(M)]
queries = [tuple(map(int, data[M + i + 1].split())) for i in range(Q)]

# Get results
results = can_satisfy(N, M, queries, people)

# Print results
print("\n".join(results))