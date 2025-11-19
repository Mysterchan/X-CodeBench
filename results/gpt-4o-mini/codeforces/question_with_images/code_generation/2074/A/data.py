def can_form_square(test_cases):
    results = []
    for l, r, d, u in test_cases:
        # Check if the distances between the points form a square
        if (r - l) == (u - d):
            results.append("Yes")
        else:
            results.append("No")
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = can_form_square(test_cases)

# Print results
for result in results:
    print(result)