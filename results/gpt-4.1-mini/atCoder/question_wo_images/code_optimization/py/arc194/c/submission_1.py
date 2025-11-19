import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# Initial sum of C[i] where A[i] == 1
s = 0
L1 = []  # A=1, B=0 (need to flip from 1 to 0)
L2 = []  # A=0, B=1 (need to flip from 0 to 1)
L3 = []  # A=1, B=1 (can flip optionally)

for i in range(N):
    if A[i] == 1:
        s += C[i]
    if A[i] == 1 and B[i] == 0:
        L1.append(C[i])
    elif A[i] == 0 and B[i] == 1:
        L2.append(C[i])
    elif A[i] == 1 and B[i] == 1:
        L3.append(C[i])

L1.sort(reverse=True)  # flip 1->0 in descending order of cost
L2.sort()              # flip 0->1 in ascending order of cost
L3.sort(reverse=True)  # optional flips, consider from largest cost down

# Precompute prefix sums for L1, L2, L3
# For cost calculation, we need sums and prefix sums to compute efficiently

# prefix sums of L1 and L2
prefix_L1 = [0]
for x in L1:
    prefix_L1.append(prefix_L1[-1] + x)
prefix_L2 = [0]
for x in L2:
    prefix_L2.append(prefix_L2[-1] + x)
prefix_L3 = [0]
for x in L3:
    prefix_L3.append(prefix_L3[-1] + x)

# We will try all possible k = number of optional flips from L3 (0 <= k <= len(L3))
# For each k, total flips from L1 + k and L2 + k
# The order of flips is:
#   - first flip all from L1 + first k from L3 (all 1->0 flips)
#   - then flip all from L2 + first k from L3 (all 0->1 flips)
# The cost is sum of costs of each operation:
#   For each flip, cost = sum of A after flip * C_i
#   The problem reduces to:
#     For the first group (L1 + k from L3), flipping from 1->0, each flip reduces sum by the flipped cost
#     For the second group (L2 + k from L3), flipping from 0->1, each flip increases sum by the flipped cost

# We can compute cost for each k in O(1) using prefix sums and precomputed sums

lenL1 = len(L1)
lenL2 = len(L2)
lenL3 = len(L3)

# Precompute partial sums for cost calculation
# For the first group (L1 + k from L3), flips are done in descending order of cost
# cost after each flip is current sum minus the flipped cost
# total cost for first group:
#   sum_{i=0}^{m-1} (s - sum of first i flipped costs)
# = m*s - sum_{i=0}^{m-1} prefix_flipped_costs[i]
# where prefix_flipped_costs[i] = sum of first i flipped costs

# Similarly for second group (L2 + k from L3), flips done in ascending order of cost
# cost after each flip is current sum plus the flipped cost
# total cost for second group:
#   sum_{i=0}^{m-1} (s + sum of first i flipped costs)
# = m*s + sum_{i=0}^{m-1} prefix_flipped_costs[i]

# For L1 + k from L3 (descending order)
# flipped costs = L1 + first k of L3 (both descending)
# For L2 + k from L3 (ascending order)
# flipped costs = L2 + first k of L3 (both ascending)

# Precompute prefix sums for L1 + L3 (descending)
L1L3_desc = L1 + L3[:]
L1L3_desc.sort(reverse=True)
prefix_L1L3_desc = [0]
for x in L1L3_desc:
    prefix_L1L3_desc.append(prefix_L1L3_desc[-1] + x)

# Precompute prefix sums for L2 + L3 (ascending)
L2L3_asc = L2 + L3[:]
L2L3_asc.sort()
prefix_L2L3_asc = [0]
for x in L2L3_asc:
    prefix_L2L3_asc.append(prefix_L2L3_asc[-1] + x)

# We want to try k from 0 to lenL3
# For each k:
#   first group size = lenL1 + k
#   second group size = lenL2 + k
# Check if k <= lenL3 (always true)
# Calculate cost:
#   cost_first = (lenL1 + k)*s - prefix sum of first (lenL1 + k) flipped costs in L1L3_desc
#   cost_second = (lenL2 + k)*s + prefix sum of first (lenL2 + k) flipped costs in L2L3_asc
# total cost = cost_first + cost_second

# To avoid index error, ensure prefix sums arrays are large enough
# prefix_L1L3_desc length = len(L1) + len(L3) + 1
# prefix_L2L3_asc length = len(L2) + len(L3) + 1

result = 10**20
max_k = lenL3
for k in range(max_k + 1):
    m1 = lenL1 + k
    m2 = lenL2 + k
    if m1 > len(prefix_L1L3_desc) - 1 or m2 > len(prefix_L2L3_asc) - 1:
        continue
    cost_first = m1 * s - prefix_L1L3_desc[m1]
    cost_second = m2 * s + prefix_L2L3_asc[m2]
    total_cost = cost_first + cost_second
    if total_cost < result:
        result = total_cost

print(result)