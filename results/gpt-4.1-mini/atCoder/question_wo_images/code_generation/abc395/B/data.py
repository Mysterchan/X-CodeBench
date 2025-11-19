N = int(input())

# Initialize the grid with empty strings (not necessary, but for clarity)
grid = [['' for _ in range(N)] for _ in range(N)]

for i in range(1, N+1):
    j = N + 1 - i
    if i <= j:
        color = '#' if i % 2 == 1 else '.'
        for r in range(i-1, j):
            for c in range(i-1, j):
                grid[r][c] = color

# Print the final grid
for row in grid:
    print(''.join(row))