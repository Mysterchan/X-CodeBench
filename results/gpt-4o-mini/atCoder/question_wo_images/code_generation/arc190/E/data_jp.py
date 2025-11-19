def max_operations(N, Q, A, queries):
    results = []
    for L, R in queries:
        B = A[L-1:R]
        total = sum(B)
        max_pairs = 0
        
        # Count the number of elements that are >= 1
        count = sum(1 for x in B if x >= 1)
        
        # The maximum number of operations is limited by the total number of 1s we can take
        # and the number of pairs we can form
        max_pairs = min(total // 2, count)
        
        results.append(max_pairs)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])
A = list(map(int, data[2:N+2]))
queries = []

for i in range(Q):
    L = int(data[N+2 + 2*i])
    R = int(data[N+3 + 2*i])
    queries.append((L, R))

# Get results
results = max_operations(N, Q, A, queries)

# Output results
for result in results:
    print(result)