def modinv(a, p):
    return pow(a, p - 2, p)

def precompute_factorials_and_inverses(max_n, mod):
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % mod
    
    inv_fact[max_n] = modinv(fact[max_n], mod)
    
    for i in range(max_n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    
    return fact, inv_fact

def comb(n, k, fact, inv_fact, mod):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

def solve_cases(cases, mod):
    results = []
    for H, W, K in cases:
        if K < (H + W - 1) or K > (H + W):
            results.append(0)
            continue
        
        # Calculate the number of ways to choose K walls
        ways = comb(H + W - 2, K - 1, fact, inv_fact, mod)
        results.append(ways)
    
    return results

import sys
input = sys.stdin.read

MOD = 998244353
MAX_N = 400000

fact, inv_fact = precompute_factorials_and_inverses(MAX_N, MOD)

data = input().split()
T = int(data[0])
cases = []

index = 1
for _ in range(T):
    H = int(data[index])
    W = int(data[index + 1])
    K = int(data[index + 2])
    cases.append((H, W, K))
    index += 3

results = solve_cases(cases, MOD)

sys.stdout.write('\n'.join(map(str, results)) + '\n')