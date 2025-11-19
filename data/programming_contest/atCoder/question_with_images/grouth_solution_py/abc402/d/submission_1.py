import random
from math import *
from functools import lru_cache,cmp_to_key
from itertools import *
from fractions import Fraction
from bisect import bisect_left as bl
from bisect import bisect_right as br
from operator import itemgetter
from collections import Counter,deque,defaultdict
from heapq import heappop as hpop, heappush as hpush
YES = ['NO','YES']
Yes = ["No","Yes"]
yes = ["no","yes"]

MOD = [10**9 + 7,998244353]
MOD = MOD[0]
rand = random.randint(10**8,10**9)
n,m,files = 0,0,0
import sys
if files:sys.stdin = open("input.txt");sys.stdout = open("output.txt", 'w')
input = sys.stdin.readline
output = sys.stdout.write

def I(): return int(input())
def S(): return input().strip()
def F(): return float(input())
def MI(): return map(int, input().split())
def MS(): return map(str, input().split())
def MF(): return map(float,input().split())
def LI(): return list(MI())
def LS(): return list(MS())
def LF(): return list(MF())
def MAT(n): return [LI() for _ in range(n)]

def fast_pow(a, b, n):
    a %= n
    res = 1
    while b:
        if b & 1:
            res = res * a % n
        a = a * a % n
        b >>= 1
    return res
def add(a, b): return (a % MOD + b % MOD) % MOD
def sub(a, b): return (a % MOD - b % MOD + MOD) % MOD
def pro(a, b): return (a % MOD * b % MOD) % MOD

def div(a, b): return pro(a, inv(b))

def inv(a): return fast_pow(a, MOD - 2, MOD)

def invcom(a):
    def egcd(a, b):
        if b == 0: return a, 1, 0
        g, x1, y1 = egcd(b, a % b)
        return g, y1, x1 - (a // b) * y1
    g, x, _ = egcd(a, MOD)
    return (x % MOD) if g == 1 else "no solution"
def inbound(i,j): return 0 <= i < n and 0 <= j < m
def idx(i,j):return i*m + j
def idxs(n): return [n//m,n%m]
def summ(n):return (n * (n+1))>>1
def nc2(n):return summ(n-1)
def sod(n): return sum(int(i) for i in str(n))
def cdc(n):return (10*n-sod(n))//9
DIR4 = [(1,0),(-1,0),(0,1),(0,-1)]
DIR8 = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
knight = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
direction = {(-1,0):"U",(1,0):"D",(0,-1):"L",(0,1):"R"}
direction_reverse = {"L":(0,1),"R":(0,-1),"U":(1,0),"D":(-1,0)}

res = []
def OI(res): output("\n".join(res))
def OL(res): output("\n".join(" ".join(i) for i in res))

n,m = MI()
lines = MAT(m)

parallel_sign = defaultdict(int)
for a,b in lines:
    parallel_sign[(a+b)%n]+=1
total = nc2(m)
for i in parallel_sign:
    total -= nc2(parallel_sign[i])
print(total)