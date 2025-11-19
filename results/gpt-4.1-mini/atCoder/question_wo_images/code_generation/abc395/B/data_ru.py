N = int(input())

# Инициализируем сетку символами '.' (белый)
grid = [['.' for _ in range(N)] for _ in range(N)]

for i in range(1, N+1):
    j = N + 1 - i
    if i <= j:
        c = '#' if i % 2 == 1 else '.'
        for r in range(i-1, j):
            for c_ in range(i-1, j):
                grid[r][c_] = c

for row in grid:
    print(''.join(row))