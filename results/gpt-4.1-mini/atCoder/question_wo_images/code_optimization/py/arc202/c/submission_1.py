import sys
input = sys.stdin.readline

MOD = 998244353
MAX = 2 * 10**5

# Precompute smallest prime factor (spf) for each number up to MAX
spf = [0] * (MAX + 1)
def sieve_spf():
    spf[1] = 1
    for i in range(2, MAX + 1):
        if spf[i] == 0:
            spf[i] = i
            for j in range(i * i, MAX + 1, i):
                if spf[j] == 0:
                    spf[j] = i
sieve_spf()

# Fast modular exponentiation
def modpow(base, exp, mod):
    result = 1
    cur = base % mod
    while exp > 0:
        if exp & 1:
            result = (result * cur) % mod
        cur = (cur * cur) % mod
        exp >>= 1
    return result

# Factorize n using spf
def factorize(n):
    factors = {}
    while n > 1:
        p = spf[n]
        factors[p] = factors.get(p, 0) + 1
        n //= p
    return factors

# Compute modular inverse using Fermat's little theorem (MOD is prime)
def modinv(x):
    return modpow(x, MOD - 2, MOD)

N = int(input())
A = list(map(int, input().split()))

# We maintain the maximum exponent of each prime factor in the LCM of R_{A_1}..R_{A_k}
max_exp = {}

# Current LCM modulo MOD
lcm_mod = 1

for k in range(N):
    n = A[k]
    # Factorize n
    f = factorize(n)
    # For each prime factor p^e in n, update max_exp and lcm_mod accordingly
    for p, e in f.items():
        prev = max_exp.get(p, 0)
        if e > prev:
            diff = e - prev
            # Update lcm_mod by multiplying p^diff mod MOD
            lcm_mod = (lcm_mod * modpow(p, diff, MOD)) % MOD
            max_exp[p] = e
    # Compute R_n mod MOD = (10^n - 1) * inv(9) mod MOD
    # But since LCM(R_{A_1}..R_{A_k}) = product over p of p^{max_exp[p]} where p are prime factors of n,
    # and R_n = (10^n - 1)/9, the LCM is product of R_{max_exp} for each prime factor.
    # So lcm_mod already represents the LCM modulo MOD.
    print(lcm_mod)