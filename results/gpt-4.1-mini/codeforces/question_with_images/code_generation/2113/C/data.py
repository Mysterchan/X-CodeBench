import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    grid = [input().strip() for __ in range(n)]

    # We want to find the maximum gold collected by detonating dynamite in any empty cell.
    # The explosion affects a square of side 2k+1 centered at (x,y).
    # Gold on the boundary of this square is collected.
    # Gold strictly inside the square disappears (not collected).
    # The explosion square can extend beyond the mine boundaries.
    # Dynamite can only be detonated in empty cells ('.').

    # The boundary of the square consists of:
    # - top row: (x-k, y-k) to (x-k, y+k)
    # - bottom row: (x+k, y-k) to (x+k, y+k)
    # - left column: (x-k+1 to x+k-1, y-k)
    # - right column: (x-k+1 to x+k-1, y+k)

    # We need to count how many gold cells ('g') are on the boundary of the square for each empty cell.

    # To do this efficiently, we can precompute prefix sums of gold cells in rows and columns.

    # Precompute prefix sums for rows and columns:
    # row_gold[i][j] = number of gold in row i from column 0 to j-1
    # col_gold[j][i] = number of gold in column j from row 0 to i-1

    # We'll create two prefix sums:
    # row_psum[i][j+1] = number of gold in row i up to column j
    # col_psum[j][i+1] = number of gold in column j up to row i

    row_psum = [[0]*(m+1) for _ in range(n)]
    col_psum = [[0]*(n+1) for _ in range(m)]

    for i in range(n):
        for j in range(m):
            row_psum[i][j+1] = row_psum[i][j] + (1 if grid[i][j] == 'g' else 0)
    for j in range(m):
        for i in range(n):
            col_psum[j][i+1] = col_psum[j][i] + (1 if grid[i][j] == 'g' else 0)

    max_gold = 0

    for x in range(n):
        for y in range(m):
            if grid[x][y] != '.':
                continue

            # Calculate boundary coordinates
            top = x - k
            bottom = x + k
            left = y - k
            right = y + k

            gold_count = 0

            # top row boundary
            if 0 <= top < n:
                c1 = max(left, 0)
                c2 = min(right, m-1)
                if c1 <= c2:
                    gold_count += row_psum[top][c2+1] - row_psum[top][c1]

            # bottom row boundary
            if 0 <= bottom < n and bottom != top:
                c1 = max(left, 0)
                c2 = min(right, m-1)
                if c1 <= c2:
                    gold_count += row_psum[bottom][c2+1] - row_psum[bottom][c1]

            # left column boundary (excluding corners already counted)
            if 0 <= left < m:
                r1 = max(top+1, 0)
                r2 = min(bottom-1, n-1)
                if r1 <= r2:
                    gold_count += col_psum[left][r2+1] - col_psum[left][r1]

            # right column boundary (excluding corners already counted)
            if 0 <= right < m and right != left:
                r1 = max(top+1, 0)
                r2 = min(bottom-1, n-1)
                if r1 <= r2:
                    gold_count += col_psum[right][r2+1] - col_psum[right][r1]

            if gold_count > max_gold:
                max_gold = gold_count

    print(max_gold)