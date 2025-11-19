def count_valid_sequences(t, test_cases):
    MOD = 998244353
    results = []
    
    for n, parents in test_cases:
        from collections import defaultdict
        
        # Build the tree
        tree = defaultdict(list)
        for child, parent in enumerate(parents, start=2):
            tree[parent].append(child)
        
        # Calculate the number of valid sequences
        def dfs(node):
            total_ways = 1
            child_count = 0
            
            for child in tree[node]:
                child_ways = dfs(child)
                total_ways *= child_ways
                total_ways %= MOD
                child_count += 1
            
            # If the node has children, we can choose any subset of them
            if child_count > 0:
                total_ways *= factorial(child_count)
                total_ways %= MOD
            
            return total_ways
        
        # Precompute factorials
        factorial = [1] * (n + 1)
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i % MOD
        
        result = dfs(1)
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
    parents = list(map(int, data[index + 1].split()))
    test_cases.append((n, parents))
    index += 2

# Get results
results = count_valid_sequences(t, test_cases)

# Output results
for res in results:
    print(res)