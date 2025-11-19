import sys
input = sys.stdin.readline

H, W = map(int, input().split())
rows = [int(input().strip(), 2) for _ in range(H)]

# The problem:
# We can flip any row (X operation) and any column (Y operation) any number of times.
# Goal: minimize sum of all bits after these flips.

# Key insight:
# Flipping a column is equivalent to flipping that bit in all rows.
# Flipping a row is flipping all bits in that row.
# We want to find a combination of column flips (bitmask) and row flips (per row)
# to minimize total number of 1s.

# Approach:
# - We try all possible column flip patterns (there are 2^W, W <= 18, so up to 262144).
# - For each column flip pattern, we compute the cost:
#   For each row:
#     - Apply column flips: row ^ col_flip_mask
#     - We can flip the row or not:
#       - cost if no flip: count of 1s in (row ^ col_flip_mask)
#       - cost if flip: count of 0s in (row ^ col_flip_mask) = W - count_ones
#     - Choose min of these two.
#   Sum over all rows.
# - Take minimum over all column flip patterns.

# Precompute popcount for all 2^W numbers for speed
popcount = [bin(i).count('1') for i in range(1 << W)]

ans = H * W  # max possible sum
for col_flip_mask in range(1 << W):
    total = 0
    for r in rows:
        flipped = r ^ col_flip_mask
        c = popcount[flipped]
        total += min(c, W - c)
        if total >= ans:
            # Early stop if already worse
            break
    if total < ans:
        ans = total

print(ans)