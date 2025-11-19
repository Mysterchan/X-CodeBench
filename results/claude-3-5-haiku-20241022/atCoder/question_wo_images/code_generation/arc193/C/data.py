MOD = 998244353

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def solve(H, W, C):
    # Precompute factorials and inverse factorials
    max_n = H + W + 1
    fact = [1] * max_n
    for i in range(1, max_n):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * max_n
    inv_fact[max_n-1] = modinv(fact[max_n-1])
    for i in range(max_n-2, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD
    
    ans = 0
    for k in range(1, H + W):
        # k operations chosen
        contrib = 0
        for r in range(max(0, k-W), min(H, k) + 1):
            c = k - r
            if 0 <= c <= W and r + c == k:
                if r == H or c == W:
                    ways = comb(H, r) * comb(W, c) % MOD
                    colors = pow(C, k, MOD)
                    contrib = (contrib + ways * colors) % MOD
        ans = (ans + contrib) % MOD
    
    return ans

H, W, C = map(int, input().split())
print(solve(H, W, C))