MOD = 998244353

import sys
input = sys.stdin.readline

N = int(input())
Y = list(map(int, input().split()))

# We have points (i, Y_i) for i=1..N, Y is a permutation of 1..N.

# We want sum of areas of bounding boxes for all subsets S with |S|>=2.
# Bounding box area = (max_x - min_x) * (max_y - min_y)
# Here x-coordinates are fixed: points are at x=1..N
# y-coordinates are permutation Y.

# Key insight:
# The sum over all subsets of (max_x - min_x) * (max_y - min_y)
# = sum over all subsets of (max_x - min_x) * sum over all subsets of (max_y - min_y)
# but subsets are the same, so we cannot separate directly.

# Instead, use linearity and combinatorial approach:
# sum of areas = sum over all subsets S with |S|>=2 of (max_x - min_x)*(max_y - min_y)

# We can write:
# sum_area = sum_{S} (max_x - min_x)*(max_y - min_y)
# = sum_{S} (max_x - min_x)*(max_y - min_y)
# = sum_{S} (max_x - min_x)*(max_y - min_y)

# We can rewrite sum over subsets as:
# sum_area = sum_{i<j} (x_j - x_i) * sum_{subsets S containing i,j} (max_y - min_y)
# Because for fixed i,j, the x-range is fixed (j - i),
# and the subsets containing i,j contribute to the sum of (max_y - min_y).

# Similarly, we can fix y-min and y-max and sum over subsets containing those points.

# The problem is symmetric in x and y, but x is fixed as 1..N,
# y is a permutation.

# Approach:
# sum_area = sum over all pairs (i,j), i<j of (j - i) * sum over subsets containing i,j of (max_y - min_y)

# But this is complicated.

# Instead, use the known formula for sum of (max - min) over all subsets:
# For a sequence A of length N,
# sum over all subsets S with |S|>=2 of (max(S) - min(S)) =
# sum_{i=1 to N} A[i] * (2^{i-1} - 2^{N - i}) if A sorted ascending.

# We can use this for x and y separately.

# But we want sum of (max_x - min_x)*(max_y - min_y) over all subsets S.

# The key is to use the formula:
# sum_{S} (max_x - min_x)*(max_y - min_y)
# = sum_{i<j} (x_j - x_i)*(y_j - y_i)*2^{j - i - 1}

# This formula comes from the fact that for each pair (i,j),
# the number of subsets where i and j are min and max in x is 2^{j - i - 1},
# and similarly for y.

# But since x is fixed as 1..N, and y is a permutation,
# we can use the formula:

# sum_area = sum_{i<j} (j - i) * |Y_j - Y_i| * 2^{j - i - 1}

# We can compute this efficiently.

# Precompute powers of 2 modulo MOD
pow2 = [1]*(N+1)
for i in range(1, N+1):
    pow2[i] = (pow2[i-1]*2) % MOD

ans = 0
for i in range(N):
    for j in range(i+1, N):
        dist_x = j - i
        dist_y = abs(Y[j] - Y[i])
        ways = pow2[j - i - 1]
        ans += dist_x * dist_y * ways
        ans %= MOD

print(ans % MOD)