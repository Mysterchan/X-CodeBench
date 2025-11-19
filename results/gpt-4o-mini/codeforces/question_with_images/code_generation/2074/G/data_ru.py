def max_score(t, test_cases):
    results = []
    for n, a in test_cases:
        max_sum = 0
        # Iterate through all combinations of three vertices
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Calculate the score for the triangle formed by vertices i, j, k
                    score = a[i] * a[j] * a[k]
                    # Check if the triangle is valid (not overlapping with previous triangles)
                    if (j - i > 1) and (k - j > 1) and (n - i + j > 2):
                        max_sum = max(max_sum, score)
        results.append(max_sum)
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