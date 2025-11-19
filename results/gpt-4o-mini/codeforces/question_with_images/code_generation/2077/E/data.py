def min_operations(b):
    if not b:
        return 0
    max_darkness = max(b)
    operations = 0
    current_darkness = 0
    for darkness in b:
        if darkness > current_darkness:
            operations += darkness - current_darkness
            current_darkness = darkness
    return operations

def solve(test_cases):
    MOD = 998244353
    results = []
    
    for n, a in test_cases:
        total_sum = 0
        for l in range(n):
            current_product = 1
            for r in range(l, n):
                current_product *= a[r]
                if current_product > 0:
                    total_sum += min_operations([current_product])
                total_sum %= MOD
        results.append(total_sum)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Solve and print results
results = solve(test_cases)
for result in results:
    print(result)