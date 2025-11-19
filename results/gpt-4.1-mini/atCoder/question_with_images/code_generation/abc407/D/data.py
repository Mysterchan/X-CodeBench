import sys
sys.setrecursionlimit(10**7)

H, W = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

N = H * W

# Flatten the grid for easier indexing
vals = [A[i // W][i % W] for i in range(N)]

# Precompute adjacency for domino placements
# Each domino covers two adjacent cells: horizontal or vertical
adj = []
for i in range(H):
    for j in range(W):
        idx = i * W + j
        # horizontal domino
        if j + 1 < W:
            adj.append((idx, idx + 1))
        # vertical domino
        if i + 1 < H:
            adj.append((idx, idx + W))

# We'll use bitmask dp:
# dp[mask] = maximum XOR of uncovered cells when cells in mask are covered
# mask is a bitmask of length N, where 1 means cell is covered by domino
# We want to find max XOR of uncovered cells = XOR of cells not in mask

# Since N <= 20, dp size = 2^N = 1,048,576 which is feasible

dp = [-1] * (1 << N)
dp[0] = 0  # no cells covered, XOR of uncovered = XOR of all cells

# Precompute XOR of all cells for dp[0]
total_xor = 0
for v in vals:
    total_xor ^= v
dp[0] = total_xor

# We'll iterate over masks in increasing order of bits set
# For each mask, try to place a domino on two adjacent uncovered cells
# and update dp[new_mask] accordingly

for mask in range(1 << N):
    if dp[mask] == -1:
        continue
    # Find first uncovered cell
    # Optimization: if no uncovered cells, no further moves
    # But we can just try all domino placements
    for (x, y) in adj:
        # if both cells are uncovered in current mask
        if (mask & (1 << x)) == 0 and (mask & (1 << y)) == 0:
            new_mask = mask | (1 << x) | (1 << y)
            # uncovered cells in new_mask = uncovered cells in mask minus x,y
            # So XOR of uncovered cells in new_mask = dp[mask] ^ vals[x] ^ vals[y]
            val = dp[mask] ^ vals[x] ^ vals[y]
            if val > dp[new_mask]:
                dp[new_mask] = val

print(max(dp))