def min_max_modulo(t, test_cases):
    results = []
    for case in test_cases:
        n, m, A, B = case
        A.sort()
        B.sort(reverse=True)
        
        current_max = 0
        for i in range(n):
            current_max = max(current_max, (A[i] + B[i]) % m)
        
        results.append(current_max)
    
    return results

import sys
input = sys.stdin.read

data = input().splitlines()
T = int(data[0])
test_cases = []

line_index = 1
for _ in range(T):
    n, m = map(int, data[line_index].split())
    a = list(map(int, data[line_index + 1].split()))
    b = list(map(int, data[line_index + 2].split()))
    test_cases.append((n, m, a, b))
    line_index += 3

results = min_max_modulo(T, test_cases)
sys.stdout.write('\n'.join(map(str, results)) + '\n')