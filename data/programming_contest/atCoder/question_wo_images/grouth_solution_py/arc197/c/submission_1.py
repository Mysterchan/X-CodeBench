import sys

int1 = lambda x: int(x)-1
pDB = lambda *x: print(*x, end="\n", file=sys.stderr)
p2D = lambda x: print(*x, sep="\n", end="\n\n", file=sys.stderr)
def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def SI(): return sys.stdin.readline().rstrip()

dij = [(0, 1), (-1, 0), (0, -1), (1, 0)]

inf = -1-(-1 << 62)

md = 998244353

class BitSum:
    def __init__(self, n):
        self._n = n+1
        self._table = [0]*self._n
        self._origin = [0]*n

    def __getitem__(self, item):
        return self._origin[item]

    def __setitem__(self, index, value):
        self.add(index, value-self._origin[index])
        self._origin[index] = value

    def add(self, i, x):
        if x == 0: return
        self._origin[i] += x
        i += 1
        while i < self._n:
            self._table[i] += x
            i += i & -i

    def sum(self, r):
        res = 0
        while r > 0:
            res += self._table[r]
            r -= r & -r
        return res

    def sumlr(self, l, r):
        if l >= r: return 0
        if l == 0: return self.sum(r)
        return self.sum(r)-self.sum(l)

    def bisect(self, x):
        idx = 0
        d = 1 << (self._n-1).bit_length()-1
        while d:
            if idx|d < self._n and self._table[idx|d] < x:
                idx |= d
                x -= self._table[idx]
            d >>= 1
        return idx

lim=3*10**6
bit=BitSum(lim)
for i in range(1,lim):bit.add(i,1)
for _ in range(II()):
    a,b=LI()
    if a<lim and bit[a]:
        for i in range(a,lim,a):bit[i]=0
    ans=bit.bisect(b)
    print(ans)