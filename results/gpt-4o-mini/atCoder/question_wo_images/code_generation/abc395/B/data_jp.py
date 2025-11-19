N = int(input())
grid = [['.' for _ in range(N)] for _ in range(N)]

for i in range(1, N + 1):
    j = N + 1 - i
    if i <= j:
        fill_char = '#' if i % 2 == 1 else '.'
        for x in range(i - 1, j):
            for y in range(i - 1, j):
                grid[x][y] = fill_char

for row in grid:
    print(''.join(row))