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

INF = 10**9

def op(N,Sint,idx):
    res = ["0"] * N
    for i in range(N):
        if Sint>>i & 1:
            res[N-1-i] = "1"

    for i in range(idx)[::-1]:
        if res[i] == '1':
            res[i+1] = '1'
            res[i] = '0'
    for i in range(idx+1,N):
        if res[i] == '1':
            res[i] = "0"
            res[i-1] = '1'

    return int("".join(res),2)

def solve_brute(N,S):
    Sint = int(S,2)
    dp = [INF] * (1<<N)
    dp[Sint] = 0
    deq = deque([Sint])
    while deq:
        v = deq.popleft()

        for i in range(N):
            nv = op(N,v,i)
            if dp[nv] == INF:
                dp[nv] = dp[v] + 1
                deq.append(nv)

    return dp

def solve_slow(N,S,T):
    T_left,T_right = 0,0
    for i in range(N):
        if T[i] == "1":
            break
        T_left += 1
    for i in range(N)[::-1]:
        if T[i] == '1':
            break
        T_right += 1

    S_left,S_right = 0,0
    for i in range(N):
        if S[i] == "1":
            break
        S_left += 1
    for i in range(N)[::-1]:
        if S[i] == '1':
            break
        S_right += 1

    S_mid = S[S_left:N-S_right]
    T_mid = T[T_left:N-T_right]
    T_mid_split = T_mid.split("1")[1:]
    T_mid_split = [s.count('0') for s in T_mid_split]

    def cond(k):
        if T_left > k+S_left or T_right > k+S_right:
            return False

        tmp_S = "0" * (k+S_left-T_left) + S_mid + "0" * (k+S_right-T_right)

        S_idx = 0
        for a in T_mid_split:
            first_idx = -1
            for i in range(S_idx,len(tmp_S)):
                if tmp_S[i] == '1':
                    first_idx = i
                    break
            if first_idx == -1:
                return False

            if (first_idx-S_idx) & 1:
                first_idx += 1

            S_idx = first_idx + 1
            while True:
                if S_idx + a > len(tmp_S):
                    return False

                for i in range(S_idx,S_idx+a):
                    if tmp_S[i] == "1":
                        if (i-S_idx) & 1 == 0:
                            i += 1
                        S_idx = i + 1
                        break
                else:
                    S_idx += a
                    break

        return True

    for k in range(2*N+1):
        if cond(k):
            return k
    return -1

def solve_bit_fast(N,S,T):
    T_left,T_right = 0,0
    for i in range(N):
        if T[i] == "1":
            break
        T_left += 1
    for i in range(N)[::-1]:
        if T[i] == '1':
            break
        T_right += 1

    S_left,S_right = 0,0
    for i in range(N):
        if S[i] == "1":
            break
        S_left += 1
    for i in range(N)[::-1]:
        if S[i] == '1':
            break
        S_right += 1

    S_mid = S[S_left:N-S_right]
    T_mid = T[T_left:N-T_right]
    T_mid_split = T_mid.split("1")[1:]
    T_mid_split = [s.count('0') for s in T_mid_split]

    def cond(k):
        if T_left > k+S_left or T_right > k+S_right:
            return False

        tmp_S = "0" * (k+S_left-T_left) + S_mid + "0" * (k+S_right-T_right)

        S_idx = 0
        for a in T_mid_split:
            first_idx = -1
            for i in range(S_idx,len(tmp_S)):
                if tmp_S[i] == '1':
                    first_idx = i
                    break
            if first_idx == -1:
                return False

            if (first_idx-S_idx) & 1:
                first_idx += 1

            S_idx = first_idx + 1
            while True:
                if S_idx + a > len(tmp_S):
                    return False

                for i in range(S_idx,S_idx+a):
                    if tmp_S[i] == "1":
                        if (i-S_idx) & 1 == 0:
                            i += 1
                        S_idx = i + 1
                        break
                else:
                    S_idx += a
                    break

        return True

    res = INF

    for p in range(2):
        ok = N + 1
        ng = -1
        while ok-ng>1:
            mid = (ok+ng)//2
            if cond(2*mid+p):
                ok = mid
            else:
                ng = mid
        res = min(res,2*ok+p)

    if res >= 2*N:
        return -1
    return res

for _ in range(int(input())):
    N = int(input())
    S = input()
    T = input()

    print(solve_bit_fast(N,S,T))