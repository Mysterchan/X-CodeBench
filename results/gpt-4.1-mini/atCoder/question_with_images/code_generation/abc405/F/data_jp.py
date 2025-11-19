import sys
input = sys.stdin.readline

N, M = map(int, input().split())
segments = []
for _ in range(M):
    A, B = map(int, input().split())
    segments.append((A, B))

Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# 2N points on circle, numbered 1 to 2N clockwise
# M segments connect pairs of even points (A_i, B_i)
# No two segments share a point (no intersection or touching)
# Queries: given two odd points (C_j, D_j), count how many of the M segments share a point with the segment (C_j, D_j)

# Key observations:
# - Points are on a circle, numbered 1..2N clockwise.
# - Segments connect even points, queries connect odd points.
# - Two segments share a point if they intersect or share an endpoint.
# - Given no two segments among M share points, so M segments are pairwise disjoint chords.
# - For query segment (C_j, D_j), count how many M segments intersect or share endpoint with it.

# Since all points are on a circle, we can represent each segment as an interval on the circle.
# We fix the circle order as 1..2N clockwise.
# For a segment (x,y), define interval as the clockwise arc from x to y if x<y, else from x to y+2N (mod 2N).
# For queries, similarly define interval from C_j to D_j.

# Two chords share a point if:
# - They share an endpoint (point)
# - Or they intersect inside the circle.

# Since M segments are pairwise disjoint, no two share endpoints or intersect.

# For query segment (C_j, D_j), count how many M segments share a point with it:
# - Segments that share an endpoint with query segment (C_j or D_j)
# - Segments that intersect with query segment

# Approach:
# 1) Preprocessing:
#   - For each M segment (A_i, B_i), store interval [A_i, B_i) in clockwise order.
#   - Build two sorted lists of segment endpoints for binary search:
#     - starts: sorted list of segment start points
#     - ends: sorted list of segment end points
#   - Also build a set of endpoints of M segments for quick endpoint sharing check.

# 2) For each query (C_j, D_j):
#   - Define interval [C_j, D_j) in clockwise order.
#   - Count how many M segments intersect with this interval.
#   - Add count of segments that share endpoint with C_j or D_j.

# How to count intersecting segments efficiently?

# Since M segments are pairwise disjoint chords, their intervals do not overlap or nest.
# Actually, chords on circle with no intersection means intervals are either nested or disjoint.
# But problem states no two segments share a point, so no intersection or touching.
# So intervals are disjoint on circle.

# So M segments correspond to M disjoint intervals on circle.

# For query interval [C_j, D_j), count how many M intervals intersect it.

# Since intervals are disjoint, intersection means intervals that overlap with query interval.

# Because circle is cyclic, intervals can wrap around.

# To handle wrap-around, we can "unwrap" circle by duplicating intervals shifted by +2N.

# Steps:
# - For each segment interval [l, r), if l > r, add interval [l, r+2N)
# - Also add interval [l+2N, r+2N) to handle wrap-around queries.

# Then queries intervals [C_j, D_j) similarly handled:
# - If C_j > D_j, consider interval [C_j, D_j+2N)

# Now all intervals are on line [1..4N)

# We want to count how many M intervals intersect query interval.

# Since M intervals are disjoint, we can store intervals as (start, end) sorted by start.

# For query interval [qL, qR), count how many intervals intersect it:
# - intervals that start < qR and end > qL

# Because intervals are disjoint, intervals sorted by start, we can binary search:

# Count intervals with start < qR
# Count intervals with end <= qL (no intersection)
# Result = count_start_less_qR - count_end_less_equal_qL

# Implementation details:
# - Store intervals twice: original and shifted by +2N
# - Sort intervals by start
# - Prepare arrays starts and ends
# - For queries, adjust interval if wrap-around
# - Use bisect to count intervals intersecting query interval

# Also, count segments sharing endpoints with query endpoints:
# - For each query endpoint (odd), check if it equals any endpoint of M segments (even points)
# - Since M segments endpoints are even, and query endpoints are odd, no endpoint sharing possible.
#   So endpoint sharing count is always zero.

# But problem states "線分 i は点 A_i と点 B_i を結んでいます。ここで、A_i と B_i は相異なる 偶数 です。"
# Queries are odd points, so no endpoint sharing possible.

# So only intersection count needed.

# Final plan:
# - Build intervals for M segments (with wrap-around)
# - For each query, count intersecting intervals

import bisect

# Build intervals list
intervals = []
for A, B in segments:
    if A > B:
        B += 2 * N
    intervals.append((A, B))
# Add shifted intervals for wrap-around queries
intervals += [(l + 2 * N, r + 2 * N) for l, r in intervals]

intervals.sort(key=lambda x: x[0])
starts = [iv[0] for iv in intervals]
ends = [iv[1] for iv in intervals]

for C, D in queries:
    if C > D:
        D += 2 * N
    # Count intervals with start < D
    right = bisect.bisect_left(starts, D)
    # Count intervals with end <= C
    left = bisect.bisect_right(ends, C)
    print(right - left)