import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    M = 998244353

    data = sys.stdin.read().strip().split()
    N = int(data[0])

    # Special cases for small N
    if N <= 2:
        # Only one connected graph on 1 or 2 vertices
        print(1)
        return

    # Precompute primes up to N via sieve
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N+1, i):
                is_prime[j] = False
    primes = [i for i in range(3, N+1) if is_prime[i]]

    # Precompute factorials and inverse factorials up to N
    fact = [1] * (N + 1)
    for i in range(1, N+1):
        fact[i] = fact[i-1] * i % M
    invfact = [1] * (N + 1)
    invfact[N] = pow(fact[N], M-2, M)
    for i in range(N, 0, -1):
        invfact[i-1] = invfact[i] * i % M

    # Precompute powers of N: pow_N[k] = N^k mod M for k=0..N
    pow_N = [1] * (N + 1)
    for i in range(1, N+1):
        pow_N[i] = pow_N[i-1] * N % M

    inv2 = (M + 1) // 2
    invN = pow(N, M-2, M)

    # Count trees: N^{N-2}
    ans = pow_N[N-2]

    # Sum unicyclic graphs with cycle length p prime (p >= 3)
    # Term for each p:  (1/2) * (N! / (N-p)!) * N^{N-p-1}
    #               = fact[N] * invfact[N-p] * pow_N[N-p-1] * inv2   (handle p=N case separately)
    fN = fact[N]
    for p in primes:
        # exponent e = N-p-1
        e = N - p - 1
        if e >= 0:
            pw = pow_N[e]
        else:
            # only e == -1 when p == N
            pw = invN
        term = fN * invfact[N-p] % M
        term = term * pw % M
        term = term * inv2 % M
        ans = (ans + term) % M

    print(ans)

if __name__ == "__main__":
    main()