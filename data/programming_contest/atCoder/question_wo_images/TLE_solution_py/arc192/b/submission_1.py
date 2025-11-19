import sys
sys.setrecursionlimit(1000000)
sys.set_int_max_str_digits(10**6)
mod = 998244353
mod2 = 10**9+7
INF = 1<<60
alf = {chr(i+ord("a")):i for i in range(26)}
ALF = {chr(i+ord("A")):i for i in range(26)}

N = int(input())
A = list(map(int, input().split()))
from functools import lru_cache
cnt0, cnt1 = 0, 0
for i in A:
    if i % 2:cnt0 += 1
    else:cnt1 += 1
@lru_cache(maxsize=None)
def solve(able, c0, c1):
    ret = 0
    if c0 + c1 == 0:return 0
    if able:ret |= solve(0, c0, c1) ^ 1
    if c0 > 0:
        ret |= solve(able, c0-1, c1) ^ 1
    if c1 > 0:
        ret |= solve(able ^ 1, c0, c1-1) ^ 1
    return ret
print("Fennec" if solve(0, cnt0, cnt1) else "Snuke")