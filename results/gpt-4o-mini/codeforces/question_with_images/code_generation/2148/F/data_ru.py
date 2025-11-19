def lexicographically_minimal_bottom_row(test_cases):
    results = []
    for arrays in test_cases:
        combined = []
        for a in arrays:
            combined.extend(a)
        combined.sort()
        results.append(combined)
    
    return results

import sys

input = sys.stdin.read
data = input().splitlines()
t = int(data[0])
idx = 1
test_cases = []

for _ in range(t):
    n = int(data[idx])
    idx += 1
    arrays = []
    for _ in range(n):
        line = list(map(int, data[idx].split()))
        arrays.append(line[1:])  # Skip the first integer since it's k_i
        idx += 1
    test_cases.append(arrays)

results = lexicographically_minimal_bottom_row(test_cases)
for result in results:
    print(" ".join(map(str, result)))