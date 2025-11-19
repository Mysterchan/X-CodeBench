MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m-2, m)

def solve(H, W):
    # Precompute factorials
    max_n = H + W + 1
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = modinv(fact[max_n])
    for i in range(max_n - 1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    def comb(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD
    
    # Calculate sum of r[1] over all sequences
    sum_r1 = 0
    for k in range(1, W + 1):
        sum_r1 = (sum_r1 + k * comb(H - 1 + k, H - 1)) % MOD
    
    # Total sum = H * sum_r1
    result = H * sum_r1 % MOD
    return result

H, W = map(int, input().split())
print(solve(H, W))