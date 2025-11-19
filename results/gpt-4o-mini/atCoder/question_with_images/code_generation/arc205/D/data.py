def max_operations(test_cases):
    results = []
    
    for p in test_cases:
        N = len(p) + 1
        children = [[] for _ in range(N + 1)]
        
        # Build the tree
        for i in range(2, N + 1):
            children[p[i - 2]].append(i)
        
        # Count the number of children for each node
        child_count = [0] * (N + 1)
        for i in range(1, N + 1):
            child_count[i] = len(children[i])
        
        # Calculate the maximum number of operations
        max_ops = 0
        for i in range(1, N + 1):
            if child_count[i] > 1:
                max_ops += child_count[i] // 2
        
        results.append(max_ops)
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []

for i in range(1, T + 1):
    N = int(data[i * 2 - 1])
    p = list(map(int, data[i * 2].split()))
    test_cases.append(p)

results = max_operations(test_cases)

for result in results:
    print(result)