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

class SegTree:
    __slots__ = ["n", "size", "op", "e", "data"]

    def __init__(self, op, e, lst):
        self.n = len(lst)
        self.size = 1 << (self.n - 1).bit_length()
        self.op = op
        self.e = e
        self.data = [e] * (2 * self.size)
        for i in range(self.n):
            self.data[self.size + i] = lst[i]
        for i in range(self.size - 1, 0, -1):
            self.data[i] = self.op(self.data[2*i], self.data[2*i+1])

    def get(self, i):
        return self.data[self.size+i]

    def add(self, i, x):
        i += self.size
        self.data[i] = self.op(x, self.data[i])
        while i > 1:
            i >>= 1
            self.data[i] = self.op(self.data[2*i], self.data[2*i+1])

    def set(self, i, x):
        i += self.size
        self.data[i] = x
        while i > 1:
            i >>= 1
            self.data[i] = self.op(self.data[2*i], self.data[2*i+1])

    def prod(self, l, r):
        if r <= l:
            return self.e
        lres = self.e
        rres = self.e
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                lres = self.op(lres, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                rres = self.op(self.data[r], rres)
            l >>= 1
            r >>= 1
        return self.op(lres, rres)

    def all_prod(self):
        return self.data[1]

    def max_right(self, l, g):
        assert 0<=l and l<=self.n
        assert g(self.e)
        if l == self.n: return self.n
        l += self.size
        sm = self.e
        while 1:
            while l&1 == 0:
                l >>= 1
            if not(g(self.op(sm, self.data[l]))):
                while l < self.size:
                    l = 2*l
                    nsm = self.op(sm, self.data[l])
                    if g(nsm):
                        sm = nsm
                        l += 1
                return l-self.size
            sm = self.op(sm, self.data[l])
            l += 1
            if (l&-l) == l: break
        return self.n

    def min_left(self, r, g):
        if r == -1: r = self.n
        assert 0<=r and r<=self.n
        assert g(self.e)
        if r == 0: return 0
        r += self.size
        sm = self.e
        while 1:
            r -= 1
            while (r>1 and r&1):
                r >>= 1
            if not(g(self.op(self.data[r], sm))):
                while r < self.size:
                    r = 2*r+1
                    nsm = self.op(self.data[r], sm)
                    if g(nsm):
                        sm = nsm
                        r -= 1
                return r + 1 -self.size
            sm = self.op(self.data[r], sm)
            if (r&-r) == r: break
        return 0

    def __str__(self):
        return str(self.data[self.size:self.size+self.n])

n = II()
a = LI()
q = II()

def op(x, y):
    l = x[0] if x[0] != x[3] else x[0] + y[0]
    r = y[1] if y[1] != y[3] else x[1] + y[1]
    s = x[3] + y[3]

    if l == s:
        c = (l >= 2)
    else:
        c = x[2] + y[2]
        if x[1] < 2 and y[0] < 2 and x[1] + y[0] >= 2:
            c += 1
        if x[1] >= 2 and y[0] >= 2:
            c -= 1

    return (l, r, c, s)

p = [(1, 1, 0, 1), (0, 0, 0, 1)]
seg = SegTree(op, (0, 0, 0, 0), [p[x] for x in a])

c0 = a.count(0)
sgn = [-1, 1]
for i in range(q):
    i = II() - 1
    c0 += sgn[a[i]]
    a[i] ^= 1

    seg.set(i, p[a[i]])
    l, r, c, s = seg.all_prod()

    if c == 0:
        if c0 == 0:
            print(n)
        else:
            ans = 2
            if l != 0 and r != 0:
                ans += 1
            print(ans)
    else:
        print(3 * c + 1 - (l >= 2) - (r >= 2) + (l == 1) + (r == 1))