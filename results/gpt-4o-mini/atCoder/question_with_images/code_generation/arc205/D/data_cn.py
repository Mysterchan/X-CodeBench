def max_operations(T, cases):
    results = []
    
    for case in cases:
        N, p = case
        children = [[] for _ in range(N + 1)]
        
        for i in range(2, N + 1):
            children[p[i - 2]].append(i)
        
        max_pairs = 0
        leaf_count = 0
        
        for i in range(1, N + 1):
            if not children[i]:  # If it's a leaf node
                leaf_count += 1
            else:
                max_pairs += (len(children[i]) // 2)
        
        max_pairs += leaf_count // 2
        results.append(max_pairs)
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
cases = []

index = 1
for _ in range(T):
    N = int(data[index])
    p = list(map(int, data[index + 1].split()))
    cases.append((N, p))
    index += 2

results = max_operations(T, cases)
print('\n'.join(map(str, results)))