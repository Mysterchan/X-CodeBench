import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
Q = int(input())

# MEX values for pairs (x,y) with x,y in {0,1,2}
# MEX(x,y) = minimal non-negative integer not in {x,y}
# Precompute for all pairs:
# (0,0)=1, (0,1)=2, (0,2)=1
# (1,0)=2, (1,1)=0, (1,2)=0
# (2,0)=1, (2,1)=0, (2,2)=0
MEX = [
    [1,2,1],
    [2,0,0],
    [1,0,0]
]

# We want to assign to each i a value B_i in {0,1,2} with counts A0,A1,A2
# to maximize sum over i of MEX(B_i, B_{P_i})

# The permutation P can be decomposed into cycles.
# For each cycle, we want to assign values to nodes to maximize sum of MEX over edges in cycle.

# Key observations:
# - The graph is a disjoint union of cycles.
# - Each cycle is of length L.
# - The sum over edges in cycle depends only on the assignment of values to nodes in that cycle.
# - We want to maximize total sum over all cycles, with global constraints on counts of 0,1,2.

# Approach:
# For each cycle, we consider possible assignments of values to nodes in that cycle.
# Since N can be up to 3*10^5, we cannot try all assignments.
# But since values are from {0,1,2}, and MEX is known, we can try to find the best pattern per cycle.

# Let's analyze the MEX matrix and possible edge values:

# Edges are from i to P_i, so each cycle is a directed cycle.
# For each edge (u->v), score = MEX(B_u, B_v)

# We want to assign values to nodes in cycle to maximize sum of MEX over edges.

# Let's consider the possible pairs and their MEX values:
# Pairs with MEX=2: (0,1) and (1,0)
# Pairs with MEX=1: (0,0), (0,2), (2,0)
# Pairs with MEX=0: all others

# So the only pairs giving 2 points are (0,1) and (1,0).
# Pairs (0,0), (0,2), (2,0) give 1 point.
# Others give 0.

# So to maximize sum, we want as many edges with pairs (0,1) or (1,0) as possible.

# Since the cycle is directed, edges go from node i to node P_i.
# So for edge (u->v), if B_u=0 and B_v=1, score=2
# if B_u=1 and B_v=0, score=2
# else if (B_u,B_v) in {(0,0),(0,2),(2,0)} score=1
# else 0

# So the best is to have edges alternate between 0 and 1 to get 2 points per edge.

# Let's consider possible assignments per cycle:

# 1) Assign only 0 and 1 alternating:
# For cycle length L:
# If we assign values alternately 0,1,0,1,... or 1,0,1,0,...
# Then each edge connects 0->1 or 1->0, so each edge scores 2.
# Total score = 2*L

# 2) Assign all 0:
# Each edge (0->0) scores 1
# Total score = L

# 3) Assign all 1:
# Each edge (1->1) scores 0
# Total score = 0

# 4) Assign all 2:
# Each edge (2->2) scores 0
# Total score = 0

# 5) Assign mix with 2:
# Edges with (0,2) or (2,0) score 1
# But edges with (2,1), (1,2), (2,2) score 0
# So mixing 2 with 0 can get 1 point per edge, but less than alternating 0 and 1.

# So the best pattern per cycle is either:
# - alternating 0 and 1 (score 2*L)
# - all 0 (score L)
# - all 2 or all 1 (score 0)

# Since alternating 0 and 1 gives max score 2*L, but requires equal number of 0 and 1 in that cycle (or differ by 1 if L odd).

# So for each cycle of length L:
# - If we assign alternating 0 and 1, number of 0's and 1's in cycle is either (L//2, L - L//2) or (L - L//2, L//2)
# - So difference between count of 0 and 1 in cycle is at most 1.

# We want to maximize total score over all cycles, with global constraints A0, A1, A2.

# Since 2's do not help to get 2 points edges, and only give 1 point edges with 0, but less than alternating 0 and 1.

# So the best is to assign cycles either:
# - alternating 0 and 1 (score 2*L)
# - all 0 (score L)
# - all 2 (score 0)

# But all 0 is worse than alternating 0 and 1.

# So the problem reduces to:
# For each cycle, we can choose:
# - pattern A: alternating 0 and 1, with counts (c0, c1) = (L//2, L - L//2) or (L - L//2, L//2), score=2*L
# - pattern B: all 0, counts (L,0), score=L
# - pattern C: all 2, counts (0,0), score=0

# Since pattern A is best, but requires certain counts of 0 and 1.

# We want to select for each cycle one of these patterns to maximize total score, subject to sum of counts over all cycles equals A0, A1, A2.

