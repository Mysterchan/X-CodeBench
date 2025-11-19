import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    mod = 998244353

    data = sys.stdin.read().strip().split()
    N = int(data[0])
    if N == 1:
        # Only the trivial graph on 1 vertex
        print(1)
        return

    # 1) Sieve primes up to N
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            for j in range(start, N + 1, step):
                is_prime[j] = False
    primes = [i for i in range(3, N + 1) if is_prime[i]]

    # 2) Precompute factorials and inverse factorials
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact = [1] * (N + 1)
    inv_fact[N] = pow(fact[N], mod - 2, mod)
    for i in range(N, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % mod

    inv2 = (mod + 1) // 2
    # 3) Count labeled trees: N^{N-2}
    tree_count = pow(N, N - 2, mod)

    # Precompute inverse of N for the case p == N
    invN = pow(N, mod - 2, mod)

    # 4) Sum over unicyclic graphs with cycle-length = prime p >= 3
    #    Term for each p: (1/2) * [N! / (N-p)!] * N^{N-p-1}  (or N^{-1} if exponent = -1)
    total_unicyclic = 0
    Nfact = fact[N]
    for p in primes:
        # p is prime and p >= 3
        # Compute N! / (N-p)! mod
        ways_cycle = Nfact * inv_fact[N - p] % mod
        # Compute the power factor N^{N-p-1}, or inv(N) if p == N
        exp = N - p - 1
        if exp >= 0:
            pow_part = pow(N, exp, mod)
        else:
            # only happens when p == N, so exp == -1
            pow_part = invN
        term = ways_cycle * pow_part % mod
        term = term * inv2 % mod
        total_unicyclic = (total_unicyclic + term) % mod

    # 5) Final answer is trees + unicyclics
    ans = (tree_count + total_unicyclic) % mod
    print(ans)

if __name__ == "__main__":
    main()