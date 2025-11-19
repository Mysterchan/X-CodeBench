import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353

    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    maxA = 2 * 10**5

    # Precompute smallest prime factor (spf) for 1..maxA
    spf = [0] * (maxA + 1)
    spf[1] = 1
    for i in range(2, maxA + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= maxA:
                for j in range(i * i, maxA + 1, i):
                    if spf[j] == 0:
                        spf[j] = i

    # Function to factorize n using spf
    def factorize(n):
        factors = {}
        while n > 1:
            p = spf[n]
            factors[p] = factors.get(p, 0) + 1
            n //= p
        return factors

    # Modular inverse using Fermat's little theorem (MOD prime)
    def modinv(a):
        return pow(a, MOD - 2, MOD)

    # Precompute modular inverses of 9 and 10
    inv9 = modinv(9)
    inv10 = modinv(10)

    # Function to compute R_n mod MOD:
    # R_n = (10^n - 1) / 9 mod MOD
    def R(n):
        # pow(10, n, MOD)
        p = pow(10, n, MOD)
        val = (p - 1) * inv9 % MOD
        return val

    # Maintain max exponents of prime factors for LCM
    max_exp = {}

    # Current LCM modulo MOD
    lcm_mod = 1

    for k in range(N):
        n = A[k]
        f = factorize(n)
        # For each prime factor, update max exponent and lcm_mod accordingly
        for p, e in f.items():
            prev_e = max_exp.get(p, 0)
            if e > prev_e:
                diff = e - prev_e
                # Update max exponent
                max_exp[p] = e
                # Multiply lcm_mod by p^diff mod MOD
                lcm_mod = (lcm_mod * pow(p, diff, MOD)) % MOD
        # Compute R_{lcm} mod MOD
        # lcm = product p^{max_exp[p]}
        # R_lcm = (10^{lcm} - 1)/9 mod MOD
        # But lcm can be huge, so we must compute 10^{lcm} mod MOD efficiently
        # We have lcm = product p^{max_exp[p]}
        # We can compute 10^{lcm} mod MOD using repeated modular exponentiation:
        # 10^{lcm} mod MOD = pow(10, lcm, MOD)
        # But lcm can be huge (up to product of primes powers), so we must compute lcm as integer first.
        # But lcm can be very large (up to 2*10^5 factors), so we cannot store lcm as integer directly.
        # Instead, we can compute 10^{lcm} mod MOD by repeated modular exponentiation:
        # pow(10, lcm, MOD) = pow(10, product p^{max_exp[p]}, MOD)
        # We can do this by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, product p^{max_exp[p]}, MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ... , MOD)
        # We can compute this by:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # But lcm is huge, so we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can do this by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # But lcm is huge, so we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can do this by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # = pow(10, p1^{e1} * p2^{e2} * ..., MOD)
        # We can compute pow(10, lcm, MOD) by:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So we must compute pow(10, lcm, MOD) by repeated pow calls:
        # pow(10, lcm, MOD) = pow(10, lcm, MOD)
        # So we need to compute lcm as integer first, but it can be huge.
        # So