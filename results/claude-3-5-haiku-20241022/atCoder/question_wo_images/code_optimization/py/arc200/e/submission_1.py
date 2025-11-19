def solve():
    MOD = 998244353
    
    def powmod(base, exp, mod):
        result = 1
        base %= mod
        while exp > 0:
            if exp & 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp >>= 1
        return result
    
    def main(n, m):
        INV2 = powmod(2, MOD - 2, MOD)
        INV6 = powmod(6, MOD - 2, MOD)
        
        # Case 1: All elements from span of 0 bits (all identical)
        # 2^m choices for the common value
        ans = powmod(2, m, MOD)
        
        # Case 2: Span of 1 bit
        # Choose 1 bit from m: m ways
        # Choose subset of {0, 1} for that bit: 2^n - 2 non-trivial ways
        # Multiply by 2^(m-1) for other bits
        if m >= 1:
            term = (m % MOD) * ((powmod(2, n, MOD) - 2 + MOD) % MOD) % MOD
            term = term * powmod(2, m - 1, MOD) % MOD
            ans = (ans + term) % MOD
        
        # Case 3: Span of 2 bits
        # Choose 2 bits from m: m*(m-1)/2 ways
        # Valid subsets of {00, 01, 10, 11}: exclude {01, 10} together
        # Total: 2^n - 1 - (2^n - 2^(n-1) - 2^(n-1) + 1) = 2^n - 2^(n-1) - 2^(n-1)
        if m >= 2 and n >= 2:
            mC2 = (m * (m - 1) % MOD) * INV2 % MOD
            # Count valid sequences on 2-bit span
            # Can use any subset except those containing both 01 and 10
            term = (powmod(4, n, MOD) - 2 * powmod(3, n, MOD) + powmod(2, n, MOD) + powmod(2, n, MOD) - 2 + MOD) % MOD
            term = term * mC2 % MOD
            term = term * powmod(2, m - 2, MOD) % MOD
            ans = (ans + term) % MOD
        
        return ans
    
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(main(n, m))

solve()