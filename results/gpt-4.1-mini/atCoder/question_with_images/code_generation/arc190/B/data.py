import sys
input = sys.stdin.readline

MOD = 998244353

N, a, b = map(int, input().split())
Q = int(input())
ks = list(map(int, input().split()))

# Explanation and approach:
# The problem asks for the number of ways to partition the N x N grid into exactly one level k L-shape for each k=1..N,
# such that the cell (a,b) is contained in the level k_i L-shape.
#
# Each level k L-shape covers exactly 2k-1 cells.
# The entire grid has N^2 cells.
# The sum of sizes of all L-shapes is sum_{k=1}^N (2k-1) = N^2, so the partition covers the whole grid exactly.
#
# The problem defines 4 types of L-shapes for each level k, each defined by a corner cell and directions.
#
# We want to count the number of ways to assign the L-shapes for all levels 1..N so that:
# - They partition the grid (no overlaps, no gaps)
# - The cell (a,b) is in the level k_i L-shape.
#
# The sample and problem hint that the number of ways depends on the position of (a,b) relative to k.
#
# Key insight (from editorial and problem structure):
# For each level k, the L-shape can be placed in 4 orientations.
# The entire partition is uniquely determined by choosing, for each k, one of the 4 orientations.
# But the cell (a,b) must be contained in the level k L-shape.
#
# For a fixed k, the number of ways to place the level k L-shape so that it contains (a,b) is the number of orientations
# for which there exists a valid corner cell (i,j) such that the L-shape covers (a,b).
#
# For each orientation, the corner cell (i,j) must satisfy certain bounds.
# For the cell (a,b) to be in the L-shape of level k with corner (i,j), (i,j) must be in a certain range.
#
# The number of valid corner cells (i,j) for each orientation that cover (a,b) is either 0 or 1,
# because the L-shape is fixed size and shape.
#
# Actually, for each orientation, there is exactly one corner cell (i,j) that covers (a,b) if (a,b) is in the valid range.
#
# So for each k, the number of ways to place the level k L-shape containing (a,b) is the count of orientations
# for which (a,b) can be covered by a valid L-shape of level k.
#
# Since the partition is independent for each k (choosing orientation for each k),
# the total number of ways to partition the grid with (a,b) in level k_i L-shape is:
#   ways(k_i) = number_of_orientations_covering(a,b,k_i) * (4^(N-1))
#
# Explanation:
# - For the level k_i, we must choose an orientation that covers (a,b).
# - For all other levels (N-1 levels), we can choose any of the 4 orientations freely.
#
# So total ways = (number_of_orientations_covering(a,b,k_i)) * 4^(N-1) mod MOD
#
# If number_of_orientations_covering(a,b,k_i) = 0, output 0.
#
# We precompute 4^(N-1) mod MOD once.
#
# Now, how to check if (a,b) is covered by level k L-shape in each orientation?
#
# Orientation 1: corner (i,j), moves down or right, 1 ≤ i ≤ N-k+1, 1 ≤ j ≤ N-k+1
# The L-shape covers cells:
#   (i + x, j) for x in [0, k-1]
#   (i, j + y) for y in [0, k-1]
# So (a,b) in this L-shape means:
#   i ≤ a ≤ i + k - 1
#   j ≤ b ≤ j + k - 1
# And i,j in [1, N-k+1]
#
# For (a,b) to be covered, there must exist i,j satisfying above.
# So:
#   i ≤ a ≤ i + k - 1  =>  i in [a - (k-1), a]
#   j ≤ b ≤ j + k - 1  =>  j in [b - (k-1), b]
# Also i,j in [1, N-k+1]
#
# So intersection:
#   i in [max(1, a-(k-1)), min(a, N-k+1)]
#   j in [max(1, b-(k-1)), min(b, N-k+1)]
#
# If these intervals are non-empty, orientation 1 covers (a,b).
#
# Similarly for other orientations:
#
# Orientation 2: corner (i,j), moves down or left, 1 ≤ i ≤ N-k+1, k ≤ j ≤ N
# L-shape covers:
#   (i + x, j) for x in [0, k-1]
#   (i, j - y) for y in [0, k-1]
# Conditions for (a,b):
#   i ≤ a ≤ i + k - 1
#   j - (k - 1) ≤ b ≤ j
# i in [1, N-k+1], j in [k, N]
#
# So:
#   i in [a - (k-1), a] ∩ [1, N-k+1]
#   j in [b, b + (k-1)] ∩ [k, N]
# But note j - (k-1) ≤ b ≤ j => j ≥ b and j ≤ b + (k-1)
#
# Orientation 3: corner (i,j), moves up or right, k ≤ i ≤ N, 1 ≤ j ≤ N-k+1
# L-shape covers:
#   (i - x, j) for x in [0, k-1]
#   (i, j + y) for y in [0, k-1]
# Conditions:
#   i - (k - 1) ≤ a ≤ i
#   j ≤ b ≤ j + k - 1
# i in [k, N], j in [1, N-k+1]
#
# So:
#   i in [a, a + (k-1)] ∩ [k, N]
#   j in [max(1, b - (k-1)), min(b, N-k+1)]
#
# Orientation 4: corner (i,j), moves up or left, k ≤ i ≤ N, k ≤ j ≤ N
# L-shape covers:
#   (i - x, j) for x in [0, k-1]
#   (i, j - y) for y in [0, k-1]
# Conditions:
#   i - (k - 1) ≤ a ≤ i
#   j - (k - 1) ≤ b ≤ j
# i in [k, N], j in [k, N]
#
# So:
#   i in [a, a + (k-1)] ∩ [k, N]
#   j in [b, b + (k-1)] ∩ [k, N]
#
# For each orientation, if the intersection intervals for i and j are non-empty, orientation covers (a,b).
#
# Count how many orientations cover (a,b) for each k.
#
# Then output count * pow(4, N-1, MOD) % MOD for each query k_i.
#
# If count == 0, output 0.
#
# Since Q ≤ 200000 and N ≤ 10^7, this is efficient.

pow4 = pow(4, N-1, MOD)

def interval_nonempty(l1, r1, l2, r2):
    l = max(l1, l2)
    r = min(r1, r2)
    return l <= r

for k in ks:
    count = 0
    # Orientation 1
    i_l1, i_r1 = max(1, a - (k - 1)), min(a, N - k + 1)
    j_l1, j_r1 = max(1, b - (k - 1)), min(b, N - k + 1)
    if interval_nonempty(i_l1, i_r1, 1, N - k + 1) and interval_nonempty(j_l1, j_r1, 1, N - k + 1):
        count += 1

    # Orientation 2
    i_l2, i_r2 = max(1, a - (k - 1)), min(a, N - k + 1)
    j_l2, j_r2 = max(b, k), min(b + (k - 1), N)
    if interval_nonempty(i_l2, i_r2, 1, N - k + 1) and interval_nonempty(j_l2, j_r2, k, N):
        count += 1

    # Orientation 3
    i_l3, i_r3 = max(a, k), min(a + (k - 1), N)
    j_l3, j_r3 = max(1, b - (k - 1)), min(b, N - k + 1)
    if interval_nonempty(i_l3, i_r3, k, N) and interval_nonempty(j_l3, j_r3, 1, N - k + 1):
        count += 1

    # Orientation 4
    i_l4, i_r4 = max(a, k), min(a + (k - 1), N)
    j_l4, j_r4 = max(b, k), min(b + (k - 1), N)
    if interval_nonempty(i_l4, i_r4, k, N) and interval_nonempty(j_l4, j_r4, k, N):
        count += 1

    if count == 0:
        print(0)
    else:
        print(count * pow4 % MOD)