import numpy as np
from numba import njit

@njit('(i8,i8,i8)')
def solve(h, w, c):
    MOD = 998244353

    def mod_pow(x, a, MOD):
        ret = 1
        cur = x
        while a > 0:
            if a & 1:
                ret = ret * cur % MOD
            cur = cur * cur % MOD
            a >>= 1
        return ret

    def prepare_factorials(n, MOD):
        factorials = np.ones(n + 1, np.int64)
        for m in range(1, n + 1):
            factorials[m] = factorials[m - 1] * m % MOD
        inversions = np.ones(n + 1, np.int64)
        inversions[n] = mod_pow(factorials[n], MOD - 2, MOD)
        for m in range(n, 1, -1):
            inversions[m - 1] = inversions[m] * m % MOD
        return factorials, inversions

    n = max(h, w)
    facts, finvs = prepare_factorials(n, MOD)
    ncr = np.zeros((n + 1, n + 1), np.int64)
    for i in range(n + 1):
        for j in range(i + 1):
            ncr[i, j] = facts[i] * finvs[j] % MOD * finvs[i - j] % MOD

    pow_c = np.ones((n + 1, 2), np.int64)
    for i in range(1, n + 1):
        pow_c[i, 0] = pow_c[i - 1, 0] * c % MOD
        pow_c[i, 1] = pow_c[i - 1, 1] * (c - 1) % MOD

    dp = np.zeros((h + 1, w + 1, 2, 2), np.int64)
    for i in range(h):
        for j in range(w):
            if i > j and 0 <= j < h and 0 <= i < w:
                dp[i, j, 0, :] = dp[j, i, 1, :]
                dp[i, j, 1, :] = dp[j, i, 0, :]
                continue

            for l in (0, 1):
                use_color = c - l
                if j == 0:
                    dp[i, j, 0, l] = 1
                else:
                    result = 0
                    for ii in range(1, i + 1):
                        coloring = dp[i - ii, j, 1, 0] * (pow_c[ii, l] - use_color) % MOD
                        if ii < i:
                            coloring += dp[i - ii, j, 1, 1] * use_color
                            coloring %= MOD
                        result += ncr[i, ii] * coloring
                        result %= MOD
                    dp[i, j, 0, l] = result

                if i == 0:
                    dp[i, j, 1, l] = 1
                else:
                    result = 0
                    for jj in range(1, j + 1):
                        coloring = dp[i, j - jj, 0, 0] * (pow_c[jj, l] - use_color) % MOD
                        if jj < j:
                            coloring += dp[i, j - jj, 0, 1] * use_color
                            coloring %= MOD
                        result += ncr[j, jj] * coloring
                        result %= MOD
                    dp[i, j, 1, l] = result

    result = 1
    for i in range(1, h):
        for j in range(1, w):
            for k in range(w - j + 1):
                choice = ncr[h, i] * ncr[w, j] % MOD * ncr[w - j, k] % MOD
                coloring = choice * pow_c[k, 1] % MOD
                l = 1 if k == 0 else 0
                result += coloring * dp[h - i, w - j - k, 0, l]
                result %= MOD

    result *= c
    result %= MOD
    return result

h, w, c = map(int, input().split())
ans = solve(h, w, c)
print(ans)