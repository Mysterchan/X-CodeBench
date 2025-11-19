import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
grid = [input().strip() for _ in range(N)]

# Precompute a grid "white_square" where white_square[r][c] = 1 if
# the 2x2 block with top-left corner at (r,c) is all white ('.'), else 0.
# r, c range from 0 to N-2 for these blocks.
white_square = [[0]*(N-1) for _ in range(N-1)]
for r in range(N-1):
    for c in range(N-1):
        if (grid[r][c] == '.' and grid[r][c+1] == '.' and
            grid[r+1][c] == '.' and grid[r+1][c+1] == '.'):
            white_square[r][c] = 1

# Build 2D prefix sums for white_square
prefix = [[0]*(N) for _ in range(N)]
for r in range(N-1):
    row_sum = 0
    for c in range(N-1):
        row_sum += white_square[r][c]
        prefix[r+1][c+1] = prefix[r][c+1] + row_sum

# For each query:
# After painting outside the rectangle black, the only white cells are inside [U_i,D_i]x[L_i,R_i].
# The 2x2 white blocks that remain must be fully inside this rectangle.
# The top-left corner (r,c) of such a 2x2 block must satisfy:
# U_i <= r+1 <= D_i-1+1 => r in [U_i-1, D_i-2]
# L_i <= c+1 <= R_i-1+1 => c in [L_i-1, R_i-2]
# Because the block covers rows r and r+1, columns c and c+1,
# so r must be at least U_i-1 and at most D_i-2 (0-based),
# similarly for c.

# We just sum white_square[r][c] over r in [U_i-1, D_i-2], c in [L_i-1, R_i-2].

for _ in range(Q):
    U, D, L, R = map(int, input().split())
    # Convert to zero-based indices for prefix sums
    r1 = U - 1
    r2 = D - 2
    c1 = L - 1
    c2 = R - 2
    if r2 < r1 or c2 < c1:
        # No 2x2 blocks fit inside the rectangle
        print(0)
        continue
    res = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
    print(res)