import os
import sys

import numpy as np

def solve(inp):
    MOD = 998244353

    def fzt(aaa, k):

        n = 1 << k
        for i in range(k):
            bit = 1 << i
            for mask in range(n):
                if mask & bit:
                    aaa[mask] += aaa[mask ^ bit]
        for i in range(n):
            aaa[i] %= MOD

    def fmt(aaa, k):

        n = 1 << k
        for i in range(k):
            bit = 1 << i
            for mask in range(n):
                if mask & bit:
                    aaa[mask] -= aaa[mask ^ bit]
        for i in range(n):
            aaa[i] %= MOD

    n, m = inp[:2]
    sss = inp[2:]

    aaa = np.zeros(1 << n, np.int64)
    for s in sss:
        aaa[s] += 1

    for i in range(n):
        k = n - i - 1
        size = 1 << k
        bbb = np.zeros(size, np.int64)
        ccc = np.zeros(size, np.int64)
        ddd = np.zeros(size, np.int64)

        for j in range(size << 1):
            j1 = j >> 1
            if aaa[j]:
                if j & 1:
                    bbb[j1] += aaa[j]
                    bbb[j1] %= MOD
                else:
                    ccc[j1] += aaa[j]
                    ccc[j1] %= MOD
                ddd[j1] += aaa[j]
                ddd[j1] %= MOD

        fzt(ccc, k)
        fzt(ddd, k)
        for j in range(size):
            ccc[j] *= ddd[j]
            ccc[j] %= MOD
        fmt(ccc, k)

        for j in range(size):
            aaa[j] = (bbb[j] + ccc[j]) % MOD
        aaa = aaa[:size]

    return aaa[0]

SIGNATURE = '(i8[:],)'
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

inp = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
ans = solve(inp)
print(ans)