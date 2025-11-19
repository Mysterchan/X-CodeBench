def modinv(a, m):
    return pow(a, m - 2, m)

def expected_leaf_pairs(t, test_cases):
    MOD = 998244353
    results = []
    
    for case in test_cases:
        n, probabilities, edges = case
        if n < 2:
            results.append(0)
            continue
        
        # Calculate the probability of each vertex being a leaf
        leaf_prob = [0] * n
        for i in range(n):
            p, q = probabilities[i]
            leaf_prob[i] = (p * modinv(q, MOD)) % MOD
        
        # Calculate the expected number of pairs of leaves
        expected_pairs = 0
        for u, v in edges:
            u -= 1
            v -= 1
            # Probability that u is a leaf and v is not
            prob_u_leaf_v_not = (leaf_prob[u] * (1 - leaf_prob[v])) % MOD
            # Probability that v is a leaf and u is not
            prob_v_leaf_u_not = (leaf_prob[v] * (1 - leaf_prob[u])) % MOD
            
            expected_pairs = (expected_pairs + prob_u_leaf_v_not + prob_v_leaf_u_not) % MOD
        
        # Each pair is counted twice, so divide by 2
        expected_pairs = (expected_pairs * modinv(2, MOD)) % MOD
        results.append(expected_pairs)
    
    return results

# Read input
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
    for i in range(n):
        p, q = map(int, data[index].split())
        probabilities.append((p, q))
        index += 1
    edges = []
    for i in range(n - 1):
        u, v = map(int, data[index].split())
        edges.append((u, v))
        index += 1
    test_cases.append((n, probabilities, edges))

# Get results
results = expected_leaf_pairs(t, test_cases)

# Print results
for result in results:
    print(result)