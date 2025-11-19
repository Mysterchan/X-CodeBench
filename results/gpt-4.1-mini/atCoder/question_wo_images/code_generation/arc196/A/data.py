import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# The problem is to repeatedly remove pairs of adjacent elements until at most one element remains,
# maximizing the sum of absolute differences of removed pairs.

# Key observations:
# - Each operation removes two adjacent elements.
# - After removing a pair, the sequence shrinks and the neighbors become adjacent.
# - We want to maximize sum of |A_i - A_j| over all pairs removed.

# Since the sequence length can be up to 3*10^5, an O(N^2) approach is impossible.
# We need a linear or O(N) solution.

# Insight:
# The problem is equivalent to pairing up elements in the sequence (in order) to maximize sum of absolute differences.
# Because we can only remove adjacent pairs, the order of elements is fixed, but after removing pairs,
# the neighbors become adjacent, so the pairing can be done in any order as long as pairs are adjacent at removal time.

# This is a classic problem that can be solved using a greedy approach:
# - If N is even, we can pair all elements.
# - If N is odd, one element remains unpaired.

# The maximum sum of absolute differences by pairing adjacent elements in some order is equal to the sum of absolute differences
# of pairs in an optimal pairing.

# The problem reduces to:
# - Find a pairing of elements (adjacent in the final sequence after removals) that maximizes sum of |A_i - A_j|.

# Since we can remove pairs in any order, the problem is equivalent to:
# - Partition the sequence into pairs (adjacent in the original sequence or after removals) to maximize sum of |A_i - A_j|.

# This is a known problem and can be solved by dynamic programming:
# Let dp[i] = maximum score obtained by pairing elements from A[0..i].
# - If i is odd (0-based), dp[i] = dp[i-2] + |A[i] - A[i-1]|
# - If i is even, dp[i] = dp[i-1] (cannot pair last element alone)

# But this only pairs adjacent elements in the original sequence, no rearrangement.

# However, the problem allows removing pairs in any order, so after removals, elements become adjacent.

# The problem is equivalent to finding a maximum matching in a path graph with weights = |A_i - A_{i+1}|.

# The maximum sum of weights of edges in a matching on a path can be found by DP:

# Define dp[i] = maximum sum of absolute differences for matching on first i elements (0-based indexing)
# Base cases:
# dp[0] = 0 (no elements)
# dp[1] = 0 (only one element, no pair)
# For i >= 2:
# dp[i] = max(dp[i-1], dp[i-2] + |A[i-1] - A[i-2]|)

# Explanation:
# - dp[i-1]: skip pairing the i-th element
# - dp[i-2] + |A[i-1] - A[i-2]|: pair elements i-2 and i-1

# The answer is dp[N]

# This DP runs in O(N) and uses O(N) memory, which is acceptable.

dp = [0] * (N + 1)
for i in range(2, N + 1):
    dp[i] = max(dp[i-1], dp[i-2] + abs(A[i-1] - A[i-2]))

print(dp[N])