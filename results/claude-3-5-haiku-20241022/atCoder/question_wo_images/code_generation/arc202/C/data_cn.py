def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

MOD = 998244353

def compute_R(n, mod):
    # R_n = (10^n - 1) / 9
    # We need to compute this modulo mod
    if n == 0:
        return 0
    
    # Compute 10^n mod (9 * mod) to avoid overflow issues
    # Then compute (10^n - 1) / 9 mod mod
    result = 0
    power = 1
    for _ in range(n):
        result = (result + power) % mod
        power = (power * 10) % mod
    return result

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    current_lcm = 1
    
    for k in range(N):
        # Compute R_{A[k]}
        R_k = compute_R(A[k], MOD * 10**15)  # Compute with high precision
        
        # Update LCM
        current_lcm = lcm(current_lcm, R_k)
        
        # Output current_lcm mod MOD
        print(current_lcm % MOD)

solve()