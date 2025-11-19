H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

# Directions for N, S, E, W
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Mark black cells
to_black = set()

# Iterate until no changes
while True:
    new_black = set()
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                black_neighbors = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '#':
                        black_neighbors += 1
                if black_neighbors == 1:
                    new_black.add((i, j))
    if not new_black:
        break
    for i, j in new_black:
        grid[i][j] = '#'

# Count the total number of black cells
black_count = sum(row.count('#') for row in grid)
print(black_count)