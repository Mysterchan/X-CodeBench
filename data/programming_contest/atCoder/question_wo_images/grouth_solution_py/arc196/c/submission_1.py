import os
import sys

import numpy as np

def solve(n, s):
    MOD = 998244353
    SUM_E = np.array(
        [911660635, 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924, 603855026, 856644456,
         131300601, 842657263, 730768835, 942482514, 806263778, 151565301, 510815449, 503497456, 743006876, 741047443,
         56250497, 867605899, 0, 0, 0, 0, 0, 0, 0, 0], np.int64)
    SUM_IE = np.array(
        [86583718, 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860, 90816748, 860285882,
         927414960, 354738543, 109331171, 293255632, 535113200, 308540755, 121186627, 608385704, 438932459, 359477183,
         824071951, 103369235, 0, 0, 0, 0, 0, 0, 0, 0], np.int64)

    def bit_length(n):
        x = 0
        while 1 << x < n:
            x += 1
        return x

    def bit_scan_forward(n):
        x = 0
        while n & 1 == 0:
            n >>= 1
            x += 1
        return x

    def pow_mod(x, n, m):
        r = 1
        y = x % m
        while n > 0:
            if n & 1 == 1:
                r = (r * y) % m
            y = y * y % m
            n >>= 1
        return r

    def butterfly(aaa):
        n = aaa.size
        h = bit_length(n)

        for ph in range(1, h + 1):
            w = 1 << (ph - 1)
            p = 1 << (h - ph)
            now = 1
            for s in range(w):
                offset = s << (h - ph + 1)
                for i in range(p):
                    l = aaa[i + offset]
                    r = aaa[i + offset + p] * now % MOD
                    aaa[i + offset] = (l + r) % MOD
                    aaa[i + offset + p] = (l - r) % MOD
                now = now * SUM_E[bit_scan_forward(~s)] % MOD

    def butterfly_inv(aaa):
        n = aaa.size
        h = bit_length(n)

        for ph in range(h, 0, -1):
            w = 1 << (ph - 1)
            p = 1 << (h - ph)
            inow = 1
            for s in range(w):
                offset = s << (h - ph + 1)
                for i in range(p):
                    l = aaa[i + offset]
                    r = aaa[i + offset + p]
                    aaa[i + offset] = (l + r) % MOD
                    aaa[i + offset + p] = ((l - r) * inow) % MOD
                inow = inow * SUM_IE[bit_scan_forward(~s)] % MOD

    def ntt(aaa, bbb):
        n = aaa.size
        m = bbb.size
        k = n + m - 1
        z = 1 << bit_length(k)
        raaa = np.zeros(z, np.int64)
        rbbb = np.zeros(z, np.int64)
        raaa[:n] = aaa
        rbbb[:m] = bbb
        butterfly(raaa)
        butterfly(rbbb)
        for i in range(z):
            raaa[i] = raaa[i] * rbbb[i] % MOD
        butterfly_inv(raaa)
        iz = pow_mod(z, MOD - 2, MOD)
        for i in range(k):
            raaa[i] = raaa[i] * iz % MOD
        return raaa[:k]

    def mod_pow(x, a, MOD):
        ret = 1
        cur = x
        while a > 0:
            if a & 1 == 1:
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

    if s[0] != 0 or s[-1] != 1:
        return 0

    facts, finvs = prepare_factorials(n * 2, MOD)

    b_cnt = np.zeros(n * 2 + 1, np.int64)
    for i in range(n * 2):
        if s[i] == 0:
            b_cnt[i + 1] = b_cnt[i] + 1
        else:
            b_cnt[i + 1] = b_cnt[i]
    w_cnt = np.arange(n * 2 + 1, dtype=np.int64)
    w_cnt -= b_cnt

    dp = np.zeros(n * 2 + 1, np.int64)

    def bruteforce(l, r):
        for i in range(l, r - 1):
            for j in range(i + 1, r):
                b = b_cnt[j] - b_cnt[i]
                w = j - b_cnt[i] - b_cnt[j]
                if b > w:
                    continue
                c = facts[w] * finvs[w - b] % MOD
                dp[j] -= c * dp[i]
                dp[j] %= MOD

    dp[0] = -1
    tasks = [(0, n * 2 + 1, -1)]
    while len(tasks) > 0:
        l, r, m = tasks.pop()
        if m == -1:
            if r - l < 500:
                bruteforce(l, r)
                continue
            m = (l + r) // 2
            tasks.append((m, r, -1))
            tasks.append((l, r, m))
            tasks.append((l, m, -1))
        else:
            bc = b_cnt[m] - b_cnt[l]
            fff = np.zeros(bc + 1, np.int64)
            for i in range(l, m):
                key = b_cnt[i] - b_cnt[l]
                fff[key] += dp[i]
            ggg = facts[:(r - l) * 2]
            hhh = ntt(fff, ggg)
            for i in range(m, r):
                wb = w_cnt[i] - b_cnt[i]
                if wb < 0:
                    continue
                dp[i] -= hhh[w_cnt[i] - b_cnt[l]] * finvs[wb] % MOD
                dp[i] %= MOD

    return dp[n * 2]

SIGNATURE = '(i8,i1[:])'
if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    cc = CC('my_module')
    cc.export('solve', SIGNATURE)(solve)
    cc.compile()
    exit()

if os.name == 'posix':

    from my_module import solve
else:
    from numba import njit

    solve = njit(SIGNATURE, cache=True)(solve)
    print('compiled', file=sys.stderr)

n = int(input())
s = np.fromiter(map('BW'.index, input()), dtype=np.int8)
ans = solve(n, s)
print(ans)