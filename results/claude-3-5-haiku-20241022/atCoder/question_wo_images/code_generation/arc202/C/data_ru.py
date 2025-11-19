def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

MOD = 998244353

def compute_r(n):
    # R_n = (10^n - 1) / 9
    return (pow(10, n, MOD * 9) - 1) // 9

def factorize(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def merge_factors(f1, f2):
    result = f1.copy()
    for p, e in f2.items():
        result[p] = max(result.get(p, 0), e)
    return result

def factors_from_value(val):
    return factorize(val)

n = int(input())
a = list(map(int, input().split()))

lcm_factors = {}

for i in range(n):
    # Compute R_{A_i}
    r_val = compute_r(a[i])
    
    # Factorize R_{A_i}
    r_factors = factors_from_value(r_val)
    
    # Merge with current LCM factors
    lcm_factors = merge_factors(lcm_factors, r_factors)
    
    # Compute LCM mod MOD
    result = 1
    for prime, exp in lcm_factors.items():
        result = (result * pow(prime, exp, MOD)) % MOD
    
    print(result)