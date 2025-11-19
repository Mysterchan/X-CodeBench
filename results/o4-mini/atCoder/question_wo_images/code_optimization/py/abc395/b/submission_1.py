n = int(input())
for i in range(n):
    # For each cell (i, j), compute the minimum distance to any border.
    # If that distance is even, the cell is '#', otherwise it is '.'
    row = []
    for j in range(n):
        d = min(i, j, n - 1 - i, n - 1 - j)
        row.append('#' if d % 2 == 0 else '.')
    print(''.join(row))