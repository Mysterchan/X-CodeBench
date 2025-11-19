n, q = map(int, input().split())
s = []
for _ in range(n):
    s.append(list(input()))

# Build 2D grid marking where 2x2 white squares exist (at top-left corner)
s_score = [[0] * n for _ in range(n)]

for row in range(n - 1):
    for col in range(n - 1):
        if s[row][col] == s[row][col + 1] == s[row + 1][col] == s[row + 1][col + 1] == ".":
            s_score[row][col] = 1

# Build 2D prefix sum
prefix = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] = s_score[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

for _ in range(q):
    u, d, l, r = map(int, input().split())
    # We need 2x2 squares with top-left at (row, col) where u <= row < d and l <= col < r
    # But the 2x2 square needs bottom-right at (row+1, col+1) which must also be in bounds
    # So top-left can be at row in [u, d-1) and col in [l, r-1)
    # In 0-indexed: row in [u-1, d-2] and col in [l-1, r-2]
    
    # Convert to 0-indexed bounds for valid top-left corners
    r1 = u - 1  # inclusive
    r2 = d - 2  # inclusive
    c1 = l - 1  # inclusive
    c2 = r - 2  # inclusive
    
    if r2 >= r1 and c2 >= c1:
        # Query 2D prefix sum for rectangle [r1, r2] x [c1, c2] (0-indexed)
        # In prefix array (1-indexed): [r1+1, r2+1] x [c1+1, c2+1]
        ans = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
    else:
        ans = 0
    
    print(ans)