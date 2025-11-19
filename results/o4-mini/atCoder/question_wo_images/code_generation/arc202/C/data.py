import sys
import threading
from math import gcd

MOD = 998244353
MAX_A = 200000

def main():
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    # Precompute smallest prime factor (spf) for all numbers up to MAX_A
    spf = [0] * (MAX_A + 1)
    spf[1] = 1
    for i in range(2, MAX_A + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= MAX_A:
                for j in range(i * i, MAX_A + 1, i):
                    if spf[j] == 0:
                        spf[j] = i

    # Function to factorize a number using spf
    def factorize(x):
        factors = {}
        while x > 1:
            p = spf[x]
            factors[p] = factors.get(p, 0) + 1
            x //= p
        return factors

    # We want to maintain the LCM of R_{A_1}, ..., R_{A_k}
    # Recall:
    # R_n = (10^n - 1) / 9
    # So prime factors of R_n come from prime factors of (10^n - 1) and 9.
    # 9 = 3^2, so factor 3 separately.

    # Key property:
    # gcd(R_a, R_b) = R_gcd(a,b)
    # lcm(R_a, R_b) = R_lcm(a,b)

    # So LCM(R_{A_1}, ..., R_{A_k}) = R_{lcm(A_1,...,A_k)}

    # But we cannot just compute R_{lcm} directly for large lcm (up to 2e5 * many times).
    # Instead, factorize R_n by prime factorization of n and multiplicative order of 10 mod p.

    # Factorization of R_n:
    # R_n = (10^n - 1)/9
    # 10^n - 1 = product over d|n of Phi_d(10) (cyclotomic polynomials)
    # Phi_n(10) is irreducible and prime factors of R_n come from Phi_d(10) for d|n, d>1.

    # To find prime factorization of R_n, we use the formula:
    # prime factors of R_n = union of prime factors of Phi_d(10) for all d|n, d>1
    # and factor 3^2 from denominator 9.

    # We will:
    # 1) Precompute prime factorization of all numbers up to MAX_A (done)
    # 2) For each prime p != 3, find the multiplicative order of 10 mod p
    # 3) For each n, factor R_n by:
    #    - factor 3^max(0, 2 - exponent of 3 in 10^n - 1)
    #    - for each prime p dividing 10^n - 1, p divides R_n if order_p(10) divides n
    #    - exponent of p in R_n is the exponent of p in 10^n - 1 minus exponent of p in 9 (only for p=3)
    #
    # But this is complicated and slow for large n.

    # Alternative approach:
    # Since gcd(R_a, R_b) = R_gcd(a,b) and lcm(R_a, R_b) = R_lcm(a,b),
    # the LCM of R_{A_1}, ..., R_{A_k} = R_{L_k} where L_k = lcm(A_1,...,A_k).

    # So we only need to maintain L_k = lcm of A_1,...,A_k and output R_{L_k} mod MOD.

    # Now, how to compute R_n mod MOD efficiently for large n?

    # R_n = (10^n - 1) / 9 mod MOD
    # Since MOD is prime, inverse of 9 mod MOD exists.
    inv9 = pow(9, MOD - 2, MOD)

    # So R_n mod MOD = (10^n - 1) * inv9 mod MOD

    # We just need to maintain L_k = lcm(A_1,...,A_k) efficiently.

    # To maintain L_k:
    # - Factorize each A_i
    # - For each prime factor p, keep max exponent seen so far
    # - L_k = product over p of p^{max_exp_p}

    # Since N and A_i up to 2e5, factorization with spf is fast.

    # We will maintain a dictionary max_exp for prime exponents in L_k.

    max_exp = {}
    current_lcm = 1  # will store the integer value of L_k (not needed actually)
    # Instead, we only need to compute 10^{L_k} mod MOD, so we need to know L_k.

    # But L_k can be huge (up to product of primes^exponents), so we cannot store L_k directly.

    # Instead, we can store L_k as prime factorization max_exp.

    # To compute 10^{L_k} mod MOD, we need to compute 10^{L_k} mod MOD.

    # Since L_k can be huge (up to 2e5 * many times), we cannot compute 10^{L_k} directly.

    # But we can compute 10^{L_k} mod MOD by:
    # 10^{L_k} mod MOD = 10^{product p^{e_p}} mod MOD

    # We cannot exponentiate 10 to a huge number directly.

    # So we need to compute exponent L_k modulo (MOD-1) because of Fermat's little theorem:
    # For prime MOD, a^{b} mod MOD = a^{b mod (MOD-1)} mod MOD

    # So we only need L_k mod (MOD-1).

    # So we maintain L_k mod (MOD-1) as well.

    # To do this:
    # - For each prime p with exponent e, L_k includes p^e
    # - So L_k mod (MOD-1) = product over p of p^{e} mod (MOD-1)

    # We can maintain L_k_mod = product of p^{e} mod (MOD-1)

    # For each new A_i:
    # - factorize A_i
    # - for each prime factor p with exponent e_i:
    #   - if e_i > max_exp[p], update max_exp[p] = e_i
    #   - update L_k_mod accordingly

    # To update L_k_mod:
    # - old exponent = old_e
    # - new exponent = e_i
    # - difference = new_e - old_e
    # - L_k_mod = L_k_mod * p^{difference} mod (MOD-1)

    # Finally, compute R_{L_k} = (10^{L_k_mod} - 1) * inv9 mod MOD

    max_exp = {}
    L_k_mod = 1  # L_k mod (MOD-1)

    for i in range(N):
        x = A[i]
        factors = {}
        while x > 1:
            p = spf[x]
            factors[p] = factors.get(p, 0) + 1
            x //= p

        for p, e in factors.items():
            old_e = max_exp.get(p, 0)
            if e > old_e:
                diff = e - old_e
                max_exp[p] = e
                # Update L_k_mod = L_k_mod * p^{diff} mod (MOD-1)
                # pow with mod (MOD-1)
                L_k_mod = (L_k_mod * pow(p, diff, MOD - 1)) % (MOD - 1)

        # Compute R_{L_k} mod MOD
        # R_{L_k} = (10^{L_k_mod} - 1) * inv9 mod MOD
        val = (pow(10, L_k_mod, MOD) - 1) * inv9 % MOD
        print(val)

threading.Thread(target=main).start()