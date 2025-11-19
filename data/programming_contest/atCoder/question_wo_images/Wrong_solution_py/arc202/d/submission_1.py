from sys import stdin
input = lambda: stdin.readline().rstrip()
MOD = 998244353

G = 3

def ntt(a, inv):
    n = len(a)
    rev = [0] * n
    for i in range(n):
        rev[i] = (rev[i >> 1] >> 1) | ((i & 1) * (n >> 1))
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]

    i = 1
    while i < n:
        wn = pow(G, (MOD - 1) // (i * 2), MOD)
        if inv == -1:
            wn = pow(wn, MOD - 2, MOD)
        j = 0
        while j < n:
            w = 1
            for k in range(i):
                x = a[j + k]
                y = w * a[j + k + i] % MOD
                a[j + k] = (x + y) % MOD
                a[j + k + i] = (x - y) % MOD
                w = w * wn % MOD
            j += i * 2
        i *= 2

    if inv == -1:
        n_inv = pow(n, -1, MOD)
        for i in range(n):
            a[i] = a[i] * n_inv % MOD

def p_mul(a, b, deg=0):
    if deg == 0:
        deg = len(a) + len(b) - 1
    n = 1
    while n < len(a) + len(b):
        n *= 2
    fa = a[:] + [0] * (n - len(a))
    fb = b[:] + [0] * (n - len(b))

    ntt(fa, 1)
    ntt(fb, 1)
    for i in range(n):
        fa[i] = fa[i] * fb[i] % MOD
    ntt(fa, -1)
    return fa[:deg]

def p_inv(f, deg):
    if deg == 1:
        return [pow(f[0], -1, MOD)]
    inv_f_half = p_inv(f, (deg + 1) // 2)
    f_ntt = f[:deg]
    n = 1
    while n < deg * 2:
        n *= 2
    f_ntt.extend([0] * (n - len(f_ntt)))
    inv_f_ntt = inv_f_half + [0] * (n - len(inv_f_half))

    ntt(f_ntt, 1)
    ntt(inv_f_ntt, 1)
    for i in range(n):
        inv_f_ntt[i] = (2 - f_ntt[i] * inv_f_ntt[i] % MOD + MOD) * inv_f_ntt[i] % MOD
    ntt(inv_f_ntt, -1)
    return inv_f_ntt[:deg]

def p_sqrt(f, deg):
    if deg == 1:
        return [1]
    sqrt_f_half = p_sqrt(f, (deg + 1) // 2)
    inv_sqrt_f = p_inv(sqrt_f_half, deg)
    f_deg = f[:deg]
    term = p_mul(f_deg, inv_sqrt_f, deg)
    res = sqrt_f_half + [0] * (deg - len(sqrt_f_half))
    two_inv = pow(2, MOD - 2, MOD)
    for i in range(deg):
        res[i] = (res[i] + term[i]) * two_inv % MOD
    return res

def p_pow(f, k, deg):
    res = [1]
    base = f[:]
    while k > 0:
        if k & 1:
            res = p_mul(res, base, deg)
        base = p_mul(base, base, deg)
        k >>= 1
    res.extend([0] * (deg - len(res)))
    return res

MX = 300001
fact = [1] * (MX + 1)
invf = [1] * (MX + 1)
for i in range(1, MX + 1):
    fact[i] = fact[i - 1] * i % MOD

invf[MX] = pow(fact[MX], -1, MOD)
for i in range(MX - 1, -1, -1):
    invf[i] = invf[i + 1] * (i + 1) % MOD

memo = {}
def get_n(d, tmax):
    d = abs(d)
    if (d, tmax) in memo:
        return memo[(d, tmax)]
    deg = tmax + 1
    poly_p = [1, -2, -3]
    sqrt_p = p_sqrt(poly_p, deg)
    inv_sqrt_p = p_inv(sqrt_p, deg)
    r1_num = [0] * deg
    r1_num[0] = (1 - sqrt_p[0]) % MOD
    r1_num[1] = (-1 - sqrt_p[1]) % MOD
    for i in range(2, deg):
        r1_num[i] = (-sqrt_p[i]) % MOD
    two_inv = pow(2, -1, MOD)
    r1 = [0] * deg
    for i in range(deg - 1):
        r1[i] = r1_num[i + 1] * two_inv % MOD
    r1[deg - 1] = 0
    if d == 0:
        res = inv_sqrt_p
    else:
        pow_r1 = p_pow(r1, d, deg)
        res = p_mul(pow_r1, inv_sqrt_p, deg)
    memo[(d, tmax)] = res
    return res

def get_f(lim, tmax, sta, end):
    dists = []
    limp1 = lim + 1
    dists.append((end - sta, 1))
    dists.append((2 * limp1 - end - sta, -1))

    for k in range(1, tmax + 2):
        new = False
        d1 = end - sta + 2 * k * limp1
        d2 = 2 * limp1 - end - sta + 2 * k * limp1
        if abs(d1) <= tmax:
            dists.append((d1, 1))
            new = True
        if abs(d2) <= tmax:
            dists.append((d2, -1))
            new = True

        d3 = end - sta - 2 * k * limp1
        d4 = 2 * limp1 - end - sta - 2 * k * limp1
        if abs(d3) <= tmax:
            dists.append((d3, 1))
            new = True
        if abs(d4) <= tmax:
            dists.append((d4, -1))
            new = True

        if not new:
            break
    t_ser = [0] * (tmax + 1)
    for d, sgn in dists:
        n_ser = get_n(d, tmax)
        for i in range(tmax + 1):
            term = sgn * n_ser[i]
            t_ser[i] = (t_ser[i] + term + MOD) % MOD
    return t_ser

def solve():
    h, w, t, a, b, c, d = map(int, input().split())
    wx_vals = get_f(w, t, b, d)
    hy_vals = get_f(h, t, a, c)
    ans = 0
    for i in range(t + 1):
        ways9_i = (wx_vals[i] * hy_vals[i]) % MOD
        comb = fact[t] * invf[i] % MOD * invf[t - i] % MOD
        term = comb * ways9_i % MOD
        if (t - i) % 2 == 1:
            ans = (ans - term + MOD) % MOD
        else:
            ans = (ans + term) % MOD
    return ans

print(solve())