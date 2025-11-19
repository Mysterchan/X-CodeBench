import sys, time, random, heapq, math, itertools, copy
from collections import deque, Counter, defaultdict
from sortedcontainers import SortedSet, SortedList
from bisect import bisect, bisect_left, bisect_right
import heapq as hq
from functools import cache, cmp_to_key
def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = ii()
for i in range(T):
    x, y, z = mi()
    flg = True
    if z > x + y:
        flg = False
    if x < z:
        flg = False
    if y > x * 2:
        flg = False
    print("Yes" if flg else "No")