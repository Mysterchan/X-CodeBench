def min_operations_to_empty(T, cases):
    results = []
    for case in cases:
        N, A = case
        # Count the number of distinct elements
        distinct_count = len(set(A))
        # The minimum operations needed is the number of distinct elements
        results.append(distinct_count + (N - distinct_count))
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