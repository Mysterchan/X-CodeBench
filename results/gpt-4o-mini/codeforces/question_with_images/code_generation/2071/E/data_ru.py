def mod_inv(a, m):
    return pow(a, m - 2, m)

def expected_leaf_pairs(t, test_cases):
    MOD = 998244353
    results = []
    
    for n, probabilities, edges in test_cases:
        if n == 1:
            results.append(0)
            continue
        
        # Calculate the expected number of leaf pairs
        expected_pairs = 0
        total_probability = 1
        
        for p, q in probabilities:
            total_probability = total_probability * q % MOD
        
        for i in range(n):
            p, q = probabilities[i]
            prob_fall = p * mod_inv(q, MOD) % MOD
            prob_stay = (q - p) * mod_inv(q, MOD) % MOD
            
            # Calculate the contribution of this vertex
            expected_pairs = (expected_pairs + prob_fall * (total_probability * mod_inv(q, MOD) % MOD)) % MOD
        
        # Calculate the total number of pairs
        total_pairs = n * (n - 1) // 2 % MOD
        
        # Final expected value
        expected_value = (expected_pairs * mod_inv(total_pairs, MOD)) % MOD
        results.append(expected_value)
    
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