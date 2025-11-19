def max_mex(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        a.sort()
        mex = 0
        for height in a:
            if height >= mex:
                mex += 1
        results.append(mex)
    return results

# Read input
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
results = max_mex(t, test_cases)

# Print results
for result in results:
    print(result)