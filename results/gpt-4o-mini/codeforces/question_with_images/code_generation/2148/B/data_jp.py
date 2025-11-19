def min_crossings(test_cases):
    results = []
    for n, m, x, y, a, b in test_cases:
        horizontal_crossings = sum(1 for height in a if height < y)
        vertical_crossings = sum(1 for width in b if width < x)
        total_crossings = horizontal_crossings + vertical_crossings
        results.append(total_crossings)
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

index = 0
t = int(data[index])
index += 1

test_cases = []
for _ in range(t):
    n, m, x, y = map(int, data[index].split())
    index += 1
    a = list(map(int, data[index].split()))
    index += 1
    b = list(map(int, data[index].split()))
    index += 1
    test_cases.append((n, m, x, y, a, b))

results = min_crossings(test_cases)

# Print output
for result in results:
    print(result)