import sys
import math
import bisect
import heapq
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate, product
from functools import lru_cache, reduce

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

def solve():
    def shifter(c, x, y):
        if c == "N":
            return x - 1, y
        if c == "S":
            return x + 1, y
        if c == "E":
            return x, y + 1
        if c == "W":
            return x, y - 1

    n, r, c = map(int, input().split())
    ss = input()
    dq = deque()
    dq.append((0, 0))
    ans = ["0"] * n
    if (r, c) == (0, 0):
        print("1" * n)
        return
    for i, cc in enumerate(ss):
        origin = False
        see = False
        for _ in range(len(dq)):
            x, y = dq.popleft()
            x, y = shifter(cc, x, y)
            dq.append((x, y))
            if (x, y) == (r, c):
                see = True
            if (x, y) == (0, 0):
                origin = True
        if not origin:
            dq.append((0, 0))
        if see:
            ans[i] = "1"

    print("".join(ans))

if __name__ == "__main__":
    solve()