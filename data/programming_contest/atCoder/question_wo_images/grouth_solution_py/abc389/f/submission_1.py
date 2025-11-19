from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
from bisect import bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd
from operator import mul
from functools import reduce
from copy import deepcopy

sys.setrecursionlimit(2147483647)
INF = 10**18

def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def S(): return input()
def LS(): return input().split()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]

class BIT:
    def __init__(self, size):
        self.bit = [0] * size
        self.size = size
        self.total = 0

    def add(self, i, w):
        x = i + 1
        self.total += w
        while x <= self.size:
            self.bit[x - 1] += w
            x += x & -x
        return

    def sum(self, i):
        res = 0
        x = i + 1
        while x:
            res += self.bit[x - 1]
            x -= x & -x
        return res

    def search(self, k):
        if k > self.total or k < 0:
            return -1
        step = 1 << (self.size.bit_length() - 1)
        now_index = 0
        ret = 0
        while step:
            if now_index + step < self.size and ret + self.bit[now_index + step - 1] < k:
                ret += self.bit[now_index + step - 1]
                now_index += step
            step >>= 1

        return now_index

n=I()
bit=BIT(7*10**5)
for g in range(1,7*10**5+1):
    bit.add(g,1)

for _ in range(n):
    l,r=LI()
    r_idx=bit.search(r+1)
    l_idx=bit.search(l)
    bit.add(l_idx,1)
    bit.add(r_idx,-1)

q=I()
for _ in range(q):
    x=I()
    print(bit.sum(x))