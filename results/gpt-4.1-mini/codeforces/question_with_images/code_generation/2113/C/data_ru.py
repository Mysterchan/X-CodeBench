import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    grid = [input().strip() for __ in range(n)]

    # We want to find, for each empty cell ('.'), how many gold cells ('g') lie on the border
    # of the square of side 2k+1 centered at that cell.
    # The border consists of:
    # - top row: (x-k, y-k) to (x-k, y+k)
    # - bottom row: (x+k, y-k) to (x+k, y+k)
    # - left column: (x-k+1, y-k) to (x+k-1, y-k)
    # - right column: (x-k+1, y+k) to (x+k-1, y+k)
    #
    # Coordinates outside the grid are ignored (no gold there).
    #
    # To efficiently count gold on these borders for all empty cells, we use prefix sums.
    #
    # We'll create prefix sums for rows and columns separately:
    # - row_gold[i][j]: number of gold in row i from column 0 to j-1
    # - col_gold[j][i]: number of gold in column j from row 0 to i-1
    #
    # Then for each empty cell, we sum:
    # top row gold = row_gold[x-k][y+k+1] - row_gold[x-k][y-k] if x-k in [0,n-1]
    # bottom row gold = row_gold[x+k][y+k+1] - row_gold[x+k][y-k] if x+k in [0,n-1]
    # left col gold = col_gold[y-k][x+k] - col_gold[y-k][x-k+1] if y-k in [0,m-1]
    # right col gold = col_gold[y+k][x+k] - col_gold[y+k][x-k+1] if y+k in [0,m-1]
    #
    # Note: for left and right columns, the range excludes corners (top and bottom rows),
    # so from x-k+1 to x+k-1 inclusive.
    #
    # We must handle boundaries carefully.

    # Build prefix sums for rows
    row_gold = [[0]*(m+1) for __ in range(n)]
    for i in range(n):
        for j in range(m):
            row_gold[i][j+1] = row_gold[i][j] + (1 if grid[i][j] == 'g' else 0)

    # Build prefix sums for columns
    col_gold = [[0]*(n+1) for __ in range(m)]
    for j in range(m):
        for i in range(n):
            col_gold[j][i+1] = col_gold[j][i] + (1 if grid[i][j] == 'g' else 0)

    max_gold = 0
    side = 2*k + 1

    for x in range(n):
        for y in range(m):
            if grid[x][y] != '.':
                continue

            gold_count = 0

            top = x - k
            bottom = x + k
            left = y - k
            right = y + k

            # top row
            if 0 <= top < n:
                c1 = max(left, 0)
                c2 = min(right, m-1)
                if c1 <= c2:
                    gold_count += row_gold[top][c2+1] - row_gold[top][c1]

            # bottom row
            if 0 <= bottom < n:
                c1 = max(left, 0)
                c2 = min(right, m-1)
                if c1 <= c2:
                    gold_count += row_gold[bottom][c2+1] - row_gold[bottom][c1]

            # left column (excluding corners)
            if 0 <= left < m:
                r1 = max(top+1, 0)
                r2 = min(bottom-1, n-1)
                if r1 <= r2:
                    gold_count += col_gold[left][r2+1] - col_gold[left][r1]

            # right column (excluding corners)
            if 0 <= right < m:
                r1 = max(top+1, 0)
                r2 = min(bottom-1, n-1)
                if r1 <= r2:
                    gold_count += col_gold[right][r2+1] - col_gold[right][r1]

            if gold_count > max_gold:
                max_gold = gold_count

    print(max_gold)