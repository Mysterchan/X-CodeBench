def min_cost_to_paint(T, cases):
    results = []
    for case in cases:
        N, U, D, L, R = case
        min_cost = float('inf')

        for i in range(N - 2):
            cost1 = U[i] + D[i]  # Vertical pair
            cost2 = L[i] + R[i]  # Horizontal pair
            min_cost = min(min_cost, cost1, cost2)

        total_cost = (N - 2) * min_cost
        results.append(total_cost)

    return results

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
cases = []
index = 1
for _ in range(T):
    N = int(data[index])
    U = list(map(int, data[index + 1].split()))
    D = list(map(int, data[index + 2].split()))
    L = list(map(int, data[index + 3].split()))
    R = list(map(int, data[index + 4].split()))
    cases.append((N, U, D, L, R))
    index += 5

results = min_cost_to_paint(T, cases)
for result in results:
    print(result)