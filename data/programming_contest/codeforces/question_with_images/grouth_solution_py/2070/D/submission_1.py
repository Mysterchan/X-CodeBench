from math import ceil, sqrt, log, log2, floor, gcd, inf, isqrt, lcm
import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify


number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
so = lambda: sorted(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp
rand = randint(1, 10000)
xor = lambda x: x ^ rand
prefix_sum = lambda arr: list(itertools.accumulate(arr))

mod = 998244353



def solve():
    n = number()
    pars = numbers()
    graph = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        graph[pars[i]].append(i + 2)
    mine = [1] * (n + 1)
    level = []
    q = deque([1])
    while q:
        cur = []
        for _ in range(len(q)):
            top = q.popleft()
            cur.append(top)
            for lij in graph[top]:
                q.append(lij)
        level.append(cur)
    level_sum = [0] * len(level)
    for node in level[-1]:
        level_sum[-1] += 1
    for i in range(len(level) - 2, 0, -1):
        cur_level = level[i]
        for node in cur_level:
            lijoche = 0
            for lij in graph[node]:
                lijoche = mine[lij] + lijoche
            mine[node] = level_sum[i + 1] - lijoche + 1
            level_sum[i] = (mine[node] + level_sum[i]) % mod
    print((level_sum[1] + 1) % mod)

    return


for _ in range(test_cases()):
    solve()
