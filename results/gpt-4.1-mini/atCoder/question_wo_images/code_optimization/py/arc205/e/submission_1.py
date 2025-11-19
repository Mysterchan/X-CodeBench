import sys
input = sys.stdin.readline
MOD = 998244353

n = int(input())
A = list(map(int, input().split()))

# dp[mask]: product of all A_i with lower 10 bits == mask
dp = [1] * 1024
res = []

for x in A:
    p = x >> 10
    q = x & 1023

    # Compute product over all dp[p<<10 | d] where d subset of p
    # Here dp is only for lower 10 bits, so we consider subsets of p
    # We want product of dp[d] for all d subset of p
    # Use subset iteration over p
    ans = x
    d = p
    while True:
        ans = ans * dp[d] % MOD
        if d == 0:
            break
        d = (d - 1) & p

    res.append(ans)

    # Update dp for all masks that are supersets of q
    # i.e. for all d where d & q == q
    # We iterate over all masks d where d & q == q
    # This is equivalent to iterating over all masks d where d has q bits set and arbitrary other bits
    # So iterate over all masks d with q fixed bits set, and other bits arbitrary
    # The number of such masks is 2^(number of bits not in q) = 2^(10 - popcount(q))
    # So we iterate over all subsets of the complement of q and add q to them

    mask = (~q) & 1023
    sub = mask
    while True:
        dp[q | sub] = dp[q | sub] * x % MOD
        if sub == 0:
            break
        sub = (sub - 1) & mask

print(*res, sep='\n')