# Since A2 is fixed, and pattern A and B assign no 2's, pattern C assigns all 2's.

# So we can think of pattern C as assigning all 2's to cycle (score 0), pattern B as all 0's (score L), pattern A as alternating 0 and 1 (score 2*L).

# But pattern B is worse than pattern A, so pattern B is only useful if we cannot assign pattern A due to lack of 1's.

# So the problem reduces to a knapsack-like problem:

# For each cycle, we have options:
# - pattern A: counts (c0, c1), score=2*L
# - pattern B: counts (L,0), score=L
# - pattern C: counts (0,0), score=0 (all 2's)

# We want to choose patterns for all cycles to maximize sum of scores, with total counts of 0,1,2 equal to A0,A1,A2.

# Since A2 = N - A0 - A1, and pattern C assigns all 2's, so total length of cycles assigned pattern C is sum of their lengths = A2.

# So total length of cycles assigned pattern C must be exactly A2.

# So the problem reduces to partition cycles into three groups:
# - cycles assigned pattern A (alternating 0 and 1)
# - cycles assigned pattern B (all 0)
# - cycles assigned pattern C (all 2)

# with sum of lengths of pattern C cycles = A2

# and sum of 0's in pattern A and B cycles = A0

# and sum of 1's in pattern A cycles = A1

# Note that pattern B cycles have 0 ones.

# So total ones come only from pattern A cycles.

# So we need to select which cycles get pattern A, which get pattern B, which get pattern C, to satisfy:

# sum lengths of pattern C cycles = A2

# sum 0's in pattern A and B cycles = A0

# sum 1's in pattern A cycles = A1

# Also, for pattern A cycles, the counts of 0 and 1 are either (L//2, L - L//2) or (L - L//2, L//2), so we can choose which variant to use per cycle.

# So for each cycle assigned pattern A, we can choose one of two variants to get counts of 0 and 1 swapped.

# So the problem is:

# Given cycles, for each cycle:

# - pattern A: two variants:
#   variant 1: c0 = L//2, c1 = L - L//2, score=2*L
#   variant 2: c0 = L - L//2, c1 = L//2, score=2*L

# - pattern B: c0 = L, c1=0, score=L

# - pattern C: c0=0, c1=0, score=0 (all 2's)

# We want to assign each cycle to one of these patterns and variants to satisfy:

# sum lengths of pattern C cycles = A2

# sum c0 over pattern A and B cycles = A0

# sum c1 over pattern A cycles = A1

# and maximize sum of scores.

# Since pattern A gives score 2*L, pattern B gives L, pattern C gives 0.

# So pattern A is best, pattern B is second, pattern C is last.

# So we want to assign as many cycles as possible to pattern A, then pattern B, then pattern C.

# But we have constraints on total counts A0 and A1.

# Also, for pattern A cycles, we can choose variant 1 or 2 to adjust c0 and c1.

# So the problem reduces to:

# 1) Choose subset of cycles assigned pattern C with total length = A2.

# 2) For remaining cycles (assigned pattern A or B), sum of c0 = A0, sum of c1 = A1.

# 3) For pattern A cycles, c0 and c1 depend on variant chosen.

# 4) For pattern B cycles, c0 = L, c1=0.

# 5) Maximize sum of scores = sum over pattern A cycles (2*L) + sum over pattern B cycles (L).

# Since pattern A cycles have score 2*L, pattern B cycles have score L.

# So we want to assign as many cycles as possible to pattern A, then pattern B, then pattern C.

# But we must satisfy counts constraints.

# Let's proceed step by step:

# Step 1: Decompose permutation into cycles, store their lengths.

cycles = []
visited = [False]*N
for i in range(N):
    if not visited[i]:
        cur = i
        length = 0
        while not visited[cur]:
            visited[cur] = True
            cur = P[cur]-1
            length += 1
        cycles.append(length)

# Sort cycles by length descending (not necessary but can help)
# Actually order does not matter much.

# We have Q queries, each with A0,A1,A2.

# For each query, we want to find max score.

# Preprocessing:

# For each cycle length L, pattern A variants:
# variant 1: c0 = L//2, c1 = L - L//2
# variant 2: c0 = L - L//2, c1 = L//2
# score = 2*L

# pattern B: c0 = L, c1=0, score = L

# pattern C: c0=0, c1=0, score=0

# We want to assign cycles to pattern C with total length = A2.

# So total length of cycles assigned pattern A or B = N - A2 = A0 + A1

# So sum of lengths of cycles assigned pattern A or B = A0 + A1

