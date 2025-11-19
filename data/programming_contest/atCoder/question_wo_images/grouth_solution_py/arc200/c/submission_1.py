import sys

sys.setrecursionlimit(200005)

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

from collections import deque
from heapq import *

def solve():
    n = II()
    lr = LLI(n)
    to = [[] for _ in range(n)]
    ot = [[] for _ in range(n)]
    for i in range(n):
        l, r = lr[i]
        for j in range(i):
            s, t = lr[j]
            if s < l and r < t:
                to[i].append(j)
                ot[j].append(i)
            if s > l and r > t:
                to[j].append(i)
                ot[i].append(j)
    for i in range(n):ot[i].sort()

    def put(i):
        nonlocal seat
        if ans[i]!=-1:return
        for j in ot[i]:put(j)
        ans[i]=seat
        seat+=1

    ans = [-1]*n
    seat = 1
    for i in range(n):put(i)
    print(*ans)

for _ in range(II()): solve()