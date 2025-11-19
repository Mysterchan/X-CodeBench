import sys
import math
sys.setrecursionlimit(10**7)
MOD = 998244353

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    # We want to find all sequences S = (S_1,...,S_N) of positive integers such that:
    # For each i: f(S_i / S_{i+1}) = A_i
    # where f(x) = P*Q if x = P/Q in lowest terms (P,Q coprime positive integers)
    # and gcd(S_1,...,S_N) = 1
    #
    # f(S_i / S_{i+1}) = A_i means:
    # Let d = gcd(S_i, S_{i+1})
    # Then S_i = d * p, S_{i+1} = d * q with gcd(p,q) = 1
    # and p * q = A_i
    #
    # So for each i, (S_i, S_{i+1}) = (d*p, d*q) where p*q = A_i and gcd(p,q)=1.
    #
    # We want to find all sequences S with gcd=1 satisfying these conditions.
    #
    # Key insight:
    # Represent S_i as product of prime factors raised to some exponents.
    # Each A_i can be factorized into primes.
    #
    # For each prime factor, the condition p*q = A_i with gcd(p,q)=1 means
    # the prime factors of A_i are split between p and q with no overlap.
    #
    # So for each prime factor, the exponent in A_i is assigned either to p or q.
    #
    # This means for each prime factor, the exponents of S_i and S_{i+1} differ by the exponent in A_i,
    # with one side having 0 and the other having the exponent.
    #
    # So for each prime factor, the sequence of exponents (e_1, e_2, ..., e_N) satisfies:
    # |e_i - e_{i+1}| = exponent of that prime in A_i
    #
    # Since gcd(S_1,...,S_N) = 1, for each prime factor, min(e_i) = 0.
    #
    # We want to find sum over all sequences S with gcd=1 of product(S_i).
    #
    # product(S_i) = product over primes of product over i of p^{e_i}
    # = product over primes of p^{sum e_i}
    #
    # So the total sum is product over primes of sum over all exponent sequences (e_i) with
    # |e_i - e_{i+1}| = exponent in A_i, min(e_i)=0, of p^{sum e_i}.
    #
    # We can solve independently for each prime factor and multiply results.
    #
    # Steps:
    # 1. Factorize all A_i into primes and record exponents.
    # 2. For each prime factor, get the sequence B = [b_1,...,b_{N-1}] where b_i = exponent of prime in A_i.
    # 3. For each prime factor, solve:
    #    Find sum over all sequences e with |e_i - e_{i+1}| = b_i, min(e_i)=0, of p^{sum e_i}.
    #
    # To solve for each prime:
    # - The sequence e is determined by choosing signs for differences:
    #   e_{i+1} = e_i ± b_i
    # - We want all sequences with min(e_i)=0.
    #
    # We can use DP:
    # Let dp[i][v] = sum of p^{sum e_j} over all sequences up to i with e_i = v and min(e_j) = 0.
    #
    # For i=1, e_1=0, dp[1][0] = p^0 = 1
    #
    # For i from 1 to N-1:
    # For each v in dp[i]:
    #   e_{i+1} = v + b_i or v - b_i (if >=0)
    #   Update dp[i+1][new_v] += dp[i][v] * p^{new_v}
    #
    # Finally sum dp[N][v] over v.
    #
    # Since p^{sum e_i} = product p^{e_i}, and at each step we multiply by p^{e_{i+1}},
    # we can accumulate the sum of exponents by multiplying by p^{new_v} at each step.
    #
    # Implement this for each prime factor and multiply results modulo MOD.
    #
    # To factorize A_i efficiently, precompute primes up to 1000 (max A_i).
    # Then factorize each A_i.
    #
    # Finally multiply all prime results modulo MOD.
    #
    # Note: p can be large prime, but we only need p^{exponent} mod MOD.
    # We'll use pow(p, exponent, MOD).
    #
    # Also, the maximum exponent sum can be large, but since exponents are at most sum of b_i,
    # and b_i <= 1000, N <= 1000, max exponent sum <= 1000*1000=10^6, pow with mod is efficient.
    #
    # We'll implement DP with dictionary to store dp states to save memory.
    #
    # Let's proceed.

    # Step 1: prime sieve for factorization
    MAX_A = 1000
    spf = [0]*(MAX_A+1)  # smallest prime factor
    def sieve():
        spf[1] = 1
        for i in range(2, MAX_A+1):
            if spf[i] == 0:
                spf[i] = i
                for j in range(i*i, MAX_A+1, i):
                    if spf[j] == 0:
                        spf[j] = i
    sieve()

    def factorize(x):
        factors = {}
        while x > 1:
            f = spf[x]
            factors[f] = factors.get(f,0)+1
            x //= f
        return factors

    # Step 2: collect all primes appearing in any A_i
    prime_set = set()
    factorizations = []
    for x in A:
        f = factorize(x)
        factorizations.append(f)
        prime_set.update(f.keys())
    primes = sorted(prime_set)

    # Step 3: for each prime, build exponent sequence B
    prime_to_B = {}
    for p in primes:
        B = []
        for f in factorizations:
            B.append(f.get(p,0))
        prime_to_B[p] = B

    # Step 4: for each prime, solve DP
    # dp[i][v] = sum of p^{sum e_j} for sequences up to i with e_i = v and min(e_j)=0
    # i from 1 to N, e_1=0
    # transitions:
    # e_{i+1} = e_i + b_i or e_i - b_i (if >=0)
    # multiply by p^{e_{i+1}} at each step

    # We'll implement a function to compute sum for one prime factor
    def solve_prime(p, B):
        from collections import defaultdict
        dp = defaultdict(int)
        # i=1, e_1=0
        dp[0] = 1  # p^{0} = 1
        for b in B:
            ndp = defaultdict(int)
            for v, val in dp.items():
                # e_{i+1} = v + b
                nv = v + b
                add_val = val * pow(p, nv, MOD) % MOD
                ndp[nv] = (ndp[nv] + add_val) % MOD
                # e_{i+1} = v - b if >=0
                if v - b >= 0:
                    nv2 = v - b
                    add_val2 = val * pow(p, nv2, MOD) % MOD
                    ndp[nv2] = (ndp[nv2] + add_val2) % MOD
            dp = ndp
        # sum over all v
        return sum(dp.values()) % MOD

    # Step 5: multiply all prime results modulo MOD
    ans = 1
    for p in primes:
        res = solve_prime(p, prime_to_B[p])
        ans = (ans * res) % MOD

    print(ans)

if __name__ == "__main__":
    main()