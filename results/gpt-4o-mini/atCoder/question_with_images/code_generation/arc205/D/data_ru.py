def max_operations(T, cases):
    results = []
    
    for case in cases:
        N, p = case
        children = [[] for _ in range(N + 1)]
        
        for i in range(2, N + 1):
            children[p[i - 2]].append(i)
        
        # To count the number of valid pairs (u, v)
        count = 0
        
        # We will use a stack to perform a DFS
        stack = []
        for i in range(1, N + 1):
            while stack and stack[-1] < i:
                stack.pop()
            if stack:
                count += 1
            stack.append(i)
        
        results.append(count)
    
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
for result in results:
    print(result)