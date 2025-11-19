def count_gravity_sort_pairs(t, test_cases):
    MOD = 998244353
    results = []
    
    for n, p, c in test_cases:
        # Create a list of tuples (height, color)
        blocks = [(p[i], c[i]) for i in range(n)]
        # Sort by height first, then by color
        blocks.sort()
        
        # Count the number of blocks with the same height and color
        from collections import defaultdict
        count_map = defaultdict(int)
        
        for height, color in blocks:
            count_map[(height, color)] += 1
        
        # Calculate the result
        result = 1
        for count in count_map.values():
            # For each unique (height, color) pair, we can arrange them in count! ways
            for i in range(1, count + 1):
                result = (result * i) % MOD
        
        results.append(result)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n = int(data[index])
    p = list(map(int, data[index + 1].split()))
    c = list(map(int, data[index + 2].split()))
    test_cases.append((n, p, c))
    index += 3

# Get results
results = count_gravity_sort_pairs(t, test_cases)

# Output results
for res in results:
    print(res)