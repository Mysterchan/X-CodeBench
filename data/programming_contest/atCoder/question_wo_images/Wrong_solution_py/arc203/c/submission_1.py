import sys
I = lambda : [*map(int, sys.stdin.readline().split())]
tt = I()[0]
out = []
MAXN = 400005
mod = 998244353
inv2 = (mod + 1) // 2
fact = [1]
for i in range(1, MAXN): fact.append(fact[-1] * i % mod)
factInv = [0] * MAXN
factInv[-1] = pow(fact[-1], -1, mod)
for i in range(MAXN - 2, -1, -1): factInv[i] = factInv[i + 1] * (i + 1) % mod
def C(n, k):
    if n < k or n < 0 or k < 0: return 0
    return fact[n] * factInv[k] % mod * factInv[n - k] % mod
p2 = [1]
for i in range(1, MAXN): p2.append(p2[-1] * 2 % mod)
for _ in range(tt):
    h, w, k = I()
    if k < h + w - 2: out.append(0); continue
    elif k == h + w - 2: out.append(C(h + w - 2, h - 1)); continue
    elif k == h + w - 1: rem = (h - 1) * w + (w - 1) * h - (h + w - 2); rem %= mod; out.append(C(h + w - 2, h - 1) * rem % mod); continue
    else:
        assert k == h + w
        rem = (h - 1) * w + (w - 1) * h - (h + w - 2) ; rem %= mod
        tot = C(h + w - 2, h - 1) * rem % mod * (rem - 1 + mod) % mod * inv2 % mod
        print(tot)
        sub = (h + w - 3) * C(h + w - 4, h - 2) % mod
        tot = (tot - sub + mod) % mod
        print(tot)

        tot += (h - 1) * C(h + w - 2, h + 1) + (w - 1) * C(h + w - 2, w + 1); tot %= mod
        out.append(tot)
print('\n'.join([str(i) for i in out]))