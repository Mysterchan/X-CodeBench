MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def solve(H, W, C):
    # Precompute factorials and inverse factorials
    max_n = H + W
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = modinv(fact[max_n])
    for i in range(max_n - 1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD
    
    result = 0
    
    # Iterate over number of operations k
    for k in range(1, H + W):
        # Calculate sum over valid (r, c) pairs
        term_sum = 0
        
        for r in range(max(1, k - W + 1), min(H, k) + 1):
            c = k - r
            if c < 1 or c > W:
                continue
            
            # Number of ways to choose operations
            ways = comb(H + W - 2, k - 1)
            
            # Contribution from this (r, c)
            contribution = ways * pow(C, k, MOD) % MOD
            term_sum = (term_sum + contribution) % MOD
        
        result = (result + term_sum) % MOD
    
    return result

H, W, C = map(int, input().split())
print(solve(H, W, C))