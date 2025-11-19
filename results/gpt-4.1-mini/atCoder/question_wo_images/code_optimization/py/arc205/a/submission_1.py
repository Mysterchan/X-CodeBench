import sys
input = sys.stdin.readline

n, q = map(int, input().split())
s = [input().rstrip() for _ in range(n)]

# Precompute a 2D prefix sum of 2x2 white squares
# s_score[r][c] = 1 if the 2x2 block with top-left corner (r,c) is all '.'
# Dimensions: (n-1) x (n-1)
s_score = [[0]*(n-1) for _ in range(n-1)]
for r in range(n-1):
    row_s = s[r]
    row_s_next = s[r+1]
    for c in range(n-1):
        if row_s[c] == '.' and row_s[c+1] == '.' and row_s_next[c] == '.' and row_s_next[c+1] == '.':
            s_score[r][c] = 1

# Build 2D prefix sum for s_score
# prefix[r+1][c+1] = sum of s_score[0..r][0..c]
prefix = [[0]*(n) for _ in range(n)]
for r in range(n-1):
    row_ps = prefix[r+1]
    row_s_score = s_score[r]
    for c in range(n-1):
        row_ps[c+1] = row_ps[c] + s_score[r][c]
for r in range(1, n):
    row_ps = prefix[r]
    row_ps_prev = prefix[r-1]
    for c in range(n):
        row_ps[c] += row_ps_prev[c]

# For each query, answer by summing s_score in the rectangle:
# rows: u to d-1 (0-based)
# cols: l to r-1 (0-based)
# Because the 2x2 blocks are indexed by top-left corner, the valid indices are from 0 to n-2
# So for query (U,D,L,R) 1-based:
# We consider blocks with top-left corners in rows [U-1, D-2], cols [L-1, R-2]
# If D-2 < U-1 or R-2 < L-1, answer is 0

for _ in range(q):
    U, D, L, R = map(int, input().split())
    r1 = U - 1
    r2 = D - 2
    c1 = L - 1
    c2 = R - 2
    if r2 < r1 or c2 < c1:
        print(0)
        continue
    ans = prefix[r2+1][c2+1] - prefix[r2+1][c1] - prefix[r1][c2+1] + prefix[r1][c1]
    print(ans)