import sys
input = sys.stdin.readline

MOD = 998244353

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Q, sh, sw = map(int, input().split())
sh -= 1
sw -= 1

# We want to compute:
# sum over all paths P from (1,1) to (H,W) of product of A_{h_i,w_i} on P
# Paths move only right or down, length M = H+W-1

# Number of paths = C(H+W-2, H-1)
# Each path corresponds to a sequence of moves: (H-1) downs and (W-1) rights in some order.

# The sum of products over all paths can be computed by DP:
# dp[h][w] = sum of products of all paths from (1,1) to (h,w)
# dp[0][0] = A[0][0]
# dp[h][w] = (dp[h-1][w] + dp[h][w-1]) * A[h][w]

# We want to support Q updates:
# Each update changes A at a single cell (h,w) to a_i
# After each update, print dp[H-1][W-1]

# Constraints:
# H,W up to 200000, but H*W <= 200000
# Q up to 200000

# So total cells <= 200000, so we can store dp in a 1D array of size H*W.

# We need to efficiently update dp after changing A[h][w].

# Observation:
# dp[h][w] depends on dp[h-1][w] and dp[h][w-1], and A[h][w].
# Changing A[h][w] affects dp[h][w] and all dp cells reachable from (h,w) by moving right/down.

# The grid is DAG with edges from (h,w) to (h+1,w) and (h,w+1).

# We can process dp in order of increasing h+w (diagonal order).

# To update dp after changing A[h][w], we can recompute dp for all cells (x,y) with x>=h and y>=w in diagonal order.

# Since total cells is 200000, and Q is 200000, worst case O(H*W*Q) is too large.

# But the problem guarantees that H*W <= 200000, so the grid is sparse in one dimension.

# We can store dp in a 1D array indexed by (h,w).

# We'll precompute dp once.

# For updates, we only need to recompute dp for cells on diagonals >= h+w.

# We'll store cells by diagonals: diagonal d = h+w

# For each diagonal d, we have cells (h,w) with h+w=d.

# After update at (h,w), we recompute dp for diagonals d' from d to H+W-2.

# For each diagonal, recompute dp for all cells on that diagonal.

# Since total cells is 200000, and Q is 200000, worst case might be large but should pass with efficient implementation.

# Implementation details:
# - Store A in 1D array indexed by (h,w)
# - Store dp similarly
# - Precompute list of cells per diagonal
# - For update at (h,w), recompute dp for diagonals d = h+w to max diagonal

# Directions for moves:
# L: w-1
# R: w+1
# U: h-1
# D: h+1

# We'll track Takahashi's position and update A accordingly.

# Precompute dp:
# dp[0][0] = A[0][0]
# dp[h][w] = (dp[h-1][w] + dp[h][w-1]) * A[h][w]

# For h=0, dp[0][w] = dp[0][w-1] * A[0][w]
# For w=0, dp[h][0] = dp[h-1][0] * A[h][0]

# We'll implement dp as a 1D array dp[h*W + w]

# Let's implement now.

# Precompute cells by diagonal
cells_by_diag = [[] for _ in range(H+W-1)]
for h in range(H):
    for w in range(W):
        cells_by_diag[h+w].append((h,w))

# Initialize dp
dp = [0]*(H*W)
def idx(h,w):
    return h*W + w

# Compute initial dp
for d in range(H+W-1):
    for (h,w) in cells_by_diag[d]:
        if h == 0 and w == 0:
            dp[idx(h,w)] = A[h][w] % MOD
        elif h == 0:
            dp[idx(h,w)] = dp[idx(h,w-1)] * A[h][w] % MOD
        elif w == 0:
            dp[idx(h,w)] = dp[idx(h-1,w)] * A[h][w] % MOD
        else:
            dp[idx(h,w)] = (dp[idx(h-1,w)] + dp[idx(h,w-1)]) * A[h][w] % MOD

# Process queries
pos_h, pos_w = sh, sw

for _ in range(Q):
    d_i, a_i = input().split()
    a_i = int(a_i)
    # Move Takahashi
    if d_i == 'L':
        pos_w -= 1
    elif d_i == 'R':
        pos_w += 1
    elif d_i == 'U':
        pos_h -= 1
    elif d_i == 'D':
        pos_h += 1
    # Update A
    A[pos_h][pos_w] = a_i

    # Recompute dp from diagonal d = pos_h + pos_w to end
    start_d = pos_h + pos_w
    for d in range(start_d, H+W-1):
        for (h,w) in cells_by_diag[d]:
            if h == 0 and w == 0:
                dp[idx(h,w)] = A[h][w] % MOD
            elif h == 0:
                dp[idx(h,w)] = dp[idx(h,w-1)] * A[h][w] % MOD
            elif w == 0:
                dp[idx(h,w)] = dp[idx(h-1,w)] * A[h][w] % MOD
            else:
                dp[idx(h,w)] = (dp[idx(h-1,w)] + dp[idx(h,w-1)]) * A[h][w] % MOD

    print(dp[idx(H-1,W-1)] % MOD)