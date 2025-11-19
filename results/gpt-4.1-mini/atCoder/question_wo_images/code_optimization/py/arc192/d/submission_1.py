import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
mod = 998244353

# Precompute primes up to 1000 using sieve
maxA = 1000
is_prime = [True] * (maxA + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(maxA**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, maxA+1, i):
            is_prime[j] = False
primes = [i for i in range(2, maxA+1) if is_prime[i]]

result = 1

for x in primes:
    # Extract exponents of prime x in A_i
    B = [0]*(N-1)
    for i in range(N-1):
        c = 0
        y = A[i]
        while y % x == 0:
            y //= x
            c += 1
        B[i] = c

    # The dp array will store counts of sequences of exponents of prime x
    # dp[i][j] = number of ways to have exponent j at position i
    # The exponent difference between consecutive elements is B[i]
    # The condition f(S_i/S_{i+1}) = A_i means:
    # |e_i - e_{i+1}| = B[i]
    # and min(e_i, e_{i+1}) = 0 (since gcd=1)
    # So for each step, from exponent e_i, next exponent e_{i+1} is either e_i + B[i] or e_i - B[i] if e_i >= B[i], else 0

    # To handle large exponents efficiently, we use a dict to store dp states
    from collections import defaultdict

    dp = defaultdict(int)
    dp[0] = 1  # start with exponent 0 at position 0

    for i in range(N-1):
        ndp = defaultdict(int)
        c = B[i]
        for e, cnt in dp.items():
            # next exponent can be e + c
            ndp[e + c] = (ndp[e + c] + cnt) % mod
            # or if e >= c, next exponent can be e - c
            if e >= c:
                ndp[e - c] = (ndp[e - c] + cnt) % mod
            else:
                # else next exponent is 0
                ndp[0] = (ndp[0] + cnt) % mod
        dp = ndp

    # sum over all possible exponents at position N-1
    # For each exponent e, the contribution to product is x^sum_of_exponents
    # sum_of_exponents = sum of all S_i exponents for prime x
    # But we only have exponents at each position, we need sum of all exponents in sequence

    # To get sum of exponents in sequence, note:
    # The sequence of exponents e_1, e_2, ..., e_N satisfies:
    # |e_i - e_{i+1}| = B[i], min(e_i, e_{i+1})=0
    # The dp only tracks e_i at position i
    # We need sum of all e_i for each sequence counted in dp

    # To handle sum of exponents, we modify dp to store (count, sum_of_exponents)
    # But that would be O(N * max exponent), which is large.

    # Instead, we can use the fact that the sum of exponents in the sequence is:
    # sum_{i=1}^N e_i = e_1 + e_2 + ... + e_N
    # We only track e_N in dp, but we can reconstruct sum of exponents by tracking partial sums.

    # So we redo dp with states: dp[i][e] = (count, sum_of_exponents)
    # sum_of_exponents is sum of exponents from position 1 to i+1

    dp = {0: (1, 0)}  # exponent: (count, sum_of_exponents)

    for i in range(N-1):
        ndp = dict()
        c = B[i]
        for e, (cnt, s) in dp.items():
            # next exponent = e + c
            ne = e + c
            ncnt, ns = ndp.get(ne, (0, 0))
            ndp[ne] = ((ncnt + cnt) % mod, (ns + s + cnt * ne) % mod)

            # next exponent = e - c if e >= c else 0
            if e >= c:
                ne = e - c
                ncnt, ns = ndp.get(ne, (0, 0))
                ndp[ne] = ((ncnt + cnt) % mod, (ns + s + cnt * ne) % mod)
            else:
                ne = 0
                ncnt, ns = ndp.get(ne, (0, 0))
                ndp[ne] = ((ncnt + cnt) % mod, (ns + s + cnt * ne) % mod)
        dp = ndp

    # Now sum over dp: for each exponent e at position N-1,
    # total count = cnt, total sum_of_exponents = s
    # The total sum of exponents in the sequence is s + e (since s sums exponents up to position N-1, and e is exponent at position N)
    # But we stored sum_of_exponents as sum of exponents up to position i+1, so s already includes e_i
    # Actually, in the loop, we added cnt * ne to s, so s is sum of exponents over all sequences counted by cnt

    # So s is total sum of exponents over all sequences counted by cnt

    # The contribution of prime x is sum over all sequences of x^{sum_of_exponents}
    # sum_{seq} x^{sum_of_exponents(seq)} = sum_{e} sum_of_sequences_with_e * x^{sum_of_exponents_for_that_sequence}
    # But we only have sum_of_exponents aggregated, not individual sequences.

    # Wait, we need sum of x^{sum_of_exponents} over all sequences.

    # The original code uses a trick with h[i] = x^i and dp storing sums weighted by h[j], which is equivalent.

    # Let's replicate that approach but more efficiently.

    # We'll do dp with values as sum of x^{sum_of_exponents} over sequences ending with exponent e.

    # So redo dp with dp[e] = sum of x^{sum_of_exponents} over sequences ending with exponent e.

    dp = {0: 1}  # exponent: sum of x^{sum_of_exponents}

    for i in range(N-1):
        ndp = dict()
        c = B[i]
        for e, val in dp.items():
            # next exponent = e + c
            ne = e + c
            ndp[ne] = (ndp.get(ne, 0) + val * pow(x, ne, mod)) % mod

            # next exponent = e - c if e >= c else 0
            if e >= c:
                ne = e - c
                ndp[ne] = (ndp.get(ne, 0) + val * pow(x, ne, mod)) % mod
            else:
                ne = 0
                ndp[ne] = (ndp.get(ne, 0) + val * pow(x, ne, mod)) % mod
        dp = ndp

    # sum over dp values is the total contribution for prime x
    w = sum(dp.values()) % mod
    result = (result * w) % mod

print(result)