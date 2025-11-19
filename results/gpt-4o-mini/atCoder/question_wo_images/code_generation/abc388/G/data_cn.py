def max_mirrors(N, sizes, Q, queries):
    results = []
    for L, R in queries:
        # Get the subarray of sizes from L to R (convert to 0-indexed)
        subarray = sizes[L - 1:R]
        count = 0
        left, right = 0, 0
        
        # Use two pointers to find pairs
        while left < len(subarray) and right < len(subarray):
            if subarray[left] * 2 >= subarray[right]:
                count += 1
                left += 1
                right += 1
            else:
                left += 1
                
        results.append(count)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
sizes = list(map(int, data[1:N+1]))
Q = int(data[N+1])
queries = []

for i in range(Q):
    L, R = map(int, data[N+2 + 2*i:N+4 + 2*i])
    queries.append((L, R))

# Get the results
results = max_mirrors(N, sizes, Q, queries)

# Print outputs
for result in results:
    print(result)