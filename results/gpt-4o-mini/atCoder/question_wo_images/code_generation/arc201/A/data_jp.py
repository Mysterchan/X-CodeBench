def max_c2c_cases(test_cases):
    results = []
    for case in test_cases:
        N, problems = case
        total_div1 = total_div2 = 0
        
        for A, B, C in problems:
            total_div1 += min(A, B)  # Div.1 requires Hard and Medium
            total_div2 += min(B, C)  # Div.2 requires Medium and Easy
        
        # The maximum number of contests we can hold is limited by the total number of Div.1 and Div.2 we can create
        results.append(min(total_div1, total_div2))
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []
index = 1

for _ in range(T):
    N = int(data[index])
    problems = []
    for i in range(N):
        A, B, C = map(int, data[index + 1 + i].split())
        problems.append((A, B, C))
    test_cases.append((N, problems))
    index += N + 1

results = max_c2c_cases(test_cases)
print('\n'.join(map(str, results)))