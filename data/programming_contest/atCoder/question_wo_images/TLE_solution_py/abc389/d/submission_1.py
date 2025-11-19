import math
import sys
import itertools
from collections import Counter
from collections import deque
from collections import defaultdict
from math import gcd
from math import sqrt
from sys import stdin
from bisect import bisect_left, bisect_right

def input() : return stdin.readline().rstrip()
def mips():
    return map(int,input().split())
def sips():
    return map(str,input().split())
def ii():
    return int(input())
def list_perm(L) :
    return [list(l) for l in itertools.permutations(L)]
def list_perm_k(L,k):
    return [list(l) for l in itertools.permutations(L,k)]
def dist(A,B):
    x1,y1 = A
    x2,y2 = B
    return sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
def ngcd(L):
    res = L[0]
    for i in range(len(L)):
        if res != 1:
            res = gcd(res,L[i])
    return res
def lcm(a,b):
    return a*b//(gcd(a,b))
def nlcm(L):
    res = L[0]
    for i in range(len(L)):
        res = lcm(res,L[i])
    return res
def ketawa(n):
    res = 0
    while (n > 0):
        res += n%10
        n //= 10
    return res

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

R = int(input())

ans = 0

move_i = [0.5, -0.5]
move_j = [0.5, -0.5]

def is_ok(point, R):
    i,j = point
    ok = True
    for k1 in range(2):
        for k2 in range(2):
            new_i, new_j = i + move_i[k1], j + move_j[k2]
            if new_i > 0 and new_j > 0 and dist((0,0), (new_i, new_j)) <= R:
                continue
            else:
                ok = False
    return ok

for i in range(1,R):
    ok = 0
    ng = 10**10
    while ng - ok > 1:
        mid = (ok + ng) // 2
        point = (i, mid)
        if is_ok(point, R):
            ok = mid
        else:
            ng = mid
    ans += ok

ans *= 4
ans += 4 * (R - 1) + 1
print(ans)