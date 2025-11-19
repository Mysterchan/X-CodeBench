import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for __ in range(n)]

    # Precompute max in each row and max in each column
    max_row = [max(row) for row in matrix]
    max_col = [max(matrix[i][j] for i in range(n)) for j in range(m)]

    # We want to minimize the maximum value after decreasing all elements in row r and column c by 1
    # After operation:
    # For row r: all elements decrease by 1
    # For column c: all elements decrease by 1
    # The intersection cell (r,c) is decreased twice, but since we only care about max value, 
    # the max in row r and max in column c both decrease by 1.
    #
    # The maximum value after operation is:
    # max(
    #   max_row[r] - 1,
    #   max_col[c] - 1,
    #   max of all other rows and columns (unchanged)
    # )
    #
    # But since max_row and max_col are independent, the max after operation is:
    # max(
    #   max(max_row[i] for i != r),
    #   max(max_col[j] for j != c),
    #   max_row[r] - 1,
    #   max_col[c] - 1
    # )
    #
    # To efficiently compute max excluding one element, we precompute prefix and suffix max arrays for rows and columns.

    # Precompute prefix and suffix max for rows
    prefix_max_row = [0] * n
    suffix_max_row = [0] * n
    prefix_max_row[0] = max_row[0]
    for i in range(1, n):
        prefix_max_row[i] = max(prefix_max_row[i-1], max_row[i])
    suffix_max_row[-1] = max_row[-1]
    for i in range(n-2, -1, -1):
        suffix_max_row[i] = max(suffix_max_row[i+1], max_row[i])

    # Precompute prefix and suffix max for columns
    prefix_max_col = [0] * m
    suffix_max_col = [0] * m
    prefix_max_col[0] = max_col[0]
    for j in range(1, m):
        prefix_max_col[j] = max(prefix_max_col[j-1], max_col[j])
    suffix_max_col[-1] = max_col[-1]
    for j in range(m-2, -1, -1):
        suffix_max_col[j] = max(suffix_max_col[j+1], max_col[j])

    ans = 10**9
    for r in range(n):
        # max row excluding r
        max_row_excl = prefix_max_row[r-1] if r > 0 else -1
        if r < n-1:
            max_row_excl = max(max_row_excl, suffix_max_row[r+1])

        for c in range(m):
            # max col excluding c
            max_col_excl = prefix_max_col[c-1] if c > 0 else -1
            if c < m-1:
                max_col_excl = max(max_col_excl, suffix_max_col[c+1])

            # max after operation
            cur_max = max(max_row_excl, max_col_excl, max_row[r] - 1, max_col[c] - 1)
            if cur_max < ans:
                ans = cur_max

    print(ans)