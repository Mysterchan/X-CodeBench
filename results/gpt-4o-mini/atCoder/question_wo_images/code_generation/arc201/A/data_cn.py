def max_c2c_cases(test_cases):
    results = []
    for case in test_cases:
        N, proposals = case
        div1_pairs = 0
        div2_pairs = 0
        
        for A, B, C in proposals:
            div1_pairs += min(A, B)
            div2_pairs += min(B, C)
        
        # The maximum number of C2C events is limited by the pairs we can form
        results.append(min(div1_pairs, div2_pairs))
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []
index = 1

for _ in range(T):
    N = int(data[index])
    proposals = []
    for i in range(N):
        A, B, C = map(int, data[index + 1 + i].split())
        proposals.append((A, B, C))
    test_cases.append((N, proposals))
    index += N + 1

results = max_c2c_cases(test_cases)

for result in results:
    print(result)