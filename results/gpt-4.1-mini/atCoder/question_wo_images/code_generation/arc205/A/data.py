import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
grid = [input().strip() for _ in range(N)]

# We want to find for each query the number of 2x2 white squares fully inside the subrectangle [U,D]x[L,R].
# After coloring outside the subrectangle black, only cells inside remain as original.
# The operation count = number of 2x2 white squares fully inside the subrectangle.

# Precompute a 2D array 'white_2x2' where white_2x2[r][c] = 1 if the 2x2 block with top-left corner (r,c) is all white.
# r and c range from 0 to N-2 (0-based indexing).
white_2x2 = [[0]*(N-1) for _ in range(N-1)]

for r in range(N-1):
    for c in range(N-1):
        if (grid[r][c] == '.' and grid[r][c+1] == '.' and
            grid[r+1][c] == '.' and grid[r+1][c+1] == '.'):
            white_2x2[r][c] = 1

# Build 2D prefix sums for white_2x2
# prefix[r+1][c+1] = sum of white_2x2[0..r][0..c]
prefix = [[0]*(N) for _ in range(N)]
for r in range(N-1):
    row_sum = 0
    for c in range(N-1):
        row_sum += white_2x2[r][c]
        prefix[r+1][c+1] = prefix[r][c+1] + row_sum

# For each query (U,D,L,R), 1-based indexing:
# The 2x2 blocks fully inside [U,D]x[L,R] have top-left corners in rows [U, D-1] and cols [L, R-1].
# Convert to 0-based indexing:
# rows: U-1 to D-2
# cols: L-1 to R-2
# If D-1 < U or R-1 < L, no 2x2 blocks inside.

for _q in range(Q):
    U, D, L, R = map(int, input().split())
    r1 = U - 1
    r2 = D - 2
    c1 = L - 1
    c2 = R - 2
    if r2 < r1 or c2 < c1:
        print(0)
        continue
    ans = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
    print(ans)