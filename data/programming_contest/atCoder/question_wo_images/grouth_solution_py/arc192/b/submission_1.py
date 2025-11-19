from sys import stdin, stderr, setrecursionlimit
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop
from math import gcd, lcm, factorial
from itertools import permutations, accumulate, product, combinations
from functools import cache, reduce, cmp_to_key
from random import randint, shuffle

setrecursionlimit(10 ** 8)
input = stdin.readline
INF = 1 << 62
INf = float("inf")
MOD99 = 998244353
MOD17 = 1000000007
MOD61 = (1 << 61) - 1

DX = (0, 1, 0, -1)
DY = (-1, 0, 1, 0)
DX8 = (0, 1, 1, 1, 0, -1, -1, -1)
DY8 = (-1, -1, 0, 1, 1, 1, 0, -1)

def clamp(lo, x, hi): return max(lo, min(x, hi))
def m_rot_r(a): return list(zip(*a[::-1]))
def m_rot_l(a): return list(zip(*[row[::-1] for row in a]))

def ini(): return int(input())
def inmi(): return map(int, input().split())
def inmdi(): return map(lambda x: int(x) - 1, input().split())
def inil(): return list(inmi())
def indil(): return list(inmdi())
def init(): return tuple(inmi())
def indit(): return tuple(inmdi())
def ins(): return input()[:-1]
def insl(): return list(ins())
def inss(): return list(input().split())
def inmul(f, n): return [f() for _ in range(n)]

def yes(f=True): print("Yes" if f else "No")
def no(f=True): print("No" if f else "Yes")

def debug(*args, **kwargs): print("debug:", *args, **kwargs, file=stderr)

def main():
    n = ini()
    a = init()

    o = 0
    for i in range(n):
        o += a[i] % 2

    if n == 1:
        print("Fennec")
    elif n == 2:
        print("Snuke")
    elif n == 3:
        print("Fennec" if o else "Snuke")
    else:
        print("Fennec" if o % 2 else "Snuke")

if __name__ == '__main__':
    main()