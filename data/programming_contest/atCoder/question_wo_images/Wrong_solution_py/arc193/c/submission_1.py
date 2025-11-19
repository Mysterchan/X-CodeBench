def pow_mod(a, b, mod):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

mod = 998244353
h, w, c = map(int, input().split())

if h == 1 or w == 1:
    print(pow_mod(c, h * w, mod))
else:
    print((pow_mod(c, h + w - 1, mod) - pow_mod(c, max(h, w) - 1, mod) + mod) * c % mod)