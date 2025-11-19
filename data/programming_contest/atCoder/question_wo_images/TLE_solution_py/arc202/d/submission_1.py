mod = 998244353
table_size = 10**6

fac = [1] * (table_size + 1)
finv = [1] * (table_size + 1)

for i in range(2, table_size + 1):
    fac[i] = fac[i - 1] * i % mod
finv[table_size] = pow(fac[table_size], mod - 2, mod)
for i in range(table_size - 1, -1, -1):
    finv[i] = finv[i + 1] * (i + 1) % mod

def rebuild(n):
    global table_size, fac, finv
    fac += [0] * (n - table_size)
    fac += [0] * (n - table_size)
    finv += [0] * (n - table_size)
    for i in range(table_size + 1, n + 1):
        fac[i] = fac[i - 1] * i % mod
    finv[n] = inv(fac[n])
    for i in range(n - 1, table_size, -1):
        finv[i] = finv[i + 1] * (i + 1) % mod
    table_size = n

def binom(n, k):
    if n < 0 or k < 0:
        return 0
    if k > n:
        return 0
    if n > table_size:
        rebuild(n + 10**4)
    return (fac[n] * finv[k] % mod) * finv[n - k] % mod

def fpow(x, k):
    res = 1
    while k:
        if k & 1:
            res = res * x % mod
        x = x * x % mod
        k >>= 1
    return res

def inv(a):
    if a < table_size:
        return fac[a - 1] * finv[a] % mod
    return fpow(a, mod - 2)

from collections import defaultdict

def naive1(T, N, S, G):
    if not (0 <= S <= N):
        return 0
    if not (0 <= G <= N):
        return 0

    d = defaultdict(int)
    d[S] = 1
    for _ in range(T):
        nd = defaultdict(int)
        for x in d:
            if 0 <= x + 1 <= N:
                nd[x + 1] += d[x]
            if 0 <= x - 1 <= N:
                nd[x - 1] += d[x]
        d = nd
    return d[G] % mod

def calc1_sub(N, M, K, L):
    P = N + M - K - L + 2
    res = 0
    for k in range(-(10**5), 10**5):
        res += binom(N + M, N + k * P) - binom(N + M, K - 1 + k * P)
    return res % mod

def calc1(T, N, S, G):
    if not (0 <= S <= N):
        return 0
    if not (0 <= G <= N):
        return 0
    if (T + (S - G)) & 1:
        return 0
    H = (T + S - G) // 2
    W = (T - (S - G)) // 2
    K = H - S
    L = W - N + S
    return calc1_sub(H, W, K, L)

H, W, T, A, B, C, D = map(int, input().split())

resX = [0] * (T + 1)
resY = [0] * (T + 1)
for t in range(T + 1):
    resX[t] = calc1(t, H - 1, A - 1, C - 1)
    resY[t] = calc1(t, W - 1, B - 1, D - 1)

ans = 0
sgn = 1
for i in range(T, 0, -1):
    X = 0
    Y = 0
    for j in range(i, 0, -1):
        X += resX[j] * binom(i, j)
        Y += resY[j] * binom(i, j)
        X %= mod
        Y %= mod
    ans += sgn * X * Y % mod * binom(T, i)
    ans %= mod
    sgn = -sgn

print(ans)