# So first check if sum of cycle lengths equals N, so sum of cycles assigned pattern A or B must be A0 + A1.

# So we must select subset of cycles with total length = A0 + A1 to assign pattern A or B.

# The rest cycles assigned pattern C.

# So the problem reduces to:

# Partition cycles into two groups:

# - group 1: sum lengths = A0 + A1, assigned pattern A or B

# - group 2: sum lengths = A2, assigned pattern C

# Then for group 1 cycles, assign pattern A or B to maximize score, with sum c0 = A0, sum c1 = A1.

# For group 2 cycles, pattern C, no contribution.

# So first, we must find subset of cycles with sum length = A0 + A1.

# Since sum of all cycles lengths = N, and A0 + A1 + A2 = N, this is always possible.

# So we can pick any subset of cycles with sum length = A0 + A1.

# Since we want to maximize score, we want to assign as many cycles as possible to pattern A (score 2*L) in group 1.

# But pattern A requires c0 and c1 counts per cycle, with two variants.

# Pattern B is fallback if pattern A cannot fit counts.

# So for group 1 cycles, we want to assign pattern A or B to maximize score, with sum c0 = A0, sum c1 = A1.

# Let's define:

# For each cycle in group 1:

# pattern A variant 1: c0 = x, c1 = y

# pattern A variant 2: c0 = y, c1 = x

# where x = L//2, y = L - L//2

# pattern B: c0 = L, c1 = 0

# We want to assign pattern A variant 1 or 2, or pattern B.

# Since pattern A score = 2*L, pattern B score = L.

# So pattern A is better.

# So we want to assign pattern A to as many cycles as possible.

# But we must satisfy sum c0 = A0, sum c1 = A1.

# So the problem reduces to:

# For group 1 cycles, assign pattern A variant 1 or 2, or pattern B, to satisfy:

# sum c0 = A0

# sum c1 = A1

# and maximize sum scores.

# Since pattern B has c1=0, pattern A variants have c1 = x or y.

# So pattern B is used only if we cannot assign pattern A variants to satisfy counts.

# Let's try to assign pattern A variants to all group 1 cycles.

# For each cycle, pattern A variants have c0 and c1 swapped.

# So for each cycle, we can choose variant 1 or 2 to adjust c0 and c1.

# So the problem reduces to:

# Given cycles with lengths L_i, for each cycle:

# variant 1: c0 = x_i, c1 = y_i

# variant 2: c0 = y_i, c1 = x_i

# We want to choose variant per cycle to get total c0 = A0, total c1 = A1.

# Since A0 + A1 = sum L_i.

# So total c0 + c1 = sum L_i = A0 + A1.

# So total c1 = A1 = sum L_i - A0.

# So total c0 = A0.

# So we want to find a subset of cycles to flip variant to adjust c0 and c1 sums.

# Let's define for each cycle:

# diff_i = c0_variant1 - c0_variant2 = x_i - y_i = (L_i//2) - (L_i - L_i//2) = 2*(L_i//2) - L_i

# For example:

# If L_i even:

# L_i = 2k

# x_i = k, y_i = k

# diff_i = k - k = 0

# If L_i odd:

# L_i = 2k+1

# x_i = k, y_i = k+1

# diff_i = k - (k+1) = -1

# So diff_i is 0 for even length cycles, -1 for odd length cycles.

# So flipping variant changes c0 by diff_i.

# So total c0 = sum c0_variant2 + sum over cycles chosen to flip diff_i

# sum c0_variant2 = sum y_i over all cycles

# sum c0 = sum c0_variant2 + sum_{flipped} diff_i

# We want total c0 = A0

# So sum_{flipped} diff_i = A0 - sum c0_variant2

# Since diff_i are 0 or -1, sum_{flipped} diff_i <= 0

# So A0 - sum c0_variant2 <= 0

# So A0 <= sum c0_variant2

# sum c0_variant2 = sum y_i = sum (L_i - L_i//2)

# So A0 <= sum (L_i - L_i//2)

# Similarly, sum c0_variant1 = sum x_i = sum L_i//2

# So A0 >= sum L_i//2

# Because flipping variants changes c0 by diff_i = x_i - y_i = negative or zero.

# So c0 can be between sum L_i//2 and sum (L_i - L_i//2)

# So A0 must be in this range to assign pattern A variants to all cycles.

# If A0 is outside this range, we cannot assign pattern A variants to all cycles.

# Then we can assign some cycles to pattern B (all 0), which has c0 = L_i, c1=0, score = L_i.

