n = int(input())
grid = [['#' for _ in range(n)] for _ in range(n)]

for i in range(1, n + 1):
    j = n + 1 - i
    if i <= j:
        fill_char = '.' if i % 2 == 0 else '#'
        for x in range(i - 1, j):
            for y in range(i - 1, j):
                grid[x][y] = fill_char

for row in grid:
    print(''.join(row))