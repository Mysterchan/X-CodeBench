MOD = 998244353

MAX_N = 2 * (10**7)
factorial = [1] * (MAX_N + 1)
inv_factorial = [1] * (MAX_N + 1)

for i in range(1, MAX_N + 1):
    factorial[i] = (factorial[i - 1] * i) % MOD

def modinv(x):
    return pow(x, MOD - 2, MOD)

inv_factorial[MAX_N] = modinv(factorial[MAX_N])
for i in range(MAX_N, 0, -1):
    inv_factorial[i - 1] = (inv_factorial[i] * i) % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return factorial[n] * inv_factorial[k] % MOD * inv_factorial[n - k] % MOD

def solve(N, a, b, ks):
    results = []
    max_k = max(ks)

    for k in ks:

        total_row_intervals = N - 1
        intervals_needed = max_k
        ways_rows = comb(total_row_intervals, intervals_needed - 1)

        total_col_intervals = N - 1
        ways_cols = comb(total_col_intervals, intervals_needed - 1)

        ways_rows_k = comb(a - 1, k - 1) * comb(N - a, intervals_needed - k) % MOD
        ways_cols_k = comb(b - 1, k - 1) * comb(N - b, intervals_needed - k) % MOD

        total_ways = ways_rows_k * ways_cols_k % MOD

        results.append(total_ways)
    return results

N, Q = map(int, input().split())
a, b = map(int, input().split())
ks = list(map(int, input().split()))

results = solve(N, a, b, ks)
for res in results:
    print(res)