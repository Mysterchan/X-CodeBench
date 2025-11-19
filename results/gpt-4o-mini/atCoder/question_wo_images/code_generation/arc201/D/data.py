def min_max_modulo(T, test_cases):
    results = []
    
    for case in test_cases:
        N, M, A, B = case
        A.sort()
        B.sort(reverse=True)

        max_value = 0
        for i in range(N):
            current_value = (A[i] + B[i]) % M
            max_value = max(max_value, current_value)
        
        results.append(max_value)
    
    return results

import sys
input = sys.stdin.read

data = input().splitlines()
T = int(data[0])
test_cases = []

index = 1
for _ in range(T):
    N, M = map(int, data[index].split())
    A = list(map(int, data[index + 1].split()))
    B = list(map(int, data[index + 2].split()))
    test_cases.append((N, M, A, B))
    index += 3

results = min_max_modulo(T, test_cases)
sys.stdout.write('\n'.join(map(str, results)) + '\n')