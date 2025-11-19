def max_cakemochi(N, sizes, Q, queries):
    results = []
    
    for L, R in queries:
        mochi_segment = sizes[L-1:R]
        count = len(mochi_segment)
        pairs = 0
        
        # To find pairs, we'll use a two-pointer approach
        i, j = 0, 0
        
        # Sort the segment in ascending order (although it should already be in order)
        mochi_segment.sort()
        
        while i < count and j < count:
            if mochi_segment[i] <= mochi_segment[j] / 2:
                pairs += 1  # We can form one pair
                i += 1      # Move from A
                j += 1      # Move from B
            else:
                j += 1      # Find a bigger B
            
        results.append(pairs)
    
    return results

# Input reading part
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
sizes = list(map(int, data[1:N+1]))
Q = int(data[N+1])
queries = [tuple(map(int, data[N+2 + i*2:N+4 + i*2])) for i in range(Q)]

# Get results
output = max_cakemochi(N, sizes, Q, queries)

# Print output
for res in output:
    print(res)