def find_dimensions(t, test_cases):
    MOD = 10**9 + 7
    results = []
    
    for a, b, k in test_cases:
        n = (a + k - 1) // k * k
        m = (b + k - 1) // k * k
        results.append((n % MOD, m % MOD))
    
    return results

# Input handling
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = find_dimensions(t, test_cases)

# Output results
for n, m in results:
    print(n, m)