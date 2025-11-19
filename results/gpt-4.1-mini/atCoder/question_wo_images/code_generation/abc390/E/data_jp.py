import sys
input = sys.stdin.readline

N, X = map(int, input().split())
foods = [[], [], []]  # index 0 for vitamin 1, 1 for vitamin 2, 2 for vitamin 3

for _ in range(N):
    V, A, C = map(int, input().split())
    foods[V-1].append((A, C))

# For each vitamin, compute dp: dp[c] = max total vitamin amount with calorie c
# dp size = X+1, initialize with -1 (impossible)
# dp[0] = 0 (no food chosen)
def calc_dp(items):
    dp = [-1]*(X+1)
    dp[0] = 0
    for A, C in items:
        for cal in range(X-C, -1, -1):
            if dp[cal] < 0:
                continue
            val = dp[cal] + A
            if val > dp[cal+C]:
                dp[cal+C] = val
    return dp

dp1 = calc_dp(foods[0])
dp2 = calc_dp(foods[1])
dp3 = calc_dp(foods[2])

# For each vitamin, create max_vit[c] = max vitamin amount achievable with calorie <= c
def max_prefix(dp):
    max_v = [-1]*(X+1)
    cur_max = -1
    for c in range(X+1):
        if dp[c] > cur_max:
            cur_max = dp[c]
        max_v[c] = cur_max
    return max_v

max1 = max_prefix(dp1)
max2 = max_prefix(dp2)
max3 = max_prefix(dp3)

# We want to maximize min(v1, v2, v3) with v1+v2+v3 <= X (calorie sum)
# Actually, we pick some calories c1, c2, c3 with c1+c2+c3 <= X
# and v1 = max1[c1], v2 = max2[c2], v3 = max3[c3]
# min(v1,v2,v3) is what we want to maximize.

# To solve efficiently:
# For each c1 in [0..X]:
#   For each c2 in [0..X - c1]:
#       c3_max = X - c1 - c2
#       v1 = max1[c1], v2 = max2[c2], v3 = max3[c3_max]
#       if any is -1, skip
#       update answer = max(answer, min(v1,v2,v3))

# This is O(X^2) = 25 million operations, which is borderline but should be okay in PyPy or with fast IO.
# We'll implement it straightforwardly.

ans = 0
for c1 in range(X+1):
    v1 = max1[c1]
    if v1 < 0:
        continue
    for c2 in range(X - c1 + 1):
        v2 = max2[c2]
        if v2 < 0:
            continue
        c3 = X - c1 - c2
        v3 = max3[c3]
        if v3 < 0:
            continue
        val = min(v1, v2, v3)
        if val > ans:
            ans = val

print(ans)