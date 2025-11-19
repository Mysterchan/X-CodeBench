def sieve(n):
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    return [i for i in range(2, n) if is_prime[i]]

N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

primes = sieve(1001)
result = 1

for p in primes:
    # Extract exponents for this prime
    B = []
    has_prime = False
    for a in A:
        c = 0
        while a % p == 0:
            c += 1
            a //= p
        B.append(c)
        if c > 0:
            has_prime = True
    
    if not has_prime:
        result = result * (N + 1) % MOD
        continue
    
    # DP with offset tracking
    MAX_OFFSET = sum(B) + 1
    dp = {0: 1}
    
    # Precompute powers
    pow_p = [1] * (MAX_OFFSET + N * max(B) + 1)
    for i in range(1, len(pow_p)):
        pow_p[i] = pow_p[i-1] * p % MOD
    
    for i in range(N - 1):
        new_dp = {}
        b = B[i]
        
        for offset, cnt in dp.items():
            # Case 1: S[i] has b more factors than S[i+1]
            new_offset = offset + b
            if new_offset <= MAX_OFFSET:
                contribution = cnt * pow_p[new_offset] % MOD
                new_dp[new_offset] = (new_dp.get(new_offset, 0) + contribution) % MOD
            
            # Case 2: S[i+1] has b more factors than S[i] (only if b > 0)
            if b > 0:
                new_offset = offset - b
                if new_offset >= 0:
                    contribution = cnt * pow_p[new_offset] % MOD
                    new_dp[new_offset] = (new_dp.get(new_offset, 0) + contribution) % MOD
                else:
                    # Shift everything by abs(new_offset)
                    shift = -new_offset
                    contribution = cnt * pow_p[shift * (i + 1)] % MOD
                    new_dp[0] = (new_dp.get(0, 0) + contribution) % MOD
        
        dp = new_dp
    
    total = sum(dp.values()) % MOD
    result = result * total % MOD

print(result)