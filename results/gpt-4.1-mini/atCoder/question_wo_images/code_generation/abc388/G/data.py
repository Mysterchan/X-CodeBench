import sys
import bisect

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# Precompute for each i, the smallest j > i such that A[j] >= 2 * A[i]
# Because a <= b/2  <=>  b >= 2*a
# We want to find for each i, the minimal j > i with A[j] >= 2*A[i]

next_pos = [N] * N  # default N means no such j

for i in range(N):
    val = 2 * A[i]
    # binary search for val in A[i+1:]
    j = bisect.bisect_left(A, val, i + 1, N)
    if j < N:
        next_pos[i] = j

# We want to answer queries: for subarray [L,R], find max K pairs (2K mochi)
# such that for each pair (a,b), a <= b/2, and all mochi used are distinct.

# The problem reduces to maximum matching in a bipartite graph where left side is mochi indices,
# right side is mochi indices, edges from i to j if j > i and A[j] >= 2*A[i].
# We want to find max matching in subarray [L,R].

# Since the array is sorted, and edges go from smaller index to larger index,
# and the condition is monotone, we can use a greedy approach to find max matching in [L,R].

# Approach:
# For each query, we want to find max number of pairs in [L,R].
# We can try to pair smallest mochi with the smallest possible mochi that satisfies the condition.

# To do this efficiently for many queries, we can precompute a "matching" array:
# We'll try to greedily match mochi from left to right:
# For each i, if next_pos[i] < N, we can match i with next_pos[i].
# But we must ensure that pairs do not overlap.

# We can build a "matching" array that stores the index of the mochi matched with i (or -1 if none).
# Then, we can build a prefix sum array of how many matches are formed up to index i.

# However, this greedy matching over the entire array may not be optimal for subranges.

# Instead, we can precompute an array "matchable" where matchable[i] = 1 if mochi i can be matched with next_pos[i], else 0.
# Then, we can build a segment tree or binary indexed tree to answer queries about maximum matching in [L,R].

# But maximum matching is not simply counting edges, because edges can overlap.

# Alternative approach:
# Since the array is sorted, and edges go from i to next_pos[i], and next_pos[i] is increasing,
# the maximum matching in [L,R] can be found by a two-pointer greedy approach:

# For each query:
# - Extract subarray A[L-1:R]
# - Use two pointers: left pointer i from L-1 to R-1, right pointer j starting from somewhere
# - For each i, find the minimal j > i in [L-1,R-1] with A[j] >= 2*A[i]
# - Greedily match pairs without overlap.

# But Q and N are large (2*10^5), so O(Q*(R-L)) is too slow.

# We need a data structure to answer queries efficiently.

# Key insight:
# The problem is similar to the classic "maximum number of pairs" problem where pairs satisfy a condition,
# and the array is sorted.

# We can precompute for each position i, the minimal j >= i such that A[j] >= 2*A[i].
# Then, for the entire array, we can build a "matching" by pairing i with next_pos[i] if possible,
# and then remove matched elements from the pool.

# Since the array is sorted, the maximum matching is the maximum number of pairs formed by matching
# the smallest elements with the smallest possible elements that satisfy the condition.

# We can precompute an array "dp" where dp[i] = maximum number of pairs in A[i:].
# We can compute dp from right to left:
# dp[i] = max(dp[i+1], 1 + dp[next_pos[i]+1]) if next_pos[i] < N else dp[i+1]

# Then, for each query [L,R], the answer is dp[L-1] - dp[R]

# Let's verify this logic:

# dp[i] = max number of pairs in A[i:]
# So dp[L-1] = max pairs in A[L-1:]
# dp[R] = max pairs in A[R:]
# So dp[L-1] - dp[R] = max pairs in A[L-1:R]

# This works because dp is non-increasing and counts pairs greedily.

# Implement this dp and answer queries accordingly.

dp = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    if next_pos[i] < N:
        dp[i] = max(dp[i + 1], 1 + dp[next_pos[i] + 1])
    else:
        dp[i] = dp[i + 1]

for _ in range(Q):
    L, R = map(int, input().split())
    # zero-based indices
    L -= 1
    R -= 1
    # max pairs in A[L:R] = dp[L] - dp[R+1]
    print(dp[L] - dp[R + 1])