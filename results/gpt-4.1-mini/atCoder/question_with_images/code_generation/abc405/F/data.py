import sys
input = sys.stdin.readline

N, M = map(int, input().split())
segments = []
for _ in range(M):
    A, B = map(int, input().split())
    if A > B:
        A, B = B, A
    segments.append((A, B))

Q = int(input())
queries = []
for _ in range(Q):
    C, D = map(int, input().split())
    if C > D:
        C, D = D, C
    queries.append((C, D))

# Key observations:
# - Points are on a circle numbered 1 to 2N.
# - M segments connect even points, no two segments share a point.
# - Queries ask how many of these M segments share a point with the segment connecting two odd points.
# - Two segments share a point if they intersect on the circle.
#
# Since no two segments share a point, the M segments form a matching on even points.
# The queries are segments between odd points.
#
# We want to count how many of the M segments intersect the query segment.
#
# Intersection on circle:
# For two chords (a,b) and (c,d) on circle with points numbered clockwise,
# they intersect if and only if the points are interleaved in order:
# a < c < b < d or c < a < d < b (mod 2N)
#
# We can fix the numbering from 1 to 2N clockwise.
#
# Approach:
# 1. For each segment (A_i, B_i), A_i < B_i, store it.
# 2. For each query (C_j, D_j), C_j < D_j.
#
# We want to count how many segments (A_i, B_i) satisfy:
# (C_j < A_i < D_j < B_i) or (A_i < C_j < B_i < D_j)
#
# Because points are on a circle, we consider intervals modulo 2N.
#
# To handle the circular nature, we can "unwrap" the circle by doubling the numbering:
# Consider points 1..2N and then 2N+1..4N as a copy of 1..2N.
#
# For each segment (A_i, B_i), we add (A_i, B_i) and (A_i+2N, B_i+2N).
# For each query (C_j, D_j), if C_j < D_j, interval is straightforward.
# If C_j > D_j (not in input since C_j < D_j guaranteed), we would handle wrap-around.
#
# But input guarantees C_j < D_j and A_i < B_i.
#
# So we can treat the circle as a line from 1 to 4N (duplicated).
#
# Then, for each query segment (C_j, D_j), we want to count how many segments (A_i, B_i)
# satisfy the intersection condition.
#
# Let's analyze intersection condition more carefully:
#
# Since segments connect even points and queries connect odd points,
# segments and queries do not share endpoints.
#
# The intersection condition for chords on circle with points numbered 1..2N clockwise:
# Two chords (a,b) and (c,d) intersect iff the endpoints are interleaved:
# a < c < b < d or c < a < d < b (mod 2N)
#
# Since all points are distinct and no two segments share endpoints,
# we can use the linear order 1..2N and check the condition directly.
#
# So for each query (C,D), count segments (A,B) with:
# (C < A < D < B) or (A < C < B < D)
#
# We can split the problem into two parts:
# Count segments with A in (C,D) and B > D
# Count segments with B in (C,D) and A < C
#
# We can pre-process segments sorted by A and by B.
#
# For each query:
# - Count segments with A in (C,D) and B > D
# - Count segments with B in (C,D) and A < C
#
# Implementation plan:
# - Sort segments by A
# - For queries, for the first count:
#   - Find segments with A in (C,D)
#   - Among them, count how many have B > D
# - Similarly for second count:
#   - Sort segments by B
#   - Find segments with B in (C,D)
#   - Among them, count how many have A < C
#
# To answer these efficiently, we can:
# - For segments sorted by A, build a Fenwick tree (BIT) over B values.
# - For segments sorted by B, build a Fenwick tree over A values.
#
# But B and A can be up to 2N (up to 2*10^6), so Fenwicks of size 2N are feasible.
#
# Steps:
# 1. Sort segments by A ascending.
# 2. For each segment in order, update Fenwicks.
# 3. For queries, binary search to find segments with A in (C,D).
# 4. For those segments, count how many have B > D.
#
# Similarly for B.
#
# But we have M up to 2*10^5, so we can compress coordinates of A and B.
#
# Let's proceed with coordinate compression of A and B.
#
# Then build two arrays:
# - segments sorted by A: list of (A, B)
# - segments sorted by B: list of (B, A)
#
# For queries:
# - For first count:
#   - Find indices l and r in segments_by_A where A in (C,D)
#   - For segments in that range, count how many have B > D
# - For second count:
#   - Find indices l and r in segments_by_B where B in (C,D)
#   - For segments in that range, count how many have A < C
#
# To answer these counts efficiently, we can:
# - For segments_by_A, build a Fenwick tree over B values.
# - For segments_by_B, build a Fenwick tree over A values.
#
# But queries are online, so we need a data structure to answer range queries.
#
# Alternative approach:
# Since M and Q are large, we can process queries offline.
#
# Offline approach:
# - For first count:
#   - For each query, we want to count segments with A in (C,D) and B > D.
#   - We can process queries sorted by D ascending.
#   - For segments sorted by A ascending:
#     - For each segment with A <= D, add B to Fenwick tree.
#   - For each query with D, count how many segments with A in (C,D) and B > D.
#     - For A in (C,D), we can find indices in segments_by_A.
#     - For B > D, we can query Fenwick tree for B > D.
#
# Similarly for second count.
#
# Let's implement this offline approach.
#
# Steps:
# 1. Coordinate compress A and B.
# 2. Sort segments by A.
# 3. Sort queries by D.
# 4. For first count:
#    - For each query in order of increasing D:
#      - Add segments with A <= D to Fenwick tree (indexed by B).
#      - Query Fenwick tree for B > D and A in (C,D).
#      - To get A in (C,D), we can binary search segments_by_A for indices of A > C and A <= D.
#      - For those segments, we have added B to Fenwick tree.
#      - So we can query Fenwick tree for B > D.
#
# But Fenwick tree is 1D, we need 2D range query: A in (C,D) and B > D.
#
# This is complex.
#
# Alternative approach:
# Since no two segments share a point, segments form a matching on even points.
#
# Let's consider the circle and the order of points.
#
# Another approach:
# For each segment (A,B), define interval (A,B).
# For each query (C,D), define interval (C,D).
#
# The intersection condition is:
# segments intersect if and only if one endpoint of the query segment lies inside the segment interval and the other lies outside.
#
# So for segment (A,B) and query (C,D):
# They intersect if and only if exactly one of C and D lies in (A,B) interval.
#
# Because points are on circle, intervals wrap around.
#
# Let's define a function inside(x, l, r):
# returns True if x in interval (l,r) clockwise on circle.
#
# Since points are numbered 1..2N clockwise,
# inside(x,l,r) = True if going clockwise from l to r, x is encountered.
#
# If l < r:
#   inside(x,l,r) = (l < x < r)
# else:
#   inside(x,l,r) = (x > l or x < r)
#
# Then segments (A,B) and (C,D) intersect iff inside(C,A,B) != inside(D,A,B)
#
# So for each query (C,D), count how many segments (A,B) satisfy inside(C,A,B) != inside(D,A,B).
#
# We can pre-process segments intervals.
#
# For each segment (A,B), store interval (A,B).
#
# For each query (C,D), count segments where inside(C,A,B) != inside(D,A,B).
#
# We can process queries offline:
#
# For each segment (A,B), mark interval (A,B).
#
# For each query (C,D), we want to count segments where inside(C,A,B) != inside(D,A,B).
#
# Let's fix the circle as 1..2N.
#
# For each segment (A,B), interval (A,B) is clockwise from A to B.
#
# For each query (C,D), we want to count segments where inside(C,A,B) != inside(D,A,B).
#
# Let's consider the points on circle as a line 1..2N with wrap.
#
# We can map intervals to ranges on 1..2N.
#
# For each segment (A,B), interval (A,B) is:
# if A < B: interval is (A,B)
# else: interval is (A, B+2N) (wrap around)
#
# Similarly for points C and D.
#
# Let's double the circle to 1..4N.
#
# For each segment (A,B):
# if A < B:
#   interval is (A,B)
# else:
#   interval is (A, B+2N)
#
# For each query (C,D):
# if C < D:
#   points are C and D
# else:
#   D = D + 2N (to unwrap)
#
# Then inside(x,A,B) = True if x in (A,B)
#
# So inside(C,A,B) != inside(D,A,B) means exactly one of C and D lies in (A,B).
#
# So for each query, count segments whose interval contains exactly one of C or D.
#
# We can process this by:
#
# For each segment interval (l,r), mark +1 at l+1 and -1 at r (prefix sums).
#
# Then for each point x, prefix sum gives how many intervals contain x.
#
# But we want to count segments whose interval contains exactly one of C or D.
#
# So for each query:
# answer = count_intervals_containing_C + count_intervals_containing_D - 2 * count_intervals_containing_both_C_and_D
#
# But intervals are disjoint (no two segments share points), so intervals do not overlap at endpoints.
#
# But intervals can overlap.
#
# However, since segments do not share points, intervals do not share endpoints.
#
# So count_intervals_containing_both_C_and_D = count_intervals_containing_interval (C,D)
#
# But C and D are odd points, segments connect even points, so intervals are on even points.
#
# So intervals do not contain odd points as endpoints.
#
# So we can:
#
# For each query:
# answer = count_intervals_containing_C + count_intervals_containing_D - 2 * count_intervals_containing_both_C_and_D
#
# But since intervals are disjoint, count_intervals_containing_both_C_and_D is either 0 or 1.
#
# But we can ignore the last term because intervals are disjoint and points are distinct.
#
# So answer = count_intervals_containing_C + count_intervals_containing_D
#
# But we want segments where exactly one of C or D is inside interval.
#
# So answer = count_intervals_containing_C + count_intervals_containing_D - 2 * count_intervals_containing_both_C_and_D
#
# Since intervals are disjoint, count_intervals_containing_both_C_and_D = 0 always.
#
# So answer = count_intervals_containing_C + count_intervals_containing_D
#
# So for each query, answer = number of segments whose interval contains C + number of segments whose interval contains D.
#
# So problem reduces to:
# For each point x (odd), count how many intervals (segments) contain x.
#
# We can pre-process prefix sums over 1..4N.
#
# Implementation:
# - For each segment (A,B):
#   if A < B:
#     add +1 at A+1, -1 at B
#   else:
#     add +1 at A+1, -1 at B+2N
# - Build prefix sums over 1..4N
# - For each query (C,D):
#   if C < D:
#     C, D as is
#   else:
#     D += 2N
# - For each query:
#   answer = prefix_sum[C] + prefix_sum[D]
#
# Because intervals are open intervals (A,B), points at A or B are not inside.
#
# We must be careful with indexing.
#
# Let's implement this.

size = 4 * N + 10
diff = [0] * (size + 1)

def add_range(l, r):
    # add +1 to (l,r) open interval
    # so +1 at l+1, -1 at r
    # but l and r are 1-based
    diff[l + 1] += 1
    if r < len(diff):
        diff[r] -= 1

for A, B in segments:
    if A < B:
        add_range(A, B)
        add_range(A + 2 * N, B + 2 * N)
    else:
        add_range(A, B + 2 * N)

# prefix sum
for i in range(1, size):
    diff[i] += diff[i - 1]

# For queries, unwrap points if needed
for C, D in queries:
    if C < D:
        c = C
        d = D
    else:
        c = C
        d = D + 2 * N
    # answer = number of intervals containing c + number of intervals containing d
    # diff array is 0-based, points are 1-based
    ans = diff[c] + diff[d]
    print(ans)