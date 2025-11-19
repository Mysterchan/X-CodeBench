def min_max_remainder(T, test_cases):
    results = []
    
    for case in test_cases:
        N, M, A, B = case
        A.sort()
        B.sort(reverse=True)
        
        max_remainder = 0
        for a, b in zip(A, B):
            max_remainder = max(max_remainder, (a + b) % M)
        
        results.append(max_remainder)
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []
line_index = 1

for _ in range(T):
    N, M = map(int, data[line_index].split())
    A = list(map(int, data[line_index + 1].split()))
    B = list(map(int, data[line_index + 2].split()))
    test_cases.append((N, M, A, B))
    line_index += 3

results = min_max_remainder(T, test_cases)

for result in results:
    print(result)