import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())
P = list(map(int, input().split()))

# We want to maximize sum of k_i where sum of k_i^2 * P_i <= M
# For each product i, cost per unit squared is P_i.
# The problem reduces to finding max total units K such that sum over i of k_i^2 * P_i <= M.

# Key insight:
# For fixed total units K, the minimal cost is achieved by distributing units to minimize sum(k_i^2 * P_i).
# Using Lagrange multipliers, optimal k_i = sqrt(M / (lambda * P_i)) and sum k_i = K.
# From this, k_i = K / sum_j sqrt(P_j) * 1/sqrt(P_i)
# So cost = sum k_i^2 * P_i = K^2 / (sum_j sqrt(P_j))^2 * sum_i P_i / P_i = K^2 / (sum_j sqrt(P_j))^2 * N
# Actually, cost = K^2 / (sum_j sqrt(P_j))^2 * sum_i P_i / P_i = K^2 / (sum_j sqrt(P_j))^2 * N (since P_i/P_i=1)
# This is incorrect, let's re-derive carefully:

# Let S = sum_i sqrt(P_i)
# k_i = K * (1/sqrt(P_i)) / S
# cost = sum_i (k_i^2 * P_i) = sum_i (K^2 * (1/sqrt(P_i))^2 / S^2 * P_i) = K^2 / S^2 * sum_i (P_i / P_i) = K^2 / S^2 * N
# So cost = K^2 * N / S^2

# So cost = K^2 * N / (sum_i sqrt(P_i))^2 <= M
# => K <= sqrt(M * (sum_i sqrt(P_i))^2 / N)

# But this is a lower bound on cost, because k_i must be integers.

# Since k_i must be integers, we can do binary search on total units K:
# For given K, minimal cost is sum_i (ceil(k_i)^2 * P_i) where k_i = K * (1/sqrt(P_i)) / S
# But ceil(k_i) can be approximated by floor(k_i) or floor(k_i)+1.

# To check feasibility for given K:
# 1. Compute ideal k_i = K * (1/sqrt(P_i)) / S
# 2. Try floor(k_i) for all i, sum floor(k_i) = sum_floor
# 3. If sum_floor < K, assign the remaining units to products with minimal incremental cost:
#    incremental cost of adding one unit to product i is (2*k_i + 1)*P_i where k_i is current units assigned.
# 4. Calculate total cost and check if <= M.

# This approach is O(N log K), which is efficient for constraints.

sqrtP = [math.sqrt(p) for p in P]
S = sum(sqrtP)

def cost_for_k(k):
    # Compute ideal distribution
    ideal = [k * (1 / sp) / S for sp in sqrtP]
    floor_k = [int(x) for x in ideal]
    sum_floor = sum(floor_k)
    rem = k - sum_floor

    # Calculate cost with floor_k
    cost = 0
    for i in range(N):
        cost += floor_k[i] * floor_k[i] * P[i]

    if rem == 0:
        return cost

    # Calculate incremental costs for adding one more unit to each product
    # incremental cost = (2 * floor_k[i] + 1) * P[i]
    inc = []
    for i in range(N):
        inc.append(((2 * floor_k[i] + 1) * P[i], i))
    inc.sort()

    for i in range(rem):
        cost += inc[i][0]
        if cost > M:
            return cost
    return cost

left, right = 0, 10**15  # large upper bound

while left < right:
    mid = (left + right + 1) // 2
    if cost_for_k(mid) <= M:
        left = mid
    else:
        right = mid - 1

print(left)