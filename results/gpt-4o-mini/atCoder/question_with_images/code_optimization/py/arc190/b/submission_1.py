MOD = 998244353

def modinv(x):
    return pow(x, MOD - 2, MOD)

def compute_factorials(max_n):
    factorial = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        factorial[i] = factorial[i - 1] * i % MOD
    return factorial

def comb(n, k, factorial, inv_factorial):
    if k < 0 or k > n:
        return 0
    return factorial[n] * inv_factorial[k] % MOD * inv_factorial[n - k] % MOD

def solve(N, a, b, ks):
    max_k = max(ks)
    factorial = compute_factorials(N)
    inv_factorial = [1] * (N + 1)
    inv_factorial[N] = modinv(factorial[N])
    for i in range(N - 1, 0, -1):
        inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD

    results = []
    for k in ks:
        total_row_intervals = N - 1
        ways_rows = comb(total_row_intervals, max_k - 1, factorial, inv_factorial)

        ways_rows_k = comb(a - 1, k - 1, factorial, inv_factorial) * comb(N - a, max_k - k) % MOD
        ways_cols_k = comb(b - 1, k - 1, factorial, inv_factorial) * comb(N - b, max_k - k) % MOD

        total_ways = ways_rows * ways_rows_k % MOD * ways_cols_k % MOD
        results.append(total_ways)
    return results

N, a, b = map(int, input().split())
Q = int(input())
ks = list(map(int, input().split()))

results = solve(N, a, b, ks)
for res in results:
    print(res)