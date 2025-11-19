def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def expected_leaf_pairs(t, test_cases):
    MOD = 998244353
    results = []
    
    for case in test_cases:
        n, probabilities, edges = case
        if n == 1:
            results.append(0)
            continue
        
        # Calculate the expected number of leaves
        expected_leaves = 0
        for p, q in probabilities:
            prob_not_falling = (q - p) * mod_inverse(q, MOD) % MOD
            expected_leaves = (expected_leaves + prob_not_falling) % MOD
        
        # Calculate the expected number of pairs of leaves
        expected_pairs = (expected_leaves * (expected_leaves - 1) // 2) % MOD
        
        results.append(expected_pairs)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
index = 1
test_cases = []

for _ in range(t):
    n = int(data[index])
    index += 1
    probabilities = []
    for _ in range(n):
        p, q = map(int, data[index].split())
        probabilities.append((p, q))
        index += 1
    edges = []
    for _ in range(n - 1):
        u, v = map(int, data[index].split())
        edges.append((u, v))
        index += 1
    test_cases.append((n, probabilities, edges))

# Get results
results = expected_leaf_pairs(t, test_cases)

# Output results
for result in results:
    print(result)