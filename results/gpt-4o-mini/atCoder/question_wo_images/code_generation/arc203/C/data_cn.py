def mod_inv(a, p):
    return pow(a, p - 2, p)

def precompute_factorials_and_inverses(max_n, mod):
    fact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % mod
    
    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = mod_inv(fact[max_n], mod)
    for i in range(max_n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    
    return fact, inv_fact

def binomial_coefficient(n, k, fact, inv_fact, mod):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

def count_ways(H, W, K, mod, fact, inv_fact):
    if K < H + W - 2 or K > H + W:
        return 0
    return binomial_coefficient(K, H - 1, fact, inv_fact, mod) * binomial_coefficient(K - (H - 1), W - 1, fact, inv_fact, mod) % mod

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    cases = [(int(data[i * 3 + 1]), int(data[i * 3 + 2]), int(data[i * 3 + 3])) for i in range(T)]
    
    mod = 998244353
    max_n = 400000
    fact, inv_fact = precompute_factorials_and_inverses(max_n, mod)
    
    results = []
    for H, W, K in cases:
        results.append(count_ways(H, W, K, mod, fact, inv_fact))
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()