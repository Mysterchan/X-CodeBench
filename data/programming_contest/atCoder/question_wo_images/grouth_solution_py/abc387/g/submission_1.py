from math import ceil, log2
import sys
input = sys.stdin.readline

MOD = 998_244_353
primitive_root = 3

class Polynomial:
    def __init__(self, size, arr):
        self.size = size
        self.coef = arr[:size]
        while len(self.coef) < size:
            self.coef.append(0)

    def __getitem__(self, item):
        return self.coef[item]

    def __setitem__(self, key, value):
        self.coef[key] = value

    def __str__(self):
        return ' '.join(map(str, self.coef))

    def __add__(self, other):
        arr = [(self[i] + other[i]) % MOD for i in range(self.size)]
        return Polynomial(self.size, arr)

    def __sub__(self, other):
        arr = [(self[i] - other[i]) % MOD for i in range(self.size)]
        return Polynomial(self.size, arr)

    @staticmethod
    def _ntt(ret, omega):
        n = len(ret)
        reverse = [0] * n
        for i in range(n):
            reverse[i] = reverse[i >> 1] >> 1
            if i & 1 == 1:
                reverse[i] |= n >> 1
            if i < reverse[i]:
                ret[i], ret[reverse[i]] = ret[reverse[i]], ret[i]

        root = [1]
        for _ in range(n - 1):
            root.append(root[-1] * omega % MOD)

        i = 2
        while i <= n:
            for j in range(0, n, i):
                for k in range(i >> 1):
                    even, odd = ret[j | k], ret[j | k | i >> 1] * root[n // i * k] % MOD
                    ret[j | k] = (even + odd) % MOD
                    ret[j | k | i >> 1] = (even - odd) % MOD
            i <<= 1

        return ret

    def __mul__(self, other):
        n = 1 << ceil(log2(self.size)) + 1
        a, b = self.coef.copy(), other.coef.copy()
        while len(a) < n:
            a.append(0)
            b.append(0)
        omega = pow(primitive_root, (MOD - 1) // n, MOD)
        A = self._ntt(a, omega)
        B = self._ntt(b, omega)
        C = [A[i] * B[i] % MOD for i in range(n)]
        c = self._ntt(C, pow(omega, -1, MOD))
        inv = pow(n, -1, MOD)
        for i in range(len(c)):
            c[i] = c[i] * inv % MOD
        return Polynomial(self.size, c)

    def __pow__(self, power, modulo=MOD):
        if power == -1:
            g = Polynomial(2, [pow(self[0], -1, MOD)])
            while g.size < self.size << 1:
                n = g.size
                f = Polynomial(n, self.coef)
                g = (Polynomial(n, [2]) - g * f) * g
                g = Polynomial(2 * n, g.coef)
            return Polynomial(self.size, g.coef)
        raise ValueError

    def __truediv__(self, other):
        return self * pow(other, -1)

    def __floordiv__(self, other):
        f, g = self.coef.copy(), other.coef.copy()
        while f[-1] == 0:
            f.pop()
        while g[-1] == 0:
            g.pop()
        F = Polynomial(self.size, f[::-1])
        G = Polynomial(self.size, g[::-1])
        return Polynomial(self.size, (F / G).coef[:len(f) - len(g) + 1][::-1])

    def __mod__(self, other):
        return self - (self // other) * other

    def derivative(self):
        ret = Polynomial(self.size, [0])
        for i in range(self.size - 1):
            ret[i] = self[i + 1] * (i + 1) % MOD
        return ret

    def integral(self, const):
        ret = Polynomial(self.size, [0])
        ret[0] = const
        for i in range(1, self.size):
            ret[i] = self[i - 1] * pow(i, -1, MOD) % MOD
        return ret

    def log(self):
        assert self[0] == 1
        return (self.derivative() / self).integral(0)

    def exp(self):
        g = Polynomial(2, [1])
        while g.size < self.size << 1:
            n = g.size
            f = Polynomial(n, self.coef)
            f[0] += 1
            g = (f - g.log()) * g
            g = Polynomial(2 * n, g.coef)
        return Polynomial(self.size, g.coef)

n=int(input())

if n==1:
  print(1)
  exit()

M=998244353
N=n
fa=[1]
for i in range(1,N+1):
  fa+=[fa[-1]*i%M]
fb=[pow(fa[N],M-2,M)]
for i in reversed(range(1,N+1)):
  fb+=[fb[-1]*i%M]
fb.reverse()
fc=lambda n,k:fa[n]*fb[k]*fb[n-k]%M if n>=k>=0 else 0

p=[1]*(n+1)
p[0]=0
for i in range(2,n+1):
  if p[i]:
    for j in range(i+i,n+1,i):
      p[j]=0
p[2]=0
p=[i for i in range(n+1) if p[i]]

q=[0]*(n+1)
for i in p:
  q[i]=fa[i-1]*(fb[2] if i>1 else 1)*i*n*fb[i]
print(fa[n]*Polynomial(n+1,q).exp()[n]*pow(n*n,M-2,M)%M)