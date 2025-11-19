def mod_inverse(x, mod):
    return pow(x, mod-2, mod)

def precompute_factorials(n, mod):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact[n] = mod_inverse(fact[n], mod)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return fact, inv_fact

def calculate_ways(N, a, b, k, mod):
    if k > N or a < 1 or b < 1 or a > N or b > N:
        return 0

    height_min = max(1, a - k + 1)
    height_max = min(N - k + 1, a)
    width_min = max(1, b - k + 1)
    width_max = min(N - k + 1, b)
    
    height_options = max(0, height_max - height_min + 1)
    width_options = max(0, width_max - width_min + 1)

    height_choices = height_options * width_options % mod
    return height_choices

def solve(N, a, b, queries):
    MOD = 998244353
    results = []
    for k in queries:
        result = calculate_ways(N, a, b, k, MOD)
        results.append(result)
    return results

import sys
input = sys.stdin.read

data = input().strip().split()
N = int(data[0])
a = int(data[1])
b = int(data[2])
Q = int(data[3])
queries = list(map(int, data[4:]))

output = solve(N, a, b, queries)

print('\n'.join(map(str, output)))