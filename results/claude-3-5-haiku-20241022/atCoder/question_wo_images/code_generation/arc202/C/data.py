import math

MOD = 998244353

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_mod(a, b, mod):
    # LCM(a, b) = a * b / GCD(a, b)
    # But we need to be careful with modular arithmetic
    g = gcd(a, b)
    # a // g first to avoid overflow
    result = (a // g) % mod
    result = (result * (b % mod)) % mod
    return result

def compute_R(n, mod):
    # R_n = (10^n - 1) / 9
    # In modular arithmetic: R_n = (10^n - 1) * modinv(9, mod)
    if n == 0:
        return 0
    
    # Compute 10^n mod (9 * mod) to preserve divisibility by 9
    # Actually, let's compute it directly
    power = pow(10, n, 9 * mod)
    r = (power - 1) // 9
    return r

def modinv(a, mod):
    return pow(a, mod - 2, mod)

n = int(input())
a = list(map(int, input().split()))

# For LCM computation, we need actual values not just mod
# Let's maintain LCM as a factorization or compute carefully

current_lcm = compute_R(a[0], MOD * 10**18)  # Get actual value

for k in range(n):
    if k == 0:
        current_lcm = compute_R(a[0], 10**100)
    else:
        r_ak = compute_R(a[k], 10**100)
        current_lcm = (current_lcm * r_ak) // gcd(current_lcm, r_ak)
    
    print(current_lcm % MOD)