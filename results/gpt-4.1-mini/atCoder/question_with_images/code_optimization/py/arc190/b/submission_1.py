import sys
input = sys.stdin.readline

MOD = 998244353

N, a, b = map(int, input().split())
Q = int(input())
ks = list(map(int, input().split()))

# Precompute factorials and inverse factorials up to N
# Since N can be up to 10^7, we must do this efficiently and only once.

# Use iterative factorial and inverse factorial computation
factorial = [1] * (N + 1)
for i in range(1, N + 1):
    factorial[i] = factorial[i - 1] * i % MOD

inv_factorial = [1] * (N + 1)
inv_factorial[N] = pow(factorial[N], MOD - 2, MOD)
for i in range(N - 1, -1, -1):
    inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return factorial[n] * inv_factorial[k] % MOD * inv_factorial[n - k] % MOD

# For each k, compute:
# ways_rows_k = C(a-1, k-1) * C(N - a, N - k)
# ways_cols_k = C(b-1, k-1) * C(N - b, N - k)
# total_ways = ways_rows_k * ways_cols_k % MOD

# Note: intervals_needed = N, so intervals_needed - k = N - k

for k in ks:
    ways_rows_k = comb(a - 1, k - 1) * comb(N - a, N - k) % MOD
    ways_cols_k = comb(b - 1, k - 1) * comb(N - b, N - k) % MOD
    print(ways_rows_k * ways_cols_k % MOD)