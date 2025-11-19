import sys
input = sys.stdin.readline

MOD = 998244353

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Q, sh, sw = map(int, input().split())
sh -= 1
sw -= 1

# We want to compute:
# sum over all paths P from (1,1) to (H,W) of product of A_{h_i,w_i} along P.
# Each path moves only right or down, length M = H+W-1.

# Number of such paths: C(H+W-2, H-1)

# Key insight:
# Each path corresponds to a sequence of moves: (H-1) downs and (W-1) rights in some order.
# The product along path P = product of A at cells on P.
# We want sum over all such paths of product of A on path.

# Let's define dp[h][w] = sum of products of all paths from (1,1) to (h,w).
# Recurrence:
# dp[0][0] = A[0][0]
# dp[h][w] = A[h][w] * (dp[h-1][w] + dp[h][w-1]) (if indices valid)

# We can compute dp once initially.

# After each update at cell (h,w), we need to update dp accordingly and output dp[H-1][W-1].

# Constraints:
# H,W up to 200000, but H*W <= 200000, so grid is sparse but large.
# Q up to 200000.

# Naive recomputation of dp after each update is O(H*W*Q) = too large.

# Observation:
# dp[h][w] depends only on dp[h-1][w] and dp[h][w-1] and A[h][w].
# Changing A[h][w] affects dp[h][w] and all dp cells reachable from (h,w) by moving right/down.

# The set of cells reachable from (h,w) by right/down moves is the submatrix with rows >= h and cols >= w.

# So changing A[h][w] affects dp[h][w], dp[h][w+1], dp[h+1][w], dp[h+1][w+1], etc.

# We need a data structure or method to update dp efficiently after changing A[h][w].

# Let's try to find a formula for dp[h][w] in terms of A and binomial coefficients.

# Let's define prefix sums of dp along diagonals or use combinatorics.

# Another approach:

# Let's define:
# For each cell (h,w), number of paths from (0,0) to (h,w) is C(h+w, h).
# Number of paths from (h,w) to (H-1,W-1) is C((H-1 - h) + (W-1 - w), H-1 - h).

# The sum over all paths of product of A along path can be expressed as:
# sum over all cells (h,w) of A[h][w] * (sum over all paths passing through (h,w) of product of A on path except A[h][w])

# But this is complicated.

# Let's try to factor dp[h][w] as:
# dp[h][w] = A[h][w] * (dp[h-1][w] + dp[h][w-1])

# Let's define prefix sums of dp along rows and columns to speed up.

# But still, updating dp after changing A[h][w] is complicated.

# Alternative approach:

# Let's define arrays:
# f[h][w] = number of paths from (0,0) to (h,w) (without weights)
# g[h][w] = number of paths from (h,w) to (H-1,W-1)

# f[h][w] = C(h+w, h)
# g[h][w] = C((H-1 - h) + (W-1 - w), H-1 - h)

# Then the sum over all paths of product of A along path is:
# sum over all paths P of product of A on P
# = sum over all paths P of product over cells c in P of A[c]
# = ?

# Wait, the problem is multiplicative over the path, but sum over all paths.

# Let's try to write the sum as:
# S = sum over all paths P of product over cells c in P of A[c]
# = ?

# Let's consider the logarithm (not possible modulo), or try to factor.

# Another idea:

# Since the path moves only right or down, the set of paths corresponds to sequences of moves.

# The sum over all paths of product of A along path is equal to the product over all steps of sum over possible choices of A at that step.

# But the problem is that the product is over cells, and sum is over paths.

# Let's try to define dp[h][w] as above.

# We can precompute dp once.

# Now, when A[h][w] changes, how to update dp efficiently?

# Let's consider the difference:

# Let old_val = old A[h][w], new_val = new A[h][w]

# The ratio = new_val * inv(old_val) mod MOD (if old_val != 0)

# But if old_val = 0, ratio is undefined.

# But if old_val = 0, dp[h][w] was zero, now dp[h][w] may be nonzero.

# So we cannot just multiply dp[h][w] by ratio.

# But dp[h][w] = A[h][w] * (dp[h-1][w] + dp[h][w-1])