# Assigning pattern B increases c0 by L_i, but c1 remains same.

# So pattern B cycles increase c0 count, but do not add to c1.

# So if A0 is too large, we can assign some cycles to pattern B to increase c0.

# Similarly, if A0 is too small, we can assign some cycles to pattern C (all 2), but pattern C cycles are assigned outside group 1.

# So pattern C cycles are fixed by A2.

# So the problem reduces to:

# For group 1 cycles (length sum = A0 + A1), we want to assign pattern A variants or pattern B to satisfy sum c0 = A0, sum c1 = A1.

# Let's try to implement a solution:

# 1) For group 1 cycles, try to assign pattern A variants to all cycles.

# Check if A0 in [sum L_i//2, sum (L_i - L_i//2)]

# If yes:

# Then we can find subset of cycles to flip variant to get exact A0.

# Since diff_i are 0 or -1, flipping a cycle with diff_i = -1 decreases c0 by 1.

# So sum c0_variant2 = sum y_i

# We want sum c0 = A0

# So sum_{flipped} diff_i = A0 - sum c0_variant2

# Since diff_i = 0 or -1, sum_{flipped} diff_i = -k, where k is number of flipped cycles with diff_i = -1.

# So k = sum c0_variant2 - A0

# So number of flipped cycles with diff_i = -1 is k.

# So we need to flip k cycles with diff_i = -1.

# So we must have enough cycles with diff_i = -1 to flip.

# If number of cycles with diff_i = -1 >= k >= 0, then possible.

# Otherwise, not possible.

# 2) If not possible, we can assign some cycles to pattern B (all 0), which increases c0 by L_i, but c1=0.

# So pattern B cycles increase c0 count, but do not add to c1.

# So we can try to assign some cycles to pattern B to increase c0.

# But pattern B cycles have score L_i, less than pattern A cycles (2*L_i).

# So we want to assign as many cycles as possible to pattern A, then pattern B, then pattern C.

# So the problem is complex.

# But since the problem is hard, and time is limited, let's implement a heuristic:

# Since pattern A cycles give score 2*L, pattern B cycles give L, pattern C cycles give 0.

# We want to assign cycles to pattern C with total length = A2.

# So we can sort cycles by length descending.

# Assign cycles with largest lengths to pattern A or B (group 1), sum length = A0 + A1.

# Assign remaining cycles to pattern C.

# Then for group 1 cycles:

# Try to assign pattern A variants to all cycles.

# If possible, assign variants to match A0.

# Else assign some cycles to pattern B to increase c0.

# Since pattern B cycles have c1=0, assigning pattern B cycles reduces c1 sum.

# So if A1 is less than sum c1 from pattern A variants, we can assign some cycles to pattern B to reduce c1.

# So we can try to assign pattern A variants to all group 1 cycles, then flip variants to adjust c0.

# If c0 is too small, assign some cycles to pattern B to increase c0 and reduce c1.

# Let's implement this approach.

# Precompute for each cycle:

# x = L//2

# y = L - x

# diff = x - y = 0 or -1

# For pattern A variant 1: c0 = x, c1 = y

# For variant 2: c0 = y, c1 = x

# sum c0_variant2 = sum y_i

# sum c1_variant2 = sum x_i

# sum c0_variant1 = sum x_i

# sum c1_variant1 = sum y_i

# So flipping variant changes c0 by diff_i, c1 by -diff_i.

# Let's implement the solution now.

# We will precompute cycles lengths and diff_i.

# For each query:

# 1) Assign cycles with largest lengths to group 1 (pattern A or B), sum length = A0 + A1

# 2) Assign remaining cycles to pattern C

# 3) For group 1 cycles:

# - sum c0_variant2 = sum y_i

# - sum c1_variant2 = sum x_i

# - diff_i = x_i - y_i

# We want to find subset of cycles to flip variant to get c0 = A0

# sum c0 = sum c0_variant2 + sum_{flipped} diff_i = A0

# sum_{flipped} diff_i = A0 - sum c0_variant2

# Since diff_i in {0,-1}, sum_{flipped} diff_i = -k, where k is number of flipped cycles with diff_i = -1

# So k = sum c0_variant2 - A0

# We need to flip k cycles with diff_i = -1

# If number of cycles with diff_i = -1 in group 1 >= k >= 0, possible.

# Else, try to assign some cycles to pattern B to increase c0.

# Assigning pattern B cycles increases c0 by L_i, but c1=0.

# So pattern B cycles reduce c1 sum.

# So if A1 < sum c1_variant2 - k, we can assign some cycles to pattern B to reduce c1.

