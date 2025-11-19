def count_trees(test_cases):
    MOD = 998244353
    results = []
    
    for A in test_cases:
        N = len(A)
        # Create a list to store the parent-child relationships
        parent = [-1] * N
        valid = True
        
        # Check the conditions for the adjacency matrix
        for i in range(N):
            for j in range(N):
                if A[i][j] == 1:
                    if parent[i] == -1:
                        parent[i] = j
                    elif parent[i] != j:
                        valid = False
                        break
            if not valid:
                break
        
        if not valid:
            results.append(0)
            continue
        
        # Count the number of valid trees
        count = 1
        for i in range(N):
            if parent[i] == -1:
                count = (count * 2) % MOD
        
        results.append(count)
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []
index = 1

for _ in range(T):
    N = int(data[index])
    index += 1
    A = []
    for i in range(N):
        A.append(list(map(int, data[index + i].split())))
    test_cases.append(A)
    index += N

results = count_trees(test_cases)

for result in results:
    print(result)