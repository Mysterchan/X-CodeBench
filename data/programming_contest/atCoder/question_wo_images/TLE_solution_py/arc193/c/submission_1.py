import sys,time

from itertools import permutations
from heapq import heappop,heappush
from collections import deque
import random
import bisect
from math import ceil,floor

input = lambda :sys.stdin.readline().rstrip()
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    return (g1[n] * g2[r] % mod) * g2[n-r] % mod

mod = 998244353
N = 2*10**5
g1 = [1]*(N+1)
g2 = [1]*(N+1)
inverse = [1]*(N+1)

for i in range( 2, N + 1 ):
    g1[i]=( ( g1[i-1] * i ) % mod )
    inverse[i]=( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2[i]=( (g2[i-1] * inverse[i]) % mod )
inverse[0]=0

def solve(H,W,C):
    dp = [[[0]*(W+1) for h in range(H+1)] for p in range(16)]

    for h in range(1,H+1):
        for w in range(1,W+1):
            for p in [8]:
                t = 1
                A,B = dp[2],dp[6]
                for i in range(1,h):
                    t = t * C % mod
                    dp[p][h][w] +=  (t-C) * (A[h-i][w] * g2[i] % mod) % mod
                    dp[p][h][w] +=  C * (B[h-i][w] * g2[i] % mod) % mod
                dp[p][h][w] %= mod

            for p in [5,9]:
                t = 1
                A,B = dp[2],dp[6]
                for i in range(1,h):
                    t = t * (C-1) % mod
                    dp[p][h][w] +=  (t-(C-1)) * (A[h-i][w] * g2[i] % mod) % mod
                    dp[p][h][w] +=  (C-1) * (B[h-i][w] * g2[i] % mod) % mod
                dp[p][h][w] %= mod

            for p in [2]:
                t = 1
                A,B = dp[8][h],dp[9][h]
                for j in range(1,w):
                    t = t * C % mod
                    dp[p][h][w] +=  (t-C) * (A[w-j] * g2[j] % mod) % mod
                    dp[p][h][w] +=  C * (B[w-j] * g2[j] % mod) % mod
                dp[p][h][w] %= mod

            for p in [5,6]:
                t = 1
                A,B = dp[8][h],dp[9][h]
                for j in range(1,w):
                    t = t * (C-1) % mod
                    dp[p][h][w] +=  (t-(C-1)) * (A[w-j] * g2[j] % mod) % mod
                    dp[p][h][w] +=  (C-1) * (B[w-j] * g2[j] % mod) % mod
                dp[p][h][w] %= mod

            for p in [2,6,8,9,5]:

                if p & 10 == 0:
                    if p & 5:
                        dp[p][h][w] += (C-1) * g2[h] * g2[w] % mod
                    else:
                        dp[p][h][w] += C * g2[h] * g2[w] % mod
                    dp[p][h][w] %= mod

                if p & 2 == 0:
                    if p & 1:
                        dp[p][h][w] += (pow(C-1,h,mod) - (C-1)) * g2[h] * g2[w] % mod
                    else:
                        dp[p][h][w] += (pow(C,h,mod) - (C)) * g2[h] * g2[w] % mod
                    dp[p][h][w] %= mod

                if p & 8 == 0:
                    if p & 4:
                        dp[p][h][w] += (pow(C-1,w,mod) - (C-1)) * g2[h] * g2[w] % mod
                    else:
                        dp[p][h][w] += (pow(C,w,mod) - C) * g2[h] * g2[w] % mod
                    dp[p][h][w] %= mod

    tmp_f = [[dp[5][h][w] % mod for w in range(W+1)] for h in range(H+1)]
    tmp_g = [[0]*(W+1) for i in range(H+1)]

    tmp_h = [0] * (max(H,W)+1)
    tmp_h[0] = 1
    for i in range(max(H,W)+1):
        nxt_h = [0] * (max(H,W)+1)
        for j in range(len(tmp_h)):
            for k in range(1,max(H,W)+1-j):
                nxt_h[j+k] += tmp_h[j] * g2[k] % mod
                nxt_h[j+k] %= mod
        tmp_h = nxt_h

        CC = pow(C-1,i,mod) * C
        for x in range(H+1):
            for y in range(W+1):
                tmp_g[x][y] += CC * (tmp_h[x] * tmp_h[y] % mod) % mod
                tmp_g[x][y] %= mod

    res = 0
    for i in range(1,H+1):
        for j in range(1,W+1):
            res += tmp_f[H-i][W-j] * tmp_g[i][j] % mod
            res %= mod

    return (res * g1[H] * g1[W] + C) % mod

H,W,C = mi()
print(solve(H,W,C))