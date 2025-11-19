import sys
input = lambda: sys.stdin.readline().strip()

class PermComb():
    def __init__(self, mod):
        self.mod = mod
        self.size = 1
        self.fact = [1, 1]
        self.inv = [0, 1]
        self.finv = [1, 1]
    def extend(self, n):
        for i in range(self.size + 1, n + 1):
            self.fact.append(self.fact[-1] * i % self.mod)
            self.inv.append(self.mod - self.inv[self.mod % i] * (self.mod // i) % self.mod)
            self.finv.append(self.finv[-1] * self.inv[i] % self.mod)
        self.size = n
    def calc_fact(self, n):
        if n > self.size:
            self.extend(n)
        return self.fact[n]
    def calc_inv(self, n):
        if n > self.size:
            self.extend(n)
        return self.inv[n]
    def calc_finv(self, n):
        if n > self.size:
            self.extend(n)
        return self.finv[n]
    def perm(self, n, k):
        if n < 0 or k < 0 or n < k: return 0
        if n == 0 or k == 0: return 1
        if n > self.size:
            self.extend(n)
        return self.fact[n] * self.finv[n - k] % self.mod
    def comb(self, n, k):
        if n < 0 or k < 0 or n < k: return 0
        if n == 0 or k == 0: return 1
        if n > self.size:
            self.extend(n)
        return self.fact[n] * self.finv[k] % self.mod * self.finv[n - k] % self.mod
    def comb_with_replacement_count(self, n, k):
        return self.comb(n + k - 1, k)

mod = 998244353
pc = PermComb(mod)
inv2 = pow(2, -1, mod)

t = int(input())
for _ in range(t):
    h, w, k = map(int, input().split())
    b = pc.comb(h + w - 2, h - 1)
    r = h * (w - 1) + (h - 1) * w - (h + w - 2)
    if k < h + w - 2:
        print(0)
    elif k == h + w - 2:
        print(b)
    elif k == h + w - 1:
        print(b * r % mod)
    else:
        term1 = (b * r * (r - 1) * inv2 - pc.comb(h + w - 4, h - 2) * (h + w - 3)) % mod
        term2 = pc.comb(h + w - 2, w - 3) * (h - 1) % mod
        term3 = pc.comb(h + w - 2, h - 3) * (w - 1) % mod
        print((term1 + term2 + term3) % mod)