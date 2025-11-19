import sys
input = sys.stdin.readline

N, X = map(int, input().split())
foods = [[], [], []]  # index 0 for vitamin 1, 1 for vitamin 2, 2 for vitamin 3

for _ in range(N):
    v, a, c = map(int, input().split())
    foods[v-1].append((a, c))

# Maximum calories sum is X, so dp arrays size = X+1
# dp[i] = max total vitamin amount achievable with i calories
# We'll do 0/1 knapsack for each vitamin group separately

def knapsack(items):
    dp = [-1]*(X+1)
    dp[0] = 0
    for a, c in items:
        for cal in range(X - c, -1, -1):
            if dp[cal] >= 0:
                val = dp[cal] + a
                if val > dp[cal + c]:
                    dp[cal + c] = val
    # Make dp non-decreasing to allow binary search
    for i in range(1, X+1):
        if dp[i] < dp[i-1]:
            dp[i] = dp[i-1]
    return dp

dp1 = knapsack(foods[0])
dp2 = knapsack(foods[1])
dp3 = knapsack(foods[2])

# Binary search on answer k
# For each k, find minimal calories to get at least k vitamin units in each dp
# If sum of these minimal calories <= X, k is achievable

def min_cal(dp, k):
    # dp is non-decreasing, find leftmost index with dp[i] >= k
    # If none, return X+1 (impossible)
    l, r = 0, X
    res = X+1
    while l <= r:
        m = (l+r)//2
        if dp[m] >= k:
            res = m
            r = m -1
        else:
            l = m +1
    return res

ok, ng = 0, 2_000_000_001  # upper bound large enough

while ng - ok > 1:
    mid = (ok + ng) // 2
    c1 = min_cal(dp1, mid)
    c2 = min_cal(dp2, mid)
    c3 = min_cal(dp3, mid)
    if c1 + c2 + c3 <= X:
        ok = mid
    else:
        ng = mid

print(ok)