import bisect
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce
import heapq
import itertools
import string
import sys
from math import ceil, floor, gcd, inf, log2, sqrt
sys.setrecursionlimit(10 ** 9)
def fmax(a, b):
    return a if a > b else b
def fmin(a, b):
    return a if a < b else b
def read_ints():
    return [int(x) for x in input().split(' ')]

def slv():
    n, = read_ints()
    p = read_ints()

    g = [[] for _ in range(n)]
    for i in range(n - 1):
        g[p[i] - 1].append(i + 1)

    sz = [0] * n
    ans = [0] * n
    def dfs(i):
        mxsz = 0
        tsz = 0
        for ch in g[i]:
            dfs(ch)
            mxsz = max(mxsz, sz[ch])
            tsz += sz[ch]
        sz[i] = tsz + 1
        for ch in g[i]:
            if sz[ch] == mxsz:
                rsz = tsz - sz[ch]
                if sz[ch] <= rsz:
                    ans[i] = tsz // 2
                    return
                mc = min(sz[ch] - ans[ch] * 2, rsz)
                rsz -= mc
                mc += min(ans[ch], rsz // 2)
                ans[i] = max(ans[i], mc + ans[ch])

    dfs(0)
    print(ans[0])

T = read_ints()[0]
for _ in range(T):
    slv()