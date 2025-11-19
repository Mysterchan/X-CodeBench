import sys
import threading
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    mod = 998244353
    inv2 = (mod + 1) // 2

    data = sys.stdin.read().strip().split()
    N = int(data[0])
    if N == 1:
        print(1)
        return

    # Sieve primes up to N
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    primes = [i for i in range(3, N + 1) if is_prime[i]]

    # Precompute factorials and invfactorials
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % mod
    invfact = [1] * (N + 1)
    invfact[N] = pow(fact[N], mod - 2, mod)
    for i in range(N, 0, -1):
        invfact[i - 1] = invfact[i] * i % mod

    # Precompute inverse of N
    invN = pow(N, mod - 2, mod)

    # Tree count: N^{N-2}
    tree_count = pow(N, N - 2, mod)

    ans = tree_count
    # Sum over unicyclic graphs with cycle length p prime >=3
    for p in primes:
        # Permutation N! / (N-p)!
        perm = fact[N] * invfact[N - p] % mod
        if p < N:
            exp = N - p - 1
            pw = pow(N, exp, mod)
        else:
            # p == N case: exponent = -1
            pw = invN
        term = perm * pw % mod * inv2 % mod
        ans += term
        if ans >= mod:
            ans -= mod

    print(ans % mod)

if __name__ == "__main__":
    main()