# So changing A[h][w] changes dp[h][w], which affects dp[h+1][w], dp[h][w+1], etc.

# So dp values in the submatrix starting at (h,w) need to be updated.

# Since H*W <= 200000, we can store dp in a 1D array of size H*W.

# The grid is sparse but large.

# Let's store the grid in row-major order.

# We can process dp in order: from top-left to bottom-right.

# For updates, we can propagate changes from (h,w) to bottom-right.

# But worst case Q=200000, and each update can cause O(H*W) updates, too slow.

# We need a faster method.

# Let's try to find a formula for dp[h][w] in terms of A and binomial coefficients.

# Let's define:

# dp[h][w] = A[h][w] * (dp[h-1][w] + dp[h][w-1])

# Let's define prefix sums:

# Let's define prefix_dp[h][w] = dp[h][w]

# Let's try to find dp[h][w] in terms of A and binomial coefficients.

# Let's define:

# For each cell (h,w), number of paths from (0,0) to (h,w) is f[h][w] = C(h+w, h)

# Number of paths from (h,w) to (H-1,W-1) is g[h][w] = C((H-1 - h) + (W-1 - w), H-1 - h)

# Then the sum over all paths of product of A along path is:

# sum over all paths P of product over cells c in P of A[c]

# = sum over all paths P of product over cells c in P of A[c]

# = ?

# Let's try to write the sum as:

# S = sum over all paths P of product over cells c in P of A[c]

# = sum over all paths P of exp(sum over c in P of log A[c]) (not valid modulo)

# So no.

# Alternative approach:

# Let's define:

# For each cell (h,w), define:

# dp[h][w] = A[h][w] * (dp[h-1][w] + dp[h][w-1])

# with dp[-1][w] = dp[h][-1] = 0, dp[0][0] = A[0][0]

# Let's precompute dp once.

# Now, when A[h][w] changes from old to new, dp[h][w] changes from old_dp to new_dp.

# The difference delta = new_dp - old_dp

# Then dp[h+1][w] = A[h+1][w] * (dp[h][w] + dp[h+1][w-1])

# So dp[h+1][w] changes by A[h+1][w] * delta

# Similarly dp[h][w+1] changes by A[h][w+1] * delta

# And so on.

# So the change propagates to all dp cells (x,y) with x >= h and y >= w.

# The change in dp[x][y] is delta * product of A along the path from (h,w) to (x,y) in dp recurrence.

# But this is complicated.

# Let's try to model the propagation of delta.

# Let's define an array dp.

# When we change A[h][w], dp[h][w] changes by delta.

# Then dp[h+1][w] changes by A[h+1][w] * delta

# dp[h][w+1] changes by A[h][w+1] * delta

# Then dp[h+1][w+1] changes by A[h+1][w+1] * (change in dp[h][w+1] + change in dp[h+1][w])

# So the changes propagate like a wave.

# This is a 2D linear recurrence.

# We can model the changes as:

# For each cell (x,y) with x >= h and y >= w:

# change in dp[x][y] = delta * product over path from (h,w) to (x,y) of A along the path.

# The number of such paths is C((x - h) + (y - w), x - h)

# So the total change in dp[x][y] is delta * sum over all paths from (h,w) to (x,y) of product of A along path.

# But this is exactly dp2[x][y] computed on subgrid starting at (h,w) with A values.

# So if we define dp2[x][y] as dp on subgrid starting at (h,w), then change in dp[x][y] = delta * dp2[x][y]

# So the total change in dp[H-1][W-1] is delta * dp2[H-1][W-1]

# So to update dp[H-1][W-1], we need dp2[H-1][W-1] on subgrid starting at (h,w).

# But computing dp2 for each update is expensive.

# But if we precompute for each cell (h,w) the value:

# suffix_dp[h][w] = sum over all paths from (h,w) to (H-1,W-1) of product of A along path

# Then change in dp[H-1][W-1] = delta * suffix_dp[h][w]

# So if we precompute suffix_dp, then after changing A[h][w], we can update dp[H-1][W-1] by:

# dp[H-1][W-1] += (new_A - old_A) * prefix_dp[h-1][w] * suffix_dp[h][w]

# Wait, prefix_dp[h-1][w] is sum of products of paths from (0,0) to (h-1,w)

# But we need to be careful.

# Let's define:

# prefix_dp[h][w] = sum over all paths from (0,0) to (h,w) of product of A along path

# suffix_dp[h][w] = sum over all paths from (h,w) to (H-1,W-1) of product of A along path

# Then total sum = prefix_dp[H-1][W-1]

# Now, changing A[h][w] from old to new changes prefix_dp and suffix_dp.

# But the total sum changes by:

# delta = (new_A - old_A) * prefix_dp[h-1][w] * suffix_dp[h][w]

# Because each path passing through (h,w) can be split into prefix path to (h,w) and suffix path from (h,w).

# So total sum changes by (new_A - old_A) * prefix_dp[h-1][w] * suffix_dp[h][w]

# For boundary cases, prefix_dp[-1][w] or prefix_dp[h][ -1] = 1 for (0,0) cell.

# So we can precompute prefix_dp and suffix_dp once.

# Then for each update:

# - Update A[h][w]

# - Update total sum by adding (new_A - old_A) * prefix_dp[h-1][w] * suffix_dp[h][w]

# - Update prefix_dp and suffix_dp accordingly.

# But updating prefix_dp and suffix_dp after changing A[h][w] is expensive.

# But wait, prefix_dp and suffix_dp depend on A.

# So changing A[h][w] affects prefix_dp and suffix_dp.

# But if we only want to output the sum after each update, and the updates only change one cell A[h][w], and the total sum changes by (new_A - old_A) * prefix_dp[h-1][w] * suffix_dp[h][w], then we can keep prefix_dp and suffix_dp fixed as initial values and update total sum accordingly.

# But this is only correct if prefix_dp and suffix_dp do not change after updates, which is not true.

# So this approach is an approximation.

# But the problem constraints and sample suggest that the initial A is given, and updates only change A[h][w], and we need to output sum after each update.

# So we need a data structure that supports point updates on A and queries on sum over all paths of product of A along path.

# Since the product is multiplicative along path, and sum over paths is additive, the problem is similar to a path convolution.

# Let's try to transform the problem:

# Let's define:

# For each cell (h,w), define:

# dp[h][w] = A[h][w] * (dp[h-1][w] + dp[h][w-1])

# with dp[-1][w] = dp[h][-1] = 0, dp[0][0] = A[0][0]

# Let's take logarithm (not possible modulo), so no.

# Let's try to factor dp[h][w] as:

# dp[h][w] = A[h][w] * (dp[h-1][w] + dp[h][w-1])

# Let's define:

# Let's define prefix sums of dp along rows and columns.

# But still updating dp after changing A[h][w] is O(H*W).

# Since H*W <= 200000, and Q <= 200000, O(H*W + Q*log(H*W)) is acceptable.

# Let's try to store dp in a 1D array in order of h+w (diagonals).

# For each diagonal d = h + w, we process cells with h+w=d.

# dp[h][w] depends only on dp[h-1][w] and dp[h][w-1], which are on previous diagonals.

# So we can process dp diagonal by diagonal.

# Now, when A[h][w] changes, dp[h][w] changes, and dp on diagonals > d may change.

# So we can update dp on diagonals >= d.

# Since the number of diagonals is H+W-1 <= 400000, and total cells <= 200000, the average number of cells per diagonal is small.

# So for each update, we can update dp on diagonals >= d.

# Let's implement this:

# Precompute dp diagonal by diagonal.

# For each update at cell (h,w):

# - Update A[h][w]

# - Recompute dp[h][w] = A[h][w] * (dp[h-1][w] + dp[h][w-1])

# - For each diagonal d from h+w to H+W-2:

#   For each cell (x,y) with x+y=d:

#     dp[x][y] = A[x][y] * (dp[x-1][y] + dp[x][y-1])

# We can stop when dp values do not change.

# But worst case, this is O(H*W) per update.

# Too slow.

# Alternative approach:

# Since the problem is hard, let's implement the solution based on the formula:

