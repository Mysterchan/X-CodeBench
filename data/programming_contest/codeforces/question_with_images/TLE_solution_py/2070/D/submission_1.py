import sys
import heapq
import math
def input():
    return sys.stdin.readline().strip()
from collections import defaultdict, Counter, deque
from random import randint
def intlist(): return list(map(int, (x for x in input().split())))
def strarr(): return list(int(x) for x in input())
def yn(val): print("YES" if val else "NO")
mod = 998244353
def solve():
    n = int(input())
    parents = intlist()

    graph = defaultdict(list)
    for i in range(n-1):
        graph[parents[i]].append(i + 2)

    queue = deque([1])
    levels = []
    while queue:
        tmp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            tmp.append(node)
            for neb in graph[node]:
                queue.append(neb)

        levels.append(tmp[:])

    dp = [1] * (n + 1)
    for i in range(len(levels) - 2, -1, -1):
        level = levels[i]
        su = 0
        for node in levels[i + 1]:
            su += dp[node]
            su %= mod
        for node in level:
            dp[node] = (dp[node] + su) % mod
            for neb in graph[node]:
                dp[node] = (dp[node] - dp[neb]) % mod

    print((su + 1) % mod)
    return

t = lambda inp = 0: int(input()) if not inp else inp
for _ in range(t()):
    solve()
