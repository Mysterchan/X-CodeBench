import sys
input = sys.stdin.readline

N, X = map(int, input().split())
products = [[], [], []]  # products by vitamin: index 0 for vit1, 1 for vit2, 2 for vit3

for _ in range(N):
    V, A, C = map(int, input().split())
    products[V-1].append((A, C))

# For each vitamin, we want to know the minimal calories needed to get at least k units of that vitamin.
# We'll build dp arrays for each vitamin:
# dp_vit[i] = minimal calories to get exactly i units of that vitamin (or inf if impossible)
# Then we convert dp_vit to minimal calories to get at least i units by suffix min.

INF = 10**15

def build_dp(items):
    # items: list of (A_i, C_i)
    max_sum = sum(a for a, c in items)
    dp = [INF] * (max_sum + 1)
    dp[0] = 0
    for a, c in items:
        for j in range(max_sum - a, -1, -1):
            if dp[j] != INF:
                val = dp[j] + c
                if val < dp[j + a]:
                    dp[j + a] = val
    # Convert dp to minimal calories to get at least i units
    for i in range(max_sum - 1, -1, -1):
        if dp[i+1] < dp[i]:
            dp[i] = dp[i+1]
    return dp

dp1 = build_dp(products[0])
dp2 = build_dp(products[1])
dp3 = build_dp(products[2])

max_vit1 = len(dp1) - 1
max_vit2 = len(dp2) - 1
max_vit3 = len(dp3) - 1

# We want to maximize m = min(vit1, vit2, vit3) such that
# there exist v1,v2,v3 >= m with dp1[v1] + dp2[v2] + dp3[v3] <= X
# Since dp arrays are minimal calories to get at least v units,
# and dp arrays are non-increasing in calories as v decreases,
# we can try m from high to low and check if there is a combination with all >= m.

# For fixed m, minimal calories to get at least m units of each vitamin:
# dp1[m], dp2[m], dp3[m]
# sum = dp1[m] + dp2[m] + dp3[m]
# If sum <= X, answer >= m

# But dp arrays might be shorter than m, so if m > max_vit, dp_vit[m] = INF

ans = 0
max_m = min(max_vit1, max_vit2, max_vit3)
for m in range(max_m, -1, -1):
    c1 = dp1[m] if m <= max_vit1 else INF
    c2 = dp2[m] if m <= max_vit2 else INF
    c3 = dp3[m] if m <= max_vit3 else INF
    if c1 == INF or c2 == INF or c3 == INF:
        continue
    if c1 + c2 + c3 <= X:
        ans = m
        break

print(ans)