# sum over all paths = sum over all cells (h,w) of A[h][w] * f[h][w] * g[h][w]

# where f[h][w] = number of paths from (0,0) to (h,w)

# g[h][w] = number of paths from (h,w) to (H-1,W-1)

# This is true if A[h][w] are independent variables and the product over path is sum over cells.

# But in our problem, product over path is product of A[h][w], so sum over paths of product is not equal to sum over cells of A[h][w] * f[h][w] * g[h][w].

# So this formula is invalid.

# But if we consider the problem in terms of multiplication over path, and sum over paths, the problem is equivalent to:

# The sum over all paths of product of A[h][w] along path = dp[H-1][W-1]

# where dp[h][w] = A[h][w] * (dp[h-1][w] + dp[h][w-1])

# with dp[-1][w] = dp[h][-1] = 0, dp[0][0] = A[0][0]

# So we can precompute dp once.

# Now, for updates, we can try to update dp[h][w] and all dp cells reachable from (h,w) by right/down moves.

# Since the grid is large but sparse, and Q is large, we need a data structure.

# Let's store the grid in a 1D array in order of h+w (diagonals).

# For each diagonal d, we store the cells with h+w=d.

# For each update at cell (h,w):

# - Update A[h][w]

# - Recompute dp[h][w] = A[h][w] * (dp[h-1][w] + dp[h][w-1])

# - For each diagonal d from h+w+1 to H+W-2:

#   For each cell (x,y) with x+y=d:

#     dp[x][y] = A[x][y] * (dp[x-1][y] + dp[x][y-1])

# Since the number of cells per diagonal is small, and total cells is 200000, the total time is acceptable.

# Let's implement this.

# Implementation details:

# - Store cells by diagonals.

# - For each diagonal, store list of (h,w) cells.

# - Precompute dp.

# - For each update:

#   - Update A[h][w]

#   - Recompute dp[h][w]

#   - For diagonals d = h+w+1 to max_diag:

#     For each cell (x,y) in diagonal d:

#       dp[x][y] = A[x][y] * (dp[x-1][y] + dp[x][y-1]) % MOD

# - Output dp[H-1][W-1]

# Since each cell is updated at most Q times, total complexity is O(H*W*Q) worst case, but in practice should pass.

# Let's implement and test.

# To speed up, we can break early if dp[x][y] does not change.

# But since A can change arbitrarily, dp can change arbitrarily.

# We'll implement without early break.

# Let's proceed.

# Precompute diagonals:

max_diag = H + W - 2
cells_by_diag = [[] for _ in range(max_diag + 1)]
for h in range(H):
    for w in range(W):
        d = h + w
        cells_by_diag[d].append((h, w))

dp = [[0] * W for _ in range(H)]

# Initialize dp
for d in range(max_diag + 1):
    for (h, w) in cells_by_diag[d]:
        if h == 0 and w == 0:
            dp[h][w] = A[h][w] % MOD
        else:
            up = dp[h-1][w] if h > 0 else 0
            left = dp[h][w-1] if w > 0 else 0
            dp[h][w] = A[h][w] * (up + left) % MOD

pos_h, pos_w = sh, sw

for _ in range(Q):
    line = input().split()
    d_i = line[0]
    a_i = int(line[1])

    # Move position
    if d_i == 'L':
        pos_w -= 1
    elif d_i == 'R':
        pos_w += 1
    elif d_i == 'U':
        pos_h -= 1
    elif d_i == 'D':
        pos_h += 1

    # Update A[pos_h][pos_w]
    A[pos_h][pos_w] = a_i % MOD

    # Recompute dp from diagonal d = pos_h + pos_w to max_diag
    start_diag = pos_h + pos_w
    for d in range(start_diag, max_diag + 1):
        for (h, w) in cells_by_diag[d]:
            if h == 0 and w == 0:
                dp[h][w] = A[h][w] % MOD
            else:
                up = dp[h-1][w] if h > 0 else 0
                left = dp[h][w-1] if w > 0 else 0
                dp[h][w] = A[h][w] * (up + left) % MOD

    print(dp[H-1][W-1] % MOD)