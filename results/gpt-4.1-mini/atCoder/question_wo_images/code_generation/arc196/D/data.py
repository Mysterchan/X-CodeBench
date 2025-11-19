import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
people = [tuple(map(int, input().split())) for _ in range(M)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Explanation and approach:
# Each person i travels from S_i to T_i along the shortest path (adjacent towns).
# Their stamina starts at 0 at S_i, ends at 0 at T_i, and is positive at all intermediate towns.
# The stamina changes by w_j on road j (between town j and j+1).
#
# Let prefix sums of w_j be P:
# P[0] = 0
# P[i] = w_1 + w_2 + ... + w_i for i=1..N-1
#
# Stamina at town x = P[x-1] - P[S_i-1] if traveling from S_i to T_i (assuming S_i < T_i)
# or P[S_i-1] - P[x-1] if S_i > T_i (reverse direction)
#
# Conditions:
# - stamina at S_i = 0
# - stamina at T_i = 0
# - stamina at intermediate towns > 0
#
# This means the partial sums between S_i and T_i must be strictly positive except at ends.
#
# Define interval [l, r] = sorted(S_i, T_i)
# The partial sums P[l-1], P[l], ..., P[r-1] must form a "mountain":
# P[l-1] = P[r-1] (start and end equal)
# P[k] > P[l-1] for all k in (l-1, r-1)
#
# So for each person i, the subarray P[l-1..r-1] must have:
# - P[l-1] = P[r-1]
# - min(P[l..r-2]) > P[l-1]
#
# Since P[l-1] = P[r-1], the difference P[r-1] - P[l-1] = 0.
#
# The problem reduces to checking if there exists an assignment of w_j (and thus P) satisfying all these constraints simultaneously.
#
# Key insight:
# For each person i, the interval [l, r] must have:
# min(P[l..r-2]) > P[l-1] = P[r-1]
#
# This means inside the interval, P is strictly greater than the boundary value.
#
# If two intervals overlap in a way that contradicts these conditions, no solution.
#
# The problem asks for queries on subranges of people: for people L_k to R_k, is it possible?
#
# We will:
# 1. For each person i, store interval [l_i, r_i] = sorted(S_i, T_i)
# 2. Check for contradictions between intervals in the query range.
#
# Contradiction arises if intervals overlap improperly.
#
# More concretely:
# - For intervals [l_i, r_i], the condition is that inside the interval, P is strictly greater than boundary.
# - If intervals overlap partially, the conditions may conflict.
#
# We can model this as a problem of checking if intervals are "nested" or "disjoint".
#
# If intervals are nested or disjoint, no contradiction.
# If intervals partially overlap (intersect but neither contains the other), contradiction.
#
# So the problem reduces to checking if the intervals in the query form a laminar family (no partial overlaps).
#
# To answer queries efficiently:
# - Sort people by their intervals' start.
# - For each prefix, maintain the maximum right endpoint seen so far.
# - For each person i, if l_i < max_right_so_far < r_i, then partial overlap occurs -> contradiction.
#
# We can precompute for each i the earliest index j > i where contradiction occurs.
# Then for each query [L, R], if contradiction index <= R, answer No; else Yes.
#
# Implementation details:
# - Sort people by l_i
# - Use a stack to detect partial overlaps:
#   For each interval in order:
#     While stack top's r_i < current l_i, pop stack (no overlap)
#     If stack top's r_i > current l_i and stack top's r_i < current r_i => partial overlap => contradiction
#     Push current interval
#
# We record for each i the earliest contradiction index.
#
# Then build a segment tree or prefix array to answer queries in O(1).
#

intervals = []
for i, (S, T) in enumerate(people):
    l, r = sorted((S, T))
    intervals.append((l, r, i))

# Sort by l
intervals.sort(key=lambda x: x[0])

contradiction_pos = [M+1] * M  # contradiction_pos[i] = earliest index j > i where contradiction occurs

stack = []  # will store (r, i) in increasing order of r
# We'll process intervals in order of l
# For each interval, check partial overlap with stack top
# If partial overlap found, record contradiction

# To map back to original indices, we keep track of i
for idx, (l, r, i) in enumerate(intervals):
    while stack and stack[-1][0] < l:
        stack.pop()
    if stack:
        top_r, top_i = stack[-1]
        # partial overlap if top_r > l and top_r < r
        if top_r > l and top_r < r:
            # contradiction between i and top_i
            # record contradiction positions
            # contradiction affects both intervals
            # We record the earliest contradiction index for both
            # Since intervals are sorted by l, idx > position of top_i in intervals
            # We want to record contradiction_pos for the smaller index in original order
            # We'll record contradiction_pos for both i and top_i as min of current and the other index
            # But to answer queries, we only need the earliest contradiction index for each i
            # We'll record contradiction_pos[i] = min(contradiction_pos[i], top_i)
            # and contradiction_pos[top_i] = min(contradiction_pos[top_i], i)
            # But i and top_i are original indices, not sorted indices
            # We need a mapping from original index to sorted index and vice versa
            # Let's create a map from original index to sorted index
            pass
    stack.append((r, i))

# The above approach needs to know the sorted index of top_i and i to record contradiction_pos properly.
# Let's create a mapping from original index to sorted index:
orig_to_sorted = [0]*M
for sorted_idx, (_, _, i) in enumerate(intervals):
    orig_to_sorted[i] = sorted_idx

contradiction_pos = [M+1]*M

stack = []
for sorted_idx, (l, r, i) in enumerate(intervals):
    while stack and stack[-1][0] < l:
        stack.pop()
    if stack:
        top_r, top_i = stack[-1]
        if top_r > l and top_r < r:
            # partial overlap between intervals i and top_i
            # record contradiction positions
            # contradiction_pos for both intervals is min of current and the other's sorted index
            # We want to record the earliest contradiction index for each original index
            # contradiction_pos[i] = min(contradiction_pos[i], orig_to_sorted[top_i])
            # contradiction_pos[top_i] = min(contradiction_pos[top_i], sorted_idx)
            contradiction_pos[i] = min(contradiction_pos[i], orig_to_sorted[top_i])
            contradiction_pos[top_i] = min(contradiction_pos[top_i], sorted_idx)
    stack.append((r, i))

# contradiction_pos[i] now stores the earliest sorted index of contradiction for interval i
# If contradiction_pos[i] > M, no contradiction for i

# We want to answer queries on original indices [L, R]
# For each i in [L, R], if contradiction_pos[i] <= R-1 (0-based), then No else Yes
# But contradiction_pos[i] is in sorted index, queries are in original index order
# So we need to map contradiction_pos[i] back to original index order

# Actually, queries are on original indices L_k, R_k (1-based)
# We want to know if any contradiction occurs inside [L_k-1, R_k-1]

# To do this efficiently:
# For each i in original order, we have contradiction_pos[i] in sorted index
# We want to transform contradiction_pos[i] to original index order to compare with R_k

# Let's create an array contradiction_pos_orig indexed by original index:
# contradiction_pos_orig[i] = the minimal original index j where contradiction occurs with i
# We have contradiction_pos[i] in sorted index, so we convert it back to original index:
contradiction_pos_orig = [M+1]*M
for i in range(M):
    cpos = contradiction_pos[i]
    if cpos <= M-1:
        # cpos is sorted index, convert to original index
        _, _, orig_j = intervals[cpos]
        contradiction_pos_orig[i] = orig_j
    else:
        contradiction_pos_orig[i] = M+1

# Now for each i, contradiction_pos_orig[i] = earliest original index j where contradiction occurs with i
# If contradiction_pos_orig[i] > M, no contradiction

# For queries [L, R], we want to check if there exists i in [L-1, R-1] with contradiction_pos_orig[i] in [L-1, R-1]
# i.e. contradiction_pos_orig[i] <= R-1 and contradiction_pos_orig[i] >= L-1

# To answer queries efficiently:
# For each i, define bad[i] = contradiction_pos_orig[i] if contradiction_pos_orig[i] <= M else M+1
# We want to check if min bad[i] for i in [L-1, R-1] <= R-1 and >= L-1

# We can build a segment tree or sparse table for bad array to get min in O(1)

# But we also need to check if min bad[i] in [L-1, R-1] is >= L-1

# So for each query:
# min_bad = min bad[i] for i in [L-1, R-1]
# if min_bad <= R-1 and min_bad >= L-1 => No else Yes

# Build segment tree for min query on bad

import math

size = 1 << (M-1).bit_length()
seg = [M+1]*(2*size)

for i in range(M):
    seg[size+i] = contradiction_pos_orig[i]
for i in range(size-1, 0, -1):
    seg[i] = min(seg[2*i], seg[2*i+1])

def query(l, r):
    # min in [l, r)
    l += size
    r += size
    res = M+1
    while l < r:
        if l & 1:
            res = min(res, seg[l])
            l += 1
        if r & 1:
            r -= 1
            res = min(res, seg[r])
        l >>= 1
        r >>= 1
    return res

for L, R in queries:
    L -= 1
    # query min bad in [L, R)
    min_bad = query(L, R)
    if L <= min_bad <= R-1:
        print("No")
    else:
        print("Yes")