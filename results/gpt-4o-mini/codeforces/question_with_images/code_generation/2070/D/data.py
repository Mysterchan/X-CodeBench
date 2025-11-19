def count_valid_sequences(t, test_cases):
    MOD = 998244353
    results = []
    
    for n, parents in test_cases:
        # Build the tree as an adjacency list
        tree = [[] for _ in range(n + 1)]
        for child in range(2, n + 1):
            parent = parents[child - 2]
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
            
            # The number of ways to choose child_count children
            if child_count > 0:
                total_ways *= factorial(child_count)
                total_ways %= MOD
            
            return total_ways
        
        # Precompute factorials up to n
        factorial = [1] * (n + 1)
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i % MOD
        
        # Start DFS from the root
        result = dfs(1)
        results.append(result)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    parents = list(map(int, input().split()))
    test_cases.append((n, parents))

# Get results
results = count_valid_sequences(t, test_cases)

# Print results
for res in results:
    print(res)