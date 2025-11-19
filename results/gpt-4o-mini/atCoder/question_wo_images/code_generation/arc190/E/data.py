def max_operations(N, Q, A, queries):
    results = []
    
    for L, R in queries:
        # Convert to 0-based index
        L -= 1
        R -= 1
        
        # Extract the subarray B
        B = A[L:R + 1]
        
        # Calculate the total number of operations
        total = sum(B)
        max_operations = total // 2
        
        # The maximum number of operations is limited by the number of pairs we can form
        # We can only form pairs of adjacent elements, so we need to check the number of pairs
        pairs = 0
        for i in range(len(B) - 1):
            pairs += min(B[i], B[i + 1])
        
        # The result for this query is the minimum of total // 2 and the number of pairs
        results.append(min(max_operations, pairs))
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])
A = list(map(int, data[2:N + 2]))
queries = []

for i in range(Q):
    L = int(data[N + 2 + 2 * i])
    R = int(data[N + 3 + 2 * i])
    queries.append((L, R))

# Get results
results = max_operations(N, Q, A, queries)

# Print results
for result in results:
    print(result)