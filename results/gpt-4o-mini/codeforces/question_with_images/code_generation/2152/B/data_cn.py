def krug_survival_time(test_cases):
    results = []
    for n, r_K, c_K, r_D, c_D in test_cases:
        distance = max(abs(r_K - r_D), abs(c_K - c_D))
        if distance > 1:
            results.append(distance)
        else:
            results.append(-1)
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = krug_survival_time(test_cases)

# Print output
for result in results:
    print(result)