import sys
input = sys.stdin.readline
II = lambda : int(input())
MI = lambda : map(int, input().split())
LI = lambda : [int(a) for a in input().split()]
SI = lambda : input().rstrip()
LLI = lambda n : [[int(a) for a in input().split()] for _ in range(n)]
LSI = lambda n : [input().rstrip() for _ in range(n)]
MI_1 = lambda : map(lambda x:int(x)-1, input().split())
LI_1 = lambda : [int(a)-1 for a in input().split()]

def graph(n:int, m:int, dir:bool=False, index:int=-1) -> list[set[int]]:
    edge = [set() for i in range(n+1+index)]
    for _ in range(m):
        a,b = map(int, input().split())
        a += index
        b += index
        edge[a].add(b)
        if not dir:
            edge[b].add(a)
    return edge

def graph_w(n:int, m:int, dir:bool=False, index:int=-1) -> list[set[tuple]]:
    edge = [set() for i in range(n+1+index)]
    for _ in range(m):
        a,b,c = map(int, input().split())
        a += index
        b += index
        edge[a].add((b,c))
        if not dir:
            edge[b].add((a,c))
    return edge

mod = 998244353
inf = 1001001001001001001
ordalp = lambda s : ord(s)-65 if s.isupper() else ord(s)-97
ordallalp = lambda s : ord(s)-39 if s.isupper() else ord(s)-97
yes = lambda : print("Yes")
no = lambda : print("No")
yn = lambda flag : print("Yes" if flag else "No")
def acc(a:list[int]):
    sa = [0]*(len(a)+1)
    for i in range(len(a)):
        sa[i+1] = a[i] + sa[i]
    return sa

prinf = lambda ans : print(ans if ans < 1000001001001001001 else -1)
alplow = "abcdefghijklmnopqrstuvwxyz"
alpup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpall = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
URDL = {'U':(-1,0), 'R':(0,1), 'D':(1,0), 'L':(0,-1)}
DIR_4 = [[-1,0],[0,1],[1,0],[0,-1]]
DIR_8 = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
DIR_BISHOP = [[-1,1],[1,1],[1,-1],[-1,-1]]
prime60 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
sys.set_int_max_str_digits(0)

from collections import defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
DD = defaultdict
BSL = bisect_left
BSR = bisect_right

class LazySegTree:
    __slots__ = ["n", "log", "size", "data", "lazy", "e", "op", "mapping", "composition", "id"]

    def push(self, k):

        self.data[2 * k] = self.mapping(self.lazy[k], self.data[2 * k])
        if 2 * k < self.size:
            self.lazy[2 * k] = self.composition(self.lazy[k], self.lazy[2 * k])

        self.data[2 * k + 1] = self.mapping(self.lazy[k], self.data[2 * k + 1])
        if 2 * k < self.size:
            self.lazy[2 * k + 1] = self.composition(self.lazy[k], self.lazy[2 * k + 1])

        self.lazy[k] = self.id

    def __init__(self, op, e, mapping, composition, id, lst):
        self.n = len(lst)
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.data = [e] * (2 * self.size)
        self.lazy = [id] * (2 * self.size)
        self.e = e
        self.op = op
        self.mapping = mapping
        self.composition = composition
        self.id = id
        for i in range(self.n):
            self.data[self.size + i] = lst[i]
        for i in range(self.size - 1, 0, -1):

            self.data[i] = self.op(self.data[i << 1], self.data[(i << 1) | 1])

    def set(self, p, x):
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.data[p] = x
        for i in range(1, self.log + 1):

            k = p >> i
            self.data[k] = self.op(self.data[k << 1], self.data[(k << 1) | 1])

    def get(self, p):
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        return self.data[p]

    def prod(self, l, r):
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
            return self.e
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push(r >> i)
        sml, smr = self.e, self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.data[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.data[1]

    def apply_point(self, p, f):
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.data[p] = self.mapping(f, self.data[p])
        for i in range(1, self.log + 1):

            k = p >> i
            self.data[k] = self.op(self.data[k << 1], self.data[(k << 1) | 1])

    def apply(self, l, r, f):
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push((r - 1) >> i)
        l2, r2 = l, r
        while l < r:
            if l & 1:

                self.data[l] = self.mapping(f, self.data[l])
                if l < self.size:
                    self.lazy[l] = self.composition(f, self.lazy[l])
                l += 1
            if r & 1:
                r -= 1

                self.data[r] = self.mapping(f, self.data[r])
                if l < self.size:
                    self.lazy[r] = self.composition(f, self.lazy[r])
            l >>= 1
            r >>= 1
        l, r = l2, r2
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:

                k = l >> i
                self.data[k] = self.op(self.data[k << 1], self.data[(k << 1) | 1])
            if ((r >> i) << i) != r:

                k = (r - 1) >> i
                self.data[k] = self.op(self.data[k << 1], self.data[(k << 1) | 1])

    def max_right(self, l, g):
        assert 0 <= l and l <= self.n
        assert g(self.e)
        if l == self.n:
            return self.n
        l += self.size
        for i in range(self.log, 0, -1):
            self.push(l >> i)
        sm = self.e
        while 1:
            while l % 2 == 0:
                l >>= 1
            if not (g(self.op(sm, self.data[l]))):
                while l < self.size:
                    self.push(l)
                    l = 2*l
                    if g(self.op(sm, self.data[l])):
                        sm = self.op(sm, self.data[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.data[l])
            l += 1
            if (l&-l) == l: break
        return self.n

    def min_left(self, r, g):
        assert 0 <= r and r <= self.n
        assert g(self.e)
        if r == 0: return 0
        r += self.size
        for i in range(self.log, 0, -1):
            self.push((r - 1) >> i)
        sm = self.e
        while 1:
            r -= 1
            while r > 1 and (r % 2):
                r >>= 1
            if not (g(self.op(self.data[r], sm))):
                while r < self.size:
                    self.push(r)
                    r = 2*r + 1
                    nsm = self.op(self.data[r], sm)
                    if g(nsm):
                        sm = nsm
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.data[r], sm)
            if (r&-r) == r: break
        return 0

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])

def op(x, y):
    return x + y

def mul(x, y):
    return x * y

n = II()
p = LI_1()

two = [1] * (n + 1)
for i in range(n):
    two[i + 1] = two[i] * 2 % mod

def calc(p):
    r = 0
    s = LazySegTree(op, 0, mul, mul, 1, [1] * (n-1))
    for i in range(n - 1):
        s.apply(p[i], n-1, 2)
        r += s.all_prod()
    return r

ans = (two[n] - 1) * (n - 1) * (n - 1) % mod
for i in range(1, n):
    ans -= 4 * two[i] * (n - 1) % mod

ans += calc(p)
ans += calc(p[::-1])
ans += calc([n-1-x for x in p])
ans += calc([n-1-x for x in p][::-1])
print(ans % mod)