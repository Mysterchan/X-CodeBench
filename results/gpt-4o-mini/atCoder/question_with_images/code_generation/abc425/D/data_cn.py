H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

# Directions for the four possible neighboring cells
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
changed = True

while changed:
    changed = False
    new_grid = [row[:] for row in grid]  # Create a copy of the current grid
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                # Count black neighbors
                black_neighbors = sum(1 for di, dj in directions if 0 <= i + di < H and 0 <= j + dj < W and grid[i + di][j + dj] == '#')
                
                if black_neighbors == 1:
                    new_grid[i][j] = '#'
                    changed = True
    
    grid = new_grid  # Update grid to the new state

# Count the number of black cells
black_count = sum(row.count('#') for row in grid)
print(black_count)