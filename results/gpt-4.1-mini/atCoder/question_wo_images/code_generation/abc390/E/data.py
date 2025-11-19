import sys
input = sys.stdin.readline

N, X = map(int, input().split())
foods = [[], [], []]  # foods[0] for vitamin 1, foods[1] for vitamin 2, foods[2] for vitamin 3

for _ in range(N):
    V, A, C = map(int, input().split())
    foods[V-1].append((A, C))

# For each vitamin, we want to know the minimum calories needed to get at least a certain amount of that vitamin.
# We'll do a knapsack-like DP for each vitamin separately:
# dp_v[i] = minimum calories to get exactly i units of vitamin v (or inf if impossible)
# Then we can query for any target amount how many calories are needed.

INF = 10**15

def knapsack_min_calories(items):
    # items: list of (A_i, C_i)
    # max_sum = sum of all A_i
    max_sum = sum(a for a, c in items)
    dp = [INF] * (max_sum + 1)
    dp[0] = 0
    for a, c in items:
        for j in range(max_sum - a, -1, -1):
            if dp[j] != INF:
                val = dp[j] + c
                if val < dp[j + a]:
                    dp[j + a] = val
    return dp

dp1 = knapsack_min_calories(foods[0])
dp2 = knapsack_min_calories(foods[1])
dp3 = knapsack_min_calories(foods[2])

# We want to maximize m = min(vit1, vit2, vit3) such that dp1[vit1] + dp2[vit2] + dp3[vit3] <= X
# Since min(vit1, vit2, vit3) = m, we want vit1 >= m, vit2 >= m, vit3 >= m
# So for each m, check if there exist vit1, vit2, vit3 >= m with dp1[vit1] + dp2[vit2] + dp3[vit3] <= X
# To optimize, for each dp array, we can precompute the minimal calories to get at least i units:
# min_cal[i] = min_{j >= i} dp[j]

def min_calories_at_least(dp):
    n = len(dp)
    min_cal = [INF] * n
    min_cal[-1] = dp[-1]
    for i in range(n-2, -1, -1):
        min_cal[i] = min(min_cal[i+1], dp[i])
    return min_cal

min_cal1 = min_calories_at_least(dp1)
min_cal2 = min_calories_at_least(dp2)
min_cal3 = min_calories_at_least(dp3)

max_m = 0
max_possible = min(len(min_cal1), len(min_cal2), len(min_cal3)) - 1

for m in range(max_possible + 1):
    cals = min_cal1[m] + min_cal2[m] + min_cal3[m]
    if cals <= X:
        max_m = m

print(max_m)