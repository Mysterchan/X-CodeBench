def can_transform(test_cases):
    results = []
    for n, s, t in test_cases:
        # Check the number of '1's in both strings
        if (s.count('1') % 2) != (t.count('1') % 2):
            results.append("No")
        else:
            results.append("Yes")
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

# Process test cases
t = int(data[0])
test_cases = []
index = 1
for _ in range(t):
    n = int(data[index])
    s = data[index + 1]
    t = data[index + 2]
    test_cases.append((n, s, t))
    index += 3

# Get results
results = can_transform(test_cases)

# Print results
print("\n".join(results))