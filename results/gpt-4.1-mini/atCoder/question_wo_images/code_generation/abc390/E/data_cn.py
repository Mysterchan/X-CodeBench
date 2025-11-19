import sys
input = sys.stdin.readline

N, X = map(int, input().split())
foods = [[], [], [], []]  # index by vitamin 1-based: foods[1], foods[2], foods[3]

for _ in range(N):
    V, A, C = map(int, input().split())
    foods[V].append((A, C))

# For each vitamin type, compute dp: dp[c] = max total vitamin A with cost c
# dp size = X+1, initialize with -1 (impossible), dp[0] = 0
def calc_dp(items):
    dp = [-1] * (X + 1)
    dp[0] = 0
    for A, C in items:
        for cost in range(X - C, -1, -1):
            if dp[cost] >= 0:
                val = dp[cost] + A
                if val > dp[cost + C]:
                    dp[cost + C] = val
    return dp

dp1 = calc_dp(foods[1])
dp2 = calc_dp(foods[2])
dp3 = calc_dp(foods[3])

# For each dp, build max prefix to get max vitamin for cost <= c
def max_prefix(dp):
    maxv = [-1] * (X + 1)
    cur = -1
    for i in range(X + 1):
        if dp[i] > cur:
            cur = dp[i]
        maxv[i] = cur
    return maxv

max1 = max_prefix(dp1)
max2 = max_prefix(dp2)
max3 = max_prefix(dp3)

# We want to maximize min(vit1, vit2, vit3) with total cost <= X
# Enumerate cost1 and cost2, cost3 = X - cost1 - cost2
# For each triple, min_vit = min(max1[c1], max2[c2], max3[c3])
# Keep track of max min_vit

ans = 0
for c1 in range(X + 1):
    if max1[c1] < 0:
        continue
    for c2 in range(X - c1 + 1):
        if max2[c2] < 0:
            continue
        c3 = X - c1 - c2
        if max3[c3] < 0:
            continue
        val = min(max1[c1], max2[c2], max3[c3])
        if val > ans:
            ans = val

print(ans)