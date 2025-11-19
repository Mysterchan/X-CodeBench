import math

MOD = 998244353

def pow_mod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

def inv_mod(a, mod):
    return pow_mod(a, mod - 2, mod)

def repunit_mod(n, mod):
    if n == 0:
        return 0
    if mod == 1:
        return 0
    # R_n = (10^n - 1) / 9
    if n < 20:
        return int("1" * n) % mod
    ten_pow_n = pow_mod(10, n, mod * 9)
    return ((ten_pow_n - 1) // 9) % mod

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def lcm_mod(a, b, a_mod, b_mod, mod):
    # a and b are the actual values (kept as factors)
    # a_mod and b_mod are a % mod and b % mod
    g = math.gcd(a, b)
    
    # LCM = a * b / gcd(a, b)
    # We need to compute (a / g) * b mod MOD
    
    a_div_g = a // g
    
    # Compute (a_div_g * b_mod) % MOD
    result = (a_div_g % mod) * b_mod % mod
    
    return result

n = int(input())
nums = list(map(int, input().split()))

# Store R_A_i as tuples (value, value_mod)
# For small values, compute directly; for large, use modular arithmetic
repunits = []
for a in nums:
    if a <= 10:
        val = int("1" * a)
        repunits.append((val, val % MOD))
    else:
        val_mod = repunit_mod(a, MOD)
        repunits.append((a, val_mod))  # Store a as proxy for large values

# Compute LCM iteratively
current_lcm_factors = {}  # Store prime factorization conceptually
current_val = nums[0]
current_mod = repunits[0][1]

print(current_mod)

for i in range(1, n):
    next_val = nums[i]
    next_mod = repunits[i][1]
    
    if current_val <= 10 and next_val <= 10:
        val1 = int("1" * current_val)
        val2 = int("1" * next_val)
        g = math.gcd(val1, val2)
        current_val = val1 // g * val2
        current_mod = current_val % MOD
    else:
        # Use modular arithmetic approach
        val1 = int("1" * current_val) if current_val <= 18 else None
        val2 = int("1" * next_val) if next_val <= 18 else None
        
        if val1 is not None and val2 is not None:
            g = math.gcd(val1, val2)
            lcm_val = val1 // g * val2
            current_val = min(current_val, next_val) if lcm_val > 10**18 else 0
            current_mod = lcm_val % MOD
        else:
            # Both are large, use modular computation
            g = math.gcd(current_val, next_val)
            a_div_g = current_val // g
            current_mod = (repunit_mod(a_div_g, MOD) * next_mod) % MOD
            current_val = max(current_val, next_val)
    
    print(current_mod)