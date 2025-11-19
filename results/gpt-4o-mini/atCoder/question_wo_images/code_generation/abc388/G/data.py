def count_kagamimochi(N, A, queries):
    results = []
    
    for L, R in queries:
        L -= 1  # Convert to 0-based index
        R -= 1  # Convert to 0-based index
        
        mochi_subset = A[L:R+1]  # Get the relevant slice of mochi sizes
        count = 0
        
        # Use two pointers to count pairs
        j = 0
        for i in range(len(mochi_subset)):
            while j < len(mochi_subset) and mochi_subset[j] <= 2 * mochi_subset[i]:
                j += 1
            count += j - i - 1  # All sizes from i+1 to j-1 can be paired with mochi_subset[i]
        
        # The maximum number of kagamimochi we can make is count // 2
        results.append(count // 2)
    
    return results

# Input reading
import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
A = list(map(int, data[1].split()))
Q = int(data[2])
queries = [tuple(map(int, line.split())) for line in data[3:3+Q]]

# Getting the results
results = count_kagamimochi(N, A, queries)

# Output results
for result in results:
    print(result)