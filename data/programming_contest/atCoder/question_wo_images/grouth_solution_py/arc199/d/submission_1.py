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
sys.setrecursionlimit(10**6)

from collections import defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
DD = defaultdict
BSL = bisect_left
BSR = bisect_right

class Comb:
    __slots__ = ["fac", "finv", "mod"]
    def __init__(self, lim:int, mod:int = mod):

        self.fac = [1]*(lim+1)
        self.finv = [1]*(lim+1)
        self.mod = mod
        for i in range(2,lim+1):
            self.fac[i] = self.fac[i-1]*i%self.mod
        self.finv[lim] = pow(self.fac[lim],-1,mod)
        for i in range(lim,2,-1):
            self.finv[i-1] = self.finv[i]*i%self.mod

    def C(self, a, b):
        if b < 0 or a < b: return 0
        if a < 0: return 0
        return self.fac[a]*self.finv[b]%self.mod*self.finv[a-b]%self.mod

    def __call__(self, a, b):
        if b < 0 or a < b: return 0
        if a < 0: return 0
        return self.fac[a]*self.finv[b]%self.mod*self.finv[a-b]%self.mod

    def P(self, a, b):
        if b < 0 or a < b: return 0
        if a < 0: return 0
        return self.fac[a]*self.finv[a-b]%self.mod

    def H(self, a, b): return self.C(a+b-1,b)
    def F(self, a): return self.fac[a]
    def Fi(self, a): return self.finv[a]

h, w = MI()
if h < w:
    h, w = w, h

comb = Comb(w + 10)

dp = [[0] * (w + 1) for i in range(h + 2)]
cnt = [[0] * (w + 1) for i in range(h + 2)]
cnt[0][0] = 1
for i in range(h):
    for j in range(w + 1):

        for k in range(w + 1 - j):

            tmp = cnt[i][j] * comb(k+j+1, j) % mod

            cnt[i+1][k+j] += tmp

            dp[i+1][k+j] += dp[i][j] * comb(k+j+1, j) % mod

            dp[i+1][k+j] += tmp * k % mod * i % mod

            dp[i+1][k+j] += cnt[i][j] * comb(k+j+1, j-1) % mod
            cnt[i+1][k+j] %= mod
            dp[i+1][k+j] %= mod

ans = 0
for j in range(w + 1):
    ans += dp[h][j] * comb(w, j) % mod
    ans += cnt[h][j] * h % mod * (w - j) % mod * comb(w, j) % mod
    ans %= mod
print(ans)