def max_operations(T, cases):
    results = []
    
    for case in cases:
        N, parents = case
        children = [[] for _ in range(N + 1)]
        
        for i in range(2, N + 1):
            children[parents[i - 2]].append(i)
        
        max_pairs = 0
        for child in children[1]:
            max_pairs += len(children[child])
        
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
    parents = list(map(int, data[index + 1].split()))
    cases.append((N, parents))
    index += 2

results = max_operations(T, cases)
for result in results:
    print(result)