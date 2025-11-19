import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
grid = [input().strip() for _ in range(N)]

# We want to find all 2x2 white squares in the original grid.
# Define a 2D array A of size (N-1) x (N-1), where
# A[r][c] = 1 if (r,c),(r,c+1),(r+1,c),(r+1,c+1) are all white ('.'), else 0.

A = [[0]*(N-1) for _ in range(N-1)]
for r in range(N-1):
    for c in range(N-1):
        if (grid[r][c] == '.' and grid[r][c+1] == '.' and
            grid[r+1][c] == '.' and grid[r+1][c+1] == '.'):
            A[r][c] = 1

# Build prefix sums for A to answer queries efficiently.
# prefix[r+1][c+1] = sum of A[0..r][0..c]
prefix = [[0]*(N) for _ in range(N)]
for r in range(N-1):
    row_sum = 0
    for c in range(N-1):
        row_sum += A[r][c]
        prefix[r+1][c+1] = prefix[r][c+1] + row_sum

# For each query (U,D,L,R):
# After painting all cells outside the rectangle black,
# the only 2x2 white squares that remain are those fully inside the rectangle.
# The 2x2 squares inside rectangle (U,D,L,R) correspond to top-left corners
# in rows U to D-1 and columns L to R-1 (1-based indexing).
# So we sum A[r][c] for r in [U-1, D-2], c in [L-1, R-2].

for _ in range(Q):
    U, D, L, R = map(int, input().split())
    if D - U < 1 or R - L < 1:
        # No 2x2 squares possible
        print(0)
        continue
    r1, r2 = U - 1, D - 2
    c1, c2 = L - 1, R - 2
    ans = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
    print(ans)