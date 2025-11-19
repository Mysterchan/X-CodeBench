import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

N, M = map(int, input().split())
S = list(map(int, input().split()))

# We want to count the number of ways to reach x = 2^N starting from x=0,
# with operations: x -> (x OR s_i) + 1, for i in [1..M].
# x ranges from 0 to 2^N (inclusive).
# When x = 2^N, we stop.

# Key observations:
# - x can only increase, since (x OR s_i) >= x and then +1.
# - The maximum x is 2^N.
# - We want dp[x] = number of ways to reach 2^N from x.
# - dp[2^N] = 1 (base case).
# - For x < 2^N:
#   dp[x] = sum over i of dp[(x OR s_i) + 1], if (x OR s_i) + 1 <= 2^N, else 0.

# Direct DP from 0 to 2^N is impossible due to size (up to 2^24 ~ 16 million).
# But we can do DP from the end (top-down with memoization) and prune states.

# We'll implement a memoized DFS with a dictionary to store dp[x].
# Since each step increases x, no cycles.
# The number of reachable states is limited by the transitions.

from collections import defaultdict
sys.setrecursionlimit(1 << 25)

dp = dict()

END = 1 << N

def dfs(x):
    if x == END:
        return 1
    if x in dp:
        return dp[x]
    res = 0
    for s in S:
        nx = (x | s) + 1
        if nx <= END:
            res += dfs(nx)
            if res >= MOD:
                res -= MOD
    dp[x] = res
    return res

print(dfs(0) % MOD)