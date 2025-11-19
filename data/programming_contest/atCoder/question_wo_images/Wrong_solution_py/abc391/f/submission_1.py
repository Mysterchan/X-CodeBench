import math
from collections import deque, defaultdict, Counter
from itertools import accumulate, permutations, combinations, product
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from random import randint, shuffle, seed
from time import perf_counter as pc
from sys import setrecursionlimit
setrecursionlimit(10**6)
def II(): return int(input())
def LI(): return [int(x) for x in input().split()]
def LI_1(): return [int(x) - 1 for x in input().split()]
def SI(): return input()
def LS(): return list(input().split())
mod = 998244353
mod2 = 1000000007
inf = 1<<61

def YN(flag: bool, Yes = "Yes", No = "No") -> None:
    return print(Yes if flag else No)

def f(i, j, k):
    return A[i] * B[j] + B[j] * C[k] + C[k] * A[i]
N,K = LI()
A = LI()
B = LI()
C = LI()

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

hq = [(-f(0, 0, 0), 0, 0, 0)]
s = {(0, 0, 0)}

for t in range(K):
    val, i, j, k = heappop(hq)
    if t == K - 1:
        print(-val)
    if i + 1 < N and (i + 1, j, k) not in s:
        heappush(hq, (-f(i + 1, j, k), i + 1, j, k))
    if j + 1 < N and (i, j + 1, k) not in s:
        heappush(hq, (-f(i, j + 1, k), i, j + 1, k))
    if k + 1 < N and (i, j, k + 1) not in s:
        heappush(hq, (-f(i, j, k + 1), i, j, k + 1))