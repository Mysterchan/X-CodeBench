def can_satisfy_requests(N, M, Q, people, queries):
    # Initialize the results list
    results = []
    
    # Create an array to track the balance of each road
    balance = [0] * (N - 1)
    
    # Process each query
    for L, R in queries:
        # Reset the balance for each query
        for i in range(N - 1):
            balance[i] = 0
        
        # Check the people in the range [L, R]
        for i in range(L - 1, R):
            S, T = people[i]
            if S > T:
                S, T = T, S
            
            # Update the balance for the roads used by this person
            for j in range(S - 1, T - 1):
                balance[j] += 1
            
            # Check if any road has a balance that exceeds the number of people
            if any(b > 1 for b in balance):
                results.append("No")
                break
        else:
            results.append("Yes")
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

# First line contains N, M, Q
N, M, Q = map(int, data[0].split())

# Next M lines contain S_i and T_i
people = [tuple(map(int, line.split())) for line in data[1:M + 1]]

# Next Q lines contain L_k and R_k
queries = [tuple(map(int, line.split())) for line in data[M + 1:M + 1 + Q]]

# Get results
results = can_satisfy_requests(N, M, Q, people, queries)

# Print results
print("\n".join(results))