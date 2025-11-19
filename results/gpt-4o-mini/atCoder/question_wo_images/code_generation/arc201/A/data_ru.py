def max_c2c_cases(test_cases):
    results = []
    for case in test_cases:
        N, problems = case
        total_div1 = total_div2 = 0
        
        for A, B, C in problems:
            total_div1 += min(A, B)  # For Div.1: one hard and one medium
            total_div2 += min(B, C)  # For Div.2: one medium and one easy
        
        # The maximum number of C2C events is limited by the total number of pairs we can form
        max_events = 0
        for i in range(min(total_div1, total_div2) + 1):
            if total_div1 - i >= 0 and total_div2 - i >= 0:
                max_events = max(max_events, i + min((total_div1 - i) // 2, (total_div2 - i) // 2))
        
        results.append(max_events)
    
    return results

import sys
input = sys.stdin.read

data = input().splitlines()
T = int(data[0])
index = 1
test_cases = []

for _ in range(T):
    N = int(data[index])
    problems = []
    for j in range(N):
        A, B, C = map(int, data[index + 1 + j].split())
        problems.append((A, B, C))
    test_cases.append((N, problems))
    index += N + 1

results = max_c2c_cases(test_cases)
print('\n'.join(map(str, results)))