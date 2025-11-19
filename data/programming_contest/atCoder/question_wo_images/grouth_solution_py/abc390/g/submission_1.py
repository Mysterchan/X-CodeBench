p=998244353
N=int(input())
class FFT():
    def bsf(self, x):
        res = 0
        while (x % 2 == 0):
            res += 1
            x //= 2
        return res
    rank2 = 0
    root = []
    iroot = []
    rate2 = []
    irate2 = []
    rate3 = []
    irate3 = []
    def __init__(self, MOD):
        self.mod = MOD
        self.g = 3
        self.rank2 = self.bsf(self.mod - 1)
        self.root = [0 for i in range(self.rank2 + 1)]
        self.iroot = [0 for i in range(self.rank2 + 1)]
        self.rate2 = [0 for i in range(self.rank2)]
        self.irate2 = [0 for i in range(self.rank2)]
        self.rate3 = [0 for i in range(self.rank2 - 1)]
        self.irate3 = [0 for i in range(self.rank2 - 1)]
        self.root[self.rank2] = pow(self.g, (self.mod - 1) >> self.rank2,
                                    self.mod)
        self.iroot[self.rank2] = pow(self.root[self.rank2], self.mod - 2,
                                     self.mod)
        for i in range(self.rank2 - 1, -1, -1):
            self.root[i] = (self.root[i + 1] ** 2) % self.mod
            self.iroot[i] = (self.iroot[i + 1] ** 2) % self.mod
        prod = 1;
        iprod = 1
        for i in range(self.rank2 - 1):
            self.rate2[i] = (self.root[i + 2] * prod) % self.mod
            self.irate2[i] = (self.iroot[i + 2] * iprod) % self.mod
            prod = (prod * self.iroot[i + 2]) % self.mod
            iprod = (iprod * self.root[i + 2]) % self.mod
        prod = 1;
        iprod = 1
        for i in range(self.rank2 - 2):
            self.rate3[i] = (self.root[i + 3] * prod) % self.mod
            self.irate3[i] = (self.iroot[i + 3] * iprod) % self.mod
            prod = (prod * self.iroot[i + 3]) % self.mod
            iprod = (iprod * self.root[i + 3]) % self.mod

    def butterfly(self, a):
        n = len(a)
        h = (n - 1).bit_length()

        LEN = 0
        while (LEN < h):
            if (h - LEN == 1):
                p = 1 << (h - LEN - 1)
                rot = 1
                for s in range(1 << LEN):
                    offset = s << (h - LEN)
                    for i in range(p):
                        l = a[i + offset]
                        r = a[i + offset + p] * rot
                        a[i + offset] = (l + r) % self.mod
                        a[i + offset + p] = (l - r) % self.mod
                    rot *= self.rate2[(~s & -~s).bit_length() - 1]
                    rot %= self.mod
                LEN += 1
            else:
                p = 1 << (h - LEN - 2)
                rot = 1
                imag = self.root[2]
                for s in range(1 << LEN):
                    rot2 = (rot * rot) % self.mod
                    rot3 = (rot2 * rot) % self.mod
                    offset = s << (h - LEN)
                    for i in range(p):
                        a0 = a[i + offset]
                        a1 = a[i + offset + p] * rot
                        a2 = a[i + offset + 2 * p] * rot2
                        a3 = a[i + offset + 3 * p] * rot3
                        a1na3imag = (a1 - a3) % self.mod * imag
                        a[i + offset] = (a0 + a2 + a1 + a3) % self.mod
                        a[i + offset + p] = (a0 + a2 - a1 - a3) % self.mod
                        a[i + offset + 2 * p] = (
                                                        a0 - a2 + a1na3imag) % self.mod
                        a[i + offset + 3 * p] = (
                                                        a0 - a2 - a1na3imag) % self.mod
                    rot *= self.rate3[(~s & -~s).bit_length() - 1]
                    rot %= self.mod
                LEN += 2

    def butterfly_inv(self, a):
        n = len(a)
        h = (n - 1).bit_length()
        LEN = h
        while (LEN):
            if (LEN == 1):
                p = 1 << (h - LEN)
                irot = 1
                for s in range(1 << (LEN - 1)):
                    offset = s << (h - LEN + 1)
                    for i in range(p):
                        l = a[i + offset]
                        r = a[i + offset + p]
                        a[i + offset] = (l + r) % self.mod
                        a[i + offset + p] = (l - r) * irot % self.mod
                    irot *= self.irate2[(~s & -~s).bit_length() - 1]
                    irot %= self.mod
                LEN -= 1
            else:
                p = 1 << (h - LEN)
                irot = 1
                iimag = self.iroot[2]
                for s in range(1 << (LEN - 2)):
                    irot2 = (irot * irot) % self.mod
                    irot3 = (irot * irot2) % self.mod
                    offset = s << (h - LEN + 2)
                    for i in range(p):
                        a0 = a[i + offset]
                        a1 = a[i + offset + p]
                        a2 = a[i + offset + 2 * p]
                        a3 = a[i + offset + 3 * p]
                        a2na3iimag = (a2 - a3) * iimag % self.mod
                        a[i + offset] = (a0 + a1 + a2 + a3) % self.mod
                        a[i + offset + p] = (
                                                    a0 - a1 + a2na3iimag) * irot % self.mod
                        a[i + offset + 2 * p] = (
                                                        a0 + a1 - a2 - a3) * irot2 % self.mod
                        a[i + offset + 3 * p] = (
                                                        a0 - a1 - a2na3iimag) * irot3 % self.mod
                    irot *= self.irate3[(~s & -~s).bit_length() - 1]
                    irot %= self.mod
                LEN -= 2

    def convolution(self, a, b):
        n = len(a);
        m = len(b)
        if not (a) or not (b):
            return []
        if min(n, m) <= 40:
            res = [0] * (n + m - 1)
            for i in range(n):
                for j in range(m):
                    res[i + j] += a[i] * b[j]
                    res[i + j] %= self.mod
            return res
        z = 1 << ((n + m - 2).bit_length())
        a = a + [0] * (z - n)
        b = b + [0] * (z - m)
        self.butterfly(a)
        self.butterfly(b)
        c = [(a[i] * b[i]) % self.mod for i in range(z)]
        self.butterfly_inv(c)
        iz = pow(z, self.mod - 2, self.mod)
        for i in range(n + m - 1):
            c[i] = (c[i] * iz) % self.mod
        return c[:n + m - 1]
CONV = FFT(p)

fct=[1,1];inv=[0,1];finv=[1,1]
for i in range(2,N+1):
  fct.append(fct[i-1]*i%p)
  inv.append(-inv[p%i]*(p//i)%p)
  finv.append(finv[i-1]*inv[i]%p)
def cmb(n,r):
  if r<0 or n<r:return 0
  return fct[n]*finv[r]*finv[n-r]%p

C=[0 for _ in range(7)]
for k in range(1,7):
  C[k]=min(N,10**k-1)-min(N,10**(k-1)-1)

F=[1]
for k in range(1,7):
  t=pow(10,k)
  G=[0 for _ in range(C[k]+1)]
  G[0]=1
  for i in range(C[k]):
    G[i+1]=G[i]*t*(C[k]-i)*inv[i+1]%p
  F=CONV.convolution(F,G)

ans=0
for k in range(1,7):
  s=(2*10**(k-1)+C[k]-1)*C[k]//2

  G=[F[i] for i in range(N+1)]
  t=pow(10,k)
  for i in range(1,N+1):
    G[i]-=t*G[i-1];G[i]%=p
  for i in range(N):
    ans+=s*G[i]*fct[i]*fct[N-1-i];ans%=p
print(ans)