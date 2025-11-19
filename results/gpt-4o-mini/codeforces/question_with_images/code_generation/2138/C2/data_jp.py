def max_beauty(t, test_cases):
    results = []
    for case in test_cases:
        n, k, parents = case
        # Determine the number of leaves in the tree
        degree = [0] * (n + 1)
        for p in parents:
            degree[p] += 1
            
        leaves_count = sum(1 for i in range(2, n + 1) if degree[i] == 0)
        
        # Calculate maximum beauty based on k and number of leaves
        if k == 0 or k == n:  # All 0's or all 1's
            max_beauty_value = leaves_count
        else:
            max_beauty_value = min(leaves_count, k + 1)
            
        results.append(max_beauty_value)
    
    return results


# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n, k = map(int, data[index].split())
    parents = list(map(int, data[index + 1].split()))
    test_cases.append((n, k, parents))
    index += 2

# Get results
results = max_beauty(t, test_cases)

# Print results
for result in results:
    print(result)