import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
S = [input().rstrip() for _ in range(N)]

# 2x2白マスの判定
# dp[r][c] = 1 if (r,c),(r,c+1),(r+1,c),(r+1,c+1) all white else 0
dp = [[0]*(N) for _ in range(N)]
for r in range(N-1):
    for c in range(N-1):
        if (S[r][c] == '.' and S[r][c+1] == '.' and
            S[r+1][c] == '.' and S[r+1][c+1] == '.'):
            dp[r][c] = 1

# 2D prefix sum for dp
psum = [[0]*(N+1) for _ in range(N+1)]
for r in range(N):
    for c in range(N):
        psum[r+1][c+1] = psum[r+1][c] + psum[r][c+1] - psum[r][c] + dp[r][c]

# For each query:
# We paint black all cells outside the rectangle [U,D]x[L,R].
# So only cells inside remain as original.
# The 2x2 white squares that remain must be fully inside the rectangle.
# Because if any cell of the 2x2 square is outside, it is blackened.
# So the count of 2x2 white squares fully inside [U,D]x[L,R] is:
# sum of dp[r][c] for r in [U,D-1], c in [L,R-1]
# (since dp indices correspond to top-left cell of 2x2 square)
#
# The maximum number of operations is exactly the number of such 2x2 white squares,
# because each operation removes one 2x2 white square by blackening one cell.
# They cannot overlap in a way to increase the count beyond the number of initial 2x2 white squares.

for _ in range(Q):
    U, D, L, R = map(int, input().split())
    # Adjust indices for prefix sums (1-based)
    # dp indices: r in [U, D-1], c in [L, R-1]
    if D - 1 < U or R - 1 < L:
        # No 2x2 squares possible
        print(0)
        continue
    res = psum[D-1][R-1] - psum[U-1][R-1] - psum[D-1][L-1] + psum[U-1][L-1]
    print(res)