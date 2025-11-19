def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

MOD = 998244353

def repunit_mod(n, mod):
    if n == 0:
        return 0
    result = 0
    power = 1
    for _ in range(n):
        result = (result + power) % mod
        power = (power * 10) % mod
    return result

def compute_lcm_mod(lcm_val, r_val, mod):
    g = gcd(lcm_val, r_val)
    
    # lcm = lcm_val * r_val / g
    # We need to compute (lcm_val / g) * r_val mod MOD
    
    lcm_div_g = lcm_val // g
    
    # Now compute lcm_div_g * r_val mod MOD
    # But r_val can be very large, so we need r_val mod MOD
    r_val_mod = r_val % mod
    
    # However, we need the actual LCM value (up to some limit) to compute the next LCM
    # So we return both: the actual LCM (if manageable) and LCM mod MOD
    
    # For actual LCM computation
    actual_lcm = lcm_val * (r_val // g)
    
    # For modular result
    result_mod = (lcm_div_g % mod * r_val_mod) % mod
    
    return actual_lcm, result_mod

N = int(input())
A = list(map(int, input().split()))

# We need to track LCM but it can grow very large
# So we track it modulo MOD for output, but also need exact value for GCD computation
# However, exact value can be too large. We need a smarter approach.

# Key insight: R_n = (10^n - 1) / 9
# LCM computation needs GCD, which requires exact values or careful modular arithmetic

# Let's track the LCM, but cap it at some reasonable value for exact computation
MAX_EXACT = 10**18

current_lcm = 0
current_lcm_mod = 0

for i in range(N):
    a = A[i]
    
    # Compute R_a
    r_a = (10**a - 1) // 9
    
    if i == 0:
        current_lcm = r_a
        current_lcm_mod = r_a % MOD
    else:
        # Compute LCM(current_lcm, r_a)
        if current_lcm <= MAX_EXACT and r_a <= MAX_EXACT:
            g = gcd(current_lcm, r_a)
            current_lcm = current_lcm * (r_a // g)
            current_lcm_mod = current_lcm % MOD
        else:
            # Need to handle large numbers carefully
            g = gcd(current_lcm if current_lcm <= MAX_EXACT else current_lcm % (10**15), r_a % (10**15))
            if g == 0:
                g = 1
            
            # Compute modular result
            lcm_div_g = current_lcm // g
            r_a_mod = r_a % MOD
            current_lcm_mod = (lcm_div_g % MOD * r_a_mod) % MOD
            
            # Update current_lcm (capped)
            new_lcm = current_lcm * (r_a // g)
            if new_lcm > MAX_EXACT:
                current_lcm = new_lcm % (10**15) + 10**15  # Keep it large but manageable
            else:
                current_lcm = new_lcm
    
    print(current_lcm_mod)