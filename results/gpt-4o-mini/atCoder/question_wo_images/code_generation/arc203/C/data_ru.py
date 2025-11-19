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

def binomial_coefficient(n, k, fact, inv_fact, mod):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

def count_ways(H, W, K, fact, inv_fact, mod):
    if K < H + W - 2:
        return 0
    if K > H + W:
        return 0
    
    total_ways = binomial_coefficient(H + W - 2, K, fact, inv_fact, mod)
    
    if K >= H + W - 1:
        total_ways = (total_ways - binomial_coefficient(H + W - 2, K - 1, fact, inv_fact, mod)) % mod
    
    return total_ways

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    queries = []
    max_h_w = 0
    
    index = 1
    for _ in range(T):
        H = int(data[index])
        W = int(data[index + 1])
        K = int(data[index + 2])
        queries.append((H, W, K))
        max_h_w = max(max_h_w, H + W)
        index += 3
    
    mod = 998244353
    fact, inv_fact = precompute_factorials_and_inverses(max_h_w, mod)
    
    results = []
    for H, W, K in queries:
        result = count_ways(H, W, K, fact, inv_fact, mod)
        results.append(result)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()