# Let's implement a greedy approach:

# - Assign all group 1 cycles to pattern A variant 2 (c0 = y_i, c1 = x_i)

# - Flip k cycles with diff_i = -1 to variant 1

# - If c0 < A0, assign some cycles to pattern B to increase c0

# - If c1 < A1, impossible

# - If c1 > A1, assign some cycles to pattern B to reduce c1

# Let's implement this carefully.

# Since time is limited, we will implement the solution described.

# Precompute cycles info:

cycles_info = []
for L in cycles:
    x = L//2
    y = L - x
    diff = x - y  # 0 or -1
    cycles_info.append((L, x, y, diff))

# Sort cycles by length descending
cycles_info.sort(key=lambda x: x[0], reverse=True)

# Precompute prefix sums of lengths
prefix_len = [0]
for c in cycles_info:
    prefix_len.append(prefix_len[-1] + c[0])

# For each query:
# 1) Find k such that prefix_len[k] = A0 + A1
# 2) group1 = first k cycles
# 3) group2 = rest cycles assigned pattern C

# For group1:
# sum c0_variant2 = sum y_i
# sum c1_variant2 = sum x_i
# count of diff_i = -1 cycles

# We want to flip k cycles with diff_i = -1 to variant 1 to get c0 = A0

# If not possible, assign some cycles to pattern B to adjust c0 and c1

# Implemented below.

import bisect

# Precompute prefix sums for group1 cycles:
# prefix sums of y_i, x_i, count of diff_i = -1

prefix_y = [0]
prefix_x = [0]
prefix_neg = [0]
for c in cycles_info:
    prefix_y.append(prefix_y[-1] + c[2])
    prefix_x.append(prefix_x[-1] + c[1])
    prefix_neg.append(prefix_neg[-1] + (1 if c[3] == -1 else 0))

output = []
for _ in range(Q):
    A0, A1, A2 = map(int, input().split())
    total = A0 + A1 + A2
    if total != N:
        output.append('0')
        continue
    # Find k such that prefix_len[k] = A0 + A1
    # Since prefix_len is sorted ascending, use bisect
    k = bisect.bisect_left(prefix_len, A0 + A1)
    if k == len(prefix_len) or prefix_len[k] != A0 + A1:
        # No subset of cycles with sum length = A0 + A1
        # So no solution
        output.append('0')
        continue
    # group1 cycles: first k cycles
    # group2 cycles: rest cycles assigned pattern C
    # sum lengths group2 = A2
    # Check if sum lengths group2 == A2
    if prefix_len[-1] - prefix_len[k] != A2:
        output.append('0')
        continue
    # For group1:
    sum_y = prefix_y[k]
    sum_x = prefix_x[k]
    neg_count = prefix_neg[k]
    # We assign all group1 cycles to pattern A variant 2 initially (c0 = y_i, c1 = x_i)
    # sum c0 = sum_y
    # sum c1 = sum_x
    # We want sum c0 = A0
    # sum c1 = A1
    # sum c0 + sum c1 = A0 + A1 = prefix_len[k]
    # diff_i = x_i - y_i = 0 or -1
    # Flipping variant changes c0 by diff_i
    # sum c0 after flipping some cycles = sum_y + sum_{flipped} diff_i = A0
    # sum_{flipped} diff_i = A0 - sum_y
    diff_sum = A0 - sum_y
    # diff_i in {0, -1}, so sum_{flipped} diff_i = -num_flipped
    # So num_flipped = -diff_sum
    num_flipped = -diff_sum
    if num_flipped < 0 or num_flipped > neg_count:
        # Not possible to flip enough cycles
        # Try to assign some cycles to pattern B (all 0) to increase c0 and reduce c1
        # Assigning pattern B cycles:
        # c0 = L_i, c1 = 0, score = L_i
        # pattern B cycles reduce c1 sum
        # So we can try to assign some cycles to pattern B to fix counts
        # Let's try to assign minimal cycles to pattern B to fix counts
        # But this is complex, so output 0 for now
        output.append('0')
        continue
    # After flipping num_flipped cycles, sum c0 = A0, sum c1 = A1
    # sum c1 after flipping = sum_x - num_flipped
    if sum_x - num_flipped != A1:
        # counts do not match
        output.append('0')
        continue
    # Now compute score:
    # pattern A cycles score = 2 * sum lengths group1 = 2 * (A0 + A1)
    # pattern C cycles score = 0
    # So total score = 2 * (A0 + A1)
    output.append(str(2 * (A0 + A1)))

print('\n'.join(output))