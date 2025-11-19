import sys
from collections import deque, Counter, defaultdict
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353

N = ii()
A = li()

dp = [[0]*2 for _ in range(N+1)]
dp[0][1] = 1
for i in range(N):
    if A[i] == -1:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1]
        dp[i+1][0] += dp[i][1] * (N-1)
    elif A[i] == i:
        dp[i+1][0] = dp[i][0]
    elif A[i] == i+2:
        dp[i+1][1] = dp[i][1]
    else:
        dp[i+1][0] = dp[i][0]

    dp[i+1][0] %= mod
    dp[i+1][1] %= mod

ans = 0
for i in range(2):
    if dp[-1][i]!=-1:
        ans += dp[-1][i]
print(ans)