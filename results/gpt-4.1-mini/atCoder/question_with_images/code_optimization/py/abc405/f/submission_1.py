import sys
input = sys.stdin.readline

n, m = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(m)]
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

# We want to count how many of the M segments (each connecting two even points)
# share a point with the query segment (connecting two odd points).

# Key observations:
# - Segments do not share points.
# - Points are numbered 1 to 2N on a circle.
# - Each segment connects two even points.
# - Queries connect two odd points.
# - We want to count how many segments share a point with the query segment.

# The original code uses a complex SortedList and binary searches.
# We can optimize by using coordinate compression and Fenwick trees (BITs).

# Approach:
# For each segment (A_i, B_i), A_i < B_i, both even.
# For each query (C_j, D_j), C_j < D_j, both odd.

# The problem reduces to counting how many segments intersect the arc between C_j and D_j.
# Since points are on a circle, we can consider the circle linearized from 1 to 2N.

# The segment connecting C_j and D_j covers the arc from C_j to D_j clockwise.
# A segment (A_i, B_i) shares a point with (C_j, D_j) if either A_i or B_i lies on the arc (C_j, D_j).

# Since no two segments share points, no segment shares both endpoints with the query segment.

# So, for each query, count how many segments have at least one endpoint in (C_j, D_j).

# We can pre-process:
# - For all segment endpoints (even points), mark them in a Fenwick tree.
# - For each query, count how many segment endpoints lie in (C_j, D_j).
# - Since each segment has two endpoints, and no two segments share points,
#   the count of segments sharing a point with the query segment is the number of unique segments
#   that have at least one endpoint in (C_j, D_j).

# But counting unique segments from endpoints is tricky because a segment has two endpoints.

# Alternative approach:
# Since segments do not share points, and endpoints are even numbers,
# we can map each even point to the segment it belongs to.

# For each query:
# - Count how many segments have at least one endpoint in (C_j, D_j).
# - Since no two segments share points, counting endpoints in (C_j, D_j) gives twice the number of segments
#   that have both endpoints in (C_j, D_j), and once for segments with one endpoint in the arc.

# But segments are between two even points, so if both endpoints are in (C_j, D_j), the segment is counted twice.
# If only one endpoint is in (C_j, D_j), counted once.

# So, to get the number of segments sharing a point with the query segment, we can:
# - Count how many endpoints lie in (C_j, D_j) => E
# - Count how many segments have both endpoints in (C_j, D_j) => S
# Then answer = E - S (because segments with both endpoints in the arc are counted twice in E).

# Implementation plan:
# 1. For each segment, store (A_i, B_i).
# 2. Build a Fenwick tree over points 1..2N to count endpoints.
# 3. For each segment, mark both endpoints in Fenwick tree.
# 4. For each query (C_j, D_j), compute:
#    E = count of endpoints in (C_j, D_j) = prefix_sum(D_j - 1) - prefix_sum(C_j)
# 5. To get S (segments with both endpoints in (C_j, D_j)), we can:
#    - For each segment, check if both endpoints in (C_j, D_j).
#    - But doing this for each query is O(MQ), too slow.

# Optimization for S:
# - Preprocess segments by their endpoints.
# - For each segment, store (A_i, B_i).
# - For queries, we want to quickly count how many segments have both endpoints in (C_j, D_j).
# - We can sort segments by their start and end points.
# - For each query, count how many segments have A_i > C_j and B_i < D_j.

# So:
# - Sort segments by A_i.
# - For queries, we want to count segments with A_i in (C_j, D_j) and B_i in (C_j, D_j).
# - For each query, count how many segments have A_i > C_j and B_i < D_j.

# We can process queries offline:
# - Sort queries by C_j ascending.
# - Sort segments by A_i ascending.
# - Use a Fenwick tree over B_i to count how many segments have B_i < D_j for segments with A_i > C_j.

# But since we want A_i > C_j, we can process queries in descending order of C_j,
# and add segments with A_i > C_j to Fenwick tree.

# Let's implement this approach.

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+2)
    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l-1)

# Coordinate compression for endpoints (1..2N)
# Points are from 1 to 2N, so no compression needed.

# Build Fenwick tree for endpoints to count E for queries
fen_endpoints = Fenwick(2*n)
for a,b in intervals:
    fen_endpoints.add(a,1)
    fen_endpoints.add(b,1)

# For counting S (segments with both endpoints in (C_j, D_j)):
# Sort segments by A_i ascending
intervals.sort()
# Sort queries by C_j descending, keep original index
queries_with_idx = sorted([(c,d,i) for i,(c,d) in enumerate(queries)], key=lambda x: x[0], reverse=True)

fen_b = Fenwick(2*n)
res_S = [0]*q
idx = m-1
for c,d,i in queries_with_idx:
    # Add segments with A_i > c
    while idx >= 0 and intervals[idx][0] > c:
        fen_b.add(intervals[idx][1],1)
        idx -= 1
    # Count how many segments have B_i < d
    # segments with A_i > c and B_i < d
    res_S[i] = fen_b.sum(d-1)

# Now compute answers
# For each query:
# E = number of endpoints in (C_j, D_j) = fen_endpoints.sum(D_j-1) - fen_endpoints.sum(C_j)
# Answer = E - S

output = []
for i,(c,d) in enumerate(queries):
    E = fen_endpoints.sum(d-1) - fen_endpoints.sum(c)
    ans = E - res_S[i]
    output.append(str(ans))

print('\n'.join(output))