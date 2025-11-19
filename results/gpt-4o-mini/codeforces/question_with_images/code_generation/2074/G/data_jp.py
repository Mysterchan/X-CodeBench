def max_score(t, test_cases):
    results = []
    for n, a in test_cases:
        max_score = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    score = a[i] * a[j] * a[k]
                    max_score = max(max_score, score)
        results.append(max_score)
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1
for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index + 1].split()))
    test_cases.append((n, a))
    index += 2

# Get results
results = max_score(t, test_cases)

# Output results
for result in results:
    print(result)