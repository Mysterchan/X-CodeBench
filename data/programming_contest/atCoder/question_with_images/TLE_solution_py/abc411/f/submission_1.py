class UnionFind():
    def __init__(self, n):
        self.n = n
        self.m = 0
        self.parents = [-1 for i in range(n)]
        self.graph = [set() for _ in range(n)]
    def root(self, x):
        if self.parents[x] == -1:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]
    def isSame(self, x, y):
        if self.root(x) == self.root(y):
            return True
        else:
            return False
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if len(self.graph[x]) < len(self.graph[y]):
            x, y = y, x
        for edge in self.graph[y]:
            edge = self.root(edge)
            if edge not in self.graph[x]:
                self.graph[x].add(edge)
                self.m += 1
            if y in self.graph[edge]:
                self.graph[edge].discard(y)
                self.m -= 1
            if x not in self.graph[edge]:
                self.graph[edge].add(x)
                self.m += 1
        self.m -= len(self.graph[y])
        self.graph[y] = set()
        if y in self.graph[x]:
            self.m -= 1
            self.graph[x].discard(y)
        if x in self.graph[x]:
            self.m -= 1
            self.graph[x].discard(x)
        self.parents[y] = x
    def __str__(self):
        ls = [set() for _ in range(self.n)]
        for i in range(self.n):
            ls[self.root(i)].add(i)
        return str(ls)
from heapq import heappop, heappush, heapify
from bisect import bisect
from sortedcontainers import SortedList
from collections import deque, defaultdict
from math import floor, ceil, isqrt, comb
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
intin = lambda: int(stdin.readline())
strin = lambda: stdin.readline().rstrip()
listin = lambda: list(map(int, stdin.readline().split()))
tuplein = lambda m: [tuple(map(lambda x: int(x) if x.isdigit() or (len(x) > 1 and x[0] == "-" and x[1:].isdigit()) else x, stdin.readline().split())) for _ in range(m)]
gridin = lambda m: [list(map(int, stdin.readline().split())) for _ in range(m)]
strgridin = lambda h: [stdin.readline().rstrip() for _ in range(h)]
mapin = lambda: map(int, stdin.readline().split())
N, M = mapin()
UV = tuplein(M)
uf = UnionFind(N)
for i in range(M): UV[i] = (UV[i][0] - 1, UV[i][1] - 1)
for u, v in UV:
    uf.graph[u].add(v)
    uf.graph[v].add(u)
uf.m = M * 2
Q = intin()
X = listin()
for x in X:
    x -= 1
    u, v = UV[x]
    uf.unite(u, v)

    print(uf.m//2)