def max_black_cells(T, cases):
    results = []
    for H, W, S in cases:
        d_count = S.count('D')
        r_count = S.count('R')
        question_count = S.count('?')

        # Maximum possible D and R we can use
        max_d = min(H - 1, d_count + question_count)
        max_r = min(W - 1, r_count + question_count)

        # Calculate the maximum number of cells that can be painted black
        max_cells = (max_d + 1) * (max_r + 1)
        results.append(max_cells)

    return results

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
cases = []

for i in range(1, T + 1):
    H, W = map(int, data[2 * i - 1].split())
    S = data[2 * i]
    cases.append((H, W, S))

results = max_black_cells(T, cases)
print('\n'.join(map(str, results)))