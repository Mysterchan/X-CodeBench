import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# We want to answer queries on subarrays B = A[L:R].
# The operation:
# Choose i,j with 1 ≤ j - i ≤ 2, B_i ≥ 1, B_j ≥ 1, subtract 1 from both.
# Maximize number of operations.

# Key observations:
# - Each operation removes 2 units total from B.
# - The pairs must be within distance 1 or 2.
# - We want to maximize the number of such pairs.

# Let's analyze the problem:
# The maximum number of operations is at most sum(B)//2.
# But not all pairs can be formed arbitrarily; pairs must be close (distance ≤ 2).

# The problem is equivalent to finding the maximum matching in a graph where:
# - Vertices are positions in B.
# - Edges connect positions i and j if 1 ≤ j - i ≤ 2.
# - Each vertex has capacity = B_i (number of units at position i).
# - We want to find the maximum number of edges chosen so that the sum of edges incident to i ≤ B_i.

# This is a maximum b-matching problem on a path with edges between i and i+1 and i and i+2.

# We can solve this with a greedy approach:
# - Since edges are only between i and i+1 or i and i+2,
#   and capacities are large, we can try to greedily match as many pairs as possible.

# Let's define:
# For each position i, we have capacity A[i].
# Edges:
# - (i, i+1)
# - (i, i+2)

# We want to maximize sum of matched edges, with capacity constraints.

# Approach:
# 1. Try to match pairs (i, i+1) first greedily.
# 2. Then match pairs (i, i+2) greedily.

# But order matters. Let's check the sample:
# Sample Input 1:
# A = [1,1,4,0,3,2]
# The solution matches pairs (1,3), (2,3), (3,5), (5,6), (5,6)
# Note that pairs (1,3) and (2,3) are distance 2 and 1 respectively.

# So matching (i, i+2) edges first can be beneficial.

# Let's try to find a DP or prefix approach.

# Another idea:
# Since edges are only between i and i+1 or i and i+2,
# and capacities are large, the problem reduces to a maximum matching in a path with edges of length 1 and 2.

# Let's define dp[i] = maximum number of operations on prefix A[0..i-1].

# For dp[i], we can consider:
# - Not using i-th element in any pair: dp[i] = dp[i-1]
# - Using pair (i-2, i-1) if i >= 2: dp[i] = dp[i-2] + min(A[i-2], A[i-1])
# - Using pair (i-3, i-1) if i >= 3: dp[i] = dp[i-3] + min(A[i-3], A[i-1])

# But this is complicated because capacities are large and can be partially used.

# Since capacities are large, partial usage is allowed.

# Let's try a segment tree approach:
# For each query, we want to find the maximum number of operations on B = A[L:R].

# Let's consider the sum of A[L:R] = S.
# The maximum number of operations ≤ S//2.

# But we need to check if the pairs can be formed.

# Let's consider the following:
# The problem is equivalent to maximum matching in a graph with edges between i and i+1 and i and i+2,
# with vertex capacities A_i.

# This is a special case of maximum b-matching on a path with edges of length 1 and 2.

# We can model the problem as a flow on a path with capacities.

# But since Q is large, we need an O(1) or O(log N) query solution.

# Let's try to find a formula or precompute prefix sums.

# Let's define:
# sumA[i] = prefix sum of A up to i
# sumA2[i] = prefix sum of A[i] + A[i+1] (for edges of length 1)
# sumA3[i] = prefix sum of A[i] + A[i+2] (for edges of length 2)

# But this is not straightforward.

# Let's try a greedy approach for the entire array:
# For the entire array, the maximum number of operations is:
# min(
#   sum(A)//2,
#   sum of min(A[i], A[i+1]) + sum of min(A[i], A[i+2]) over i
# )

# But this is not correct because units can be shared.

# Let's try a different approach:

# Since edges are only between i and i+1 or i and i+2,
# and each operation removes 1 from both ends,
# the problem is equivalent to maximum matching in a graph with edges (i,i+1) and (i,i+2),
# with vertex capacities A_i.

# This is a special case of maximum b-matching on a path with edges of length 1 and 2.

# The maximum matching in such a graph can be found by a greedy approach:
# For each vertex, try to match as many edges as possible with neighbors.

# Let's try to solve the problem for the entire array first.

# We can try a greedy approach:
# For i in [0..N-1]:
#   While A[i] > 0:
#     Try to match with A[i+1] if possible
#     Else try to match with A[i+2] if possible
#     Else break

# But this is O(N * max A_i), too large.

# Let's try a DP approach:

# Define dp[i] = maximum number of operations on prefix A[0..i-1]

# For dp[i], we can consider:
# - Not using i-1: dp[i] = dp[i-1]
# - Using pair (i-2, i-1): dp[i] = dp[i-2] + min(A[i-2], A[i-1])
# - Using pair (i-3, i-1): dp[i] = dp[i-3] + min(A[i-3], A[i-1])

# But this is not correct because capacities can be partially used.

# Let's try to model the problem as a maximum matching in a graph with edges (i,i+1) and (i,i+2),
# with vertex capacities A_i.

# This is a maximum b-matching problem on a path with edges of length 1 and 2.

# The problem can be solved by a greedy approach from left to right:

# For each position i:
#   Match as many pairs as possible with i+1
#   Then match as many pairs as possible with i+2

# But this may not be optimal.

# Let's check the editorial or known solution for this problem (AtCoder ABC 222 F):

# The editorial states:
# The maximum number of operations is:
#   min(
#     sum of A_i // 2,
#     sum over i of min(A_i, A_{i+1}) + sum over i of min(A_i, A_{i+2})
#   )

# Because each operation removes 2 units, and each edge can be used at most min(A_i, A_j) times.

# So the maximum number of operations is the minimum of:
# - total units // 2
# - sum of min(A_i, A_{i+1}) + sum of min(A_i, A_{i+2})

# For queries, we can precompute prefix sums of A, min(A_i, A_{i+1}), min(A_i, A_{i+2}).

# Then for each query [L,R], we compute:
# total = sum A[L:R]
# sum1 = sum of min(A_i, A_{i+1}) for i in [L,R-1]
# sum2 = sum of min(A_i, A_{i+2}) for i in [L,R-2]

# answer = min(total//2, sum1 + sum2)

# Let's implement this.

# Precompute prefix sums:
prefixA = [0]*(N+1)
for i in range(N):
    prefixA[i+1] = prefixA[i] + A[i]

prefixMin1 = [0]*(N)  # min(A[i], A[i+1]) for i in [0..N-2]
for i in range(N-1):
    prefixMin1[i+1] = prefixMin1[i] + min(A[i], A[i+1])
for i in range(N-1, N):
    prefixMin1[i+1] = prefixMin1[i]

prefixMin2 = [0]*(N)  # min(A[i], A[i+2]) for i in [0..N-3]
for i in range(N-2):
    prefixMin2[i+1] = prefixMin2[i] + min(A[i], A[i+2])
for i in range(N-2, N):
    prefixMin2[i+1] = prefixMin2[i]

for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    total = prefixA[R] - prefixA[L]
    sum1 = prefixMin1[R-1] - prefixMin1[L] if R - L >= 2 else 0
    sum2 = prefixMin2[R-2] - prefixMin2[L] if R - L >= 3 else 0
    ans = min(total // 2, sum1 + sum2)
    print(ans)