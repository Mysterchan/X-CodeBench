def can_satisfy_queries(N, M, Q, people, queries):
    # Initialize the strength requirements for each road
    strength = [0] * (N - 1)
    
    # Create a list to store the results for each query
    results = []
    
    # Process each query
    for L, R in queries:
        # Create a temporary array to track the strength changes
        temp_strength = [0] * (N - 1)
        
        # Mark the strength changes for the range L to R
        for i in range(L - 1, R):
            S, T = people[i]
            if S > T:
                S, T = T, S
            
            # We need to increase strength on the path from S to T
            for j in range(S - 1, T - 1):
                temp_strength[j] += 1
            
            # We need to decrease strength on the path from S to T
            if S > 1:
                temp_strength[S - 2] -= 1
            if T < N:
                temp_strength[T - 1] -= 1
        
        # Check if the temporary strength can be satisfied
        valid = True
        current_strength = 0
        for j in range(N - 1):
            current_strength += temp_strength[j]
            if current_strength < 0:
                valid = False
                break
        
        results.append("Yes" if valid else "No")
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, M, Q = map(int, data[0].split())
people = [tuple(map(int, data[i + 1].split())) for i in range(M)]
queries = [tuple(map(int, data[M + i + 1].split())) for i in range(Q)]

# Get results
results = can_satisfy_queries(N, M, Q, people, queries)

# Print results
print("\n".join(results))