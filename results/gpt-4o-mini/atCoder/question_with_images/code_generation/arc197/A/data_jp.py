def max_black_cells(T, cases):
    results = []
    for H, W, S in cases:
        d_count = S.count('D')
        r_count = S.count('R')
        question_count = S.count('?')

        # Maximum D's we can use is min(d_count + question_count, H - 1)
        max_d = min(d_count + question_count, H - 1)
        # Maximum R's we can use is min(r_count + question_count, W - 1)
        max_r = min(r_count + question_count, W - 1)

        # Total cells that can be painted black
        max_black = (max_d + 1) * (max_r + 1)
        results.append(max_black)

    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
cases = []

for i in range(1, 2 * T, 2):
    H, W = map(int, data[i].split())
    S = data[i + 1]
    cases.append((H, W, S))

# Get results
results = max_black_cells(T, cases)

# Output results
for result in results:
    print(result)