import sys
import os

sys.setrecursionlimit(10**7)

input = lambda: sys.stdin.readline().rstrip()

filename = r'ABC_390\インプット\_input_E.txt'
if os.path.exists(filename):
    sys.stdin = open(filename, 'r')

try:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')
except ModuleNotFoundError:
    pass

def MAPIN():
    return map(int,input().split())
def LIN():
    return list(map(int,input().split()))
def ININ():
    return int(input())

import bisect
N,X = MAPIN()

dp1 = [0]*(X+1)
dp2 = [0]*(X+1)
dp3 = [0]*(X+1)
for _ in range(N):
    V,A,C = MAPIN()
    dp_new = [0]*(X+1)
    if V == 1:
        for i in range(X+1):
            dp_new[i] = max(dp_new[i],dp1[i])
            if i+C < X+1:
                dp_new[i+C] = max(dp_new[i+C],dp1[i]+A)
        dp1 = dp_new
    if V == 2:
        for i in range(X+1):
            dp_new[i] = max(dp_new[i],dp2[i])
            if i+C < X+1:
                dp_new[i+C] = max(dp_new[i+C],dp2[i]+A)
        dp2 = dp_new
    if V == 3:
        for i in range(X+1):
            dp_new[i] = max(dp_new[i],dp3[i])
            if i+C < X+1:
                dp_new[i+C] = max(dp_new[i+C],dp3[i]+A)
        dp3 = dp_new

def CanTake(Q):
    c1 = bisect.bisect_left(dp1,Q)
    c2 = bisect.bisect_left(dp2,Q)
    c3 = bisect.bisect_left(dp3,Q)
    return (c1+c2+c3) <= X

MV = max([dp1[-1],dp2[-1],dp3[-1]])
l = 0
r = MV
while l < r:
    mid = (l+r)//2
    if CanTake(mid):
        l = mid+1
    else:
        r = mid
print(l-1)