def count_black_cells(H, W, grid):
    # Directions for adjacency (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Convert grid to a mutable list of lists for easier manipulation
    grid = [list(row) for row in grid]
    
    def is_white(i, j):
        return 0 <= i < H and 0 <= j < W and grid[i][j] == '.'

    # Keep coloring until no more changes happen
    while True:
        to_color = []
        
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '.':
                    count_black_neighbors = sum(
                        1 for di, dj in directions if 0 <= i + di < H and 0 <= j + dj < W and grid[i + di][j + dj] == '#'
                    )
                    if count_black_neighbors == 1:
                        to_color.append((i, j))
        
        if not to_color:
            break
        
        # Color the identified cells black
        for i, j in to_color:
            grid[i][j] = '#'
    
    # Count the total black cells
    return sum(row.count('#') for row in grid)

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

H, W = map(int, data[0].split())
grid = data[1:H + 1]

# Output the result
print(count_black_cells(H, W, grid))