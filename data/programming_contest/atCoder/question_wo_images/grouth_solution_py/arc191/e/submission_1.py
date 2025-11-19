import sys
from functools import lru_cache

import numpy as np

sys.setrecursionlimit(10**6)
MOD = 998244353

def dprint(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

N, X, Y = map(int, input().split())
X %= 2
Y %= 2

facts = [1] * (N + 1)
factinvs = [1] * (N + 1)
for i in range(1, N + 1):
    facts[i] = facts[i - 1] * i % MOD

factinvs[N] = pow(facts[N], MOD - 2, MOD)
for i in range(N - 1, 0, -1):
    factinvs[i] = factinvs[i + 1] * (i + 1) % MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return facts[n] * factinvs[k] * factinvs[n - k] % MOD

@lru_cache(maxsize=None)
def test(a, b, turn):
    if a == 0 and b == 0:
        return False
    if b > 0 and not test(a, b - 1, 1 - turn):
        return True
    if turn == 0:
        if a > 0 and not test(a - 1, b + X, 1 - turn):
            return True
    else:
        if a > 0 and not test(a - 1, b + Y, 1 - turn):
            return True
    return False

res = []
for i in range(N):
    a, b = map(int, input().split())
    b %= 2
    if a > 3:
        if a % 2 == 0:
            a = 4
        else:
            a = 3
    first = test(a, b, 0) * 1
    second = -test(a, b, 1) * 1
    res.append((first, second))
zeros = 0
ones = 0
twos = 0
req = 0
for a, b in res:
    d = a - b
    if d == 0:
        zeros += 1
    elif d == 1:
        ones += 1
    elif d == 2:
        twos += 1
    req += -b

one_select = [comb(ones, i) for i in range(ones + 1)]
two_select = [comb(twos, i // 2) if i % 2 == 0 else 0 for i in range(2 * twos + 1)]
one_select_cumsum = [0] * (ones + 2)
for i in range(ones + 1):
    one_select_cumsum[i + 1] = one_select_cumsum[i] + one_select[i]
ans = 0
for i in range(len(two_select)):
    one_minimum = max(0, req + 1 - i)
    if one_minimum > ones:
        continue
    ans += two_select[i] * (one_select_cumsum[-1] - one_select_cumsum[one_minimum])
    ans %= MOD
ans %= MOD
ans *= pow(2, zeros, MOD)
ans %= MOD
print(ans)