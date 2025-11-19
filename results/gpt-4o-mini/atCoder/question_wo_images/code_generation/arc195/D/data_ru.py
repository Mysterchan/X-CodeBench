def min_operations_to_empty(T, cases):
    results = []
    for case in cases:
        N, A = case
        last_seen = {}
        operations = 0
        
        for i in range(N):
            if A[i] in last_seen:
                if last_seen[A[i]] < i - 1:
                    operations += 1  # Need to swap to group
            else:
                operations += 1  # First occurrence of this number
            
            last_seen[A[i]] = i
        
        results.append(operations)
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
cases = []
index = 1
for _ in range(T):
    N = int(data[index])
    A = list(map(int, data[index + 1].split()))
    cases.append((N, A))
    index += 2

results = min_operations_to_empty(T, cases)
print('\n'.join(map(str, results)))