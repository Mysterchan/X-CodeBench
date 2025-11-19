def count_black_cells_after_infection(H, W, grid):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    black_cells = set()
    white_cells = set()

    # Initialize the sets of black and white cells
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                black_cells.add((i, j))
            else:
                white_cells.add((i, j))

    # Perform infection until no new white cells can be turned black
    while True:
        newly_colored_black = set()
        for (i, j) in white_cells:
            black_neighbors = sum((i + di, j + dj) in black_cells for di, dj in directions)
            if black_neighbors == 1:
                newly_colored_black.add((i, j))

        if not newly_colored_black:
            break
        
        black_cells.update(newly_colored_black)
        white_cells.difference_update(newly_colored_black)

    return len(black_cells)

# Read input
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    H, W = map(int, data[0].split())
    grid = data[1:H + 1]
    
    result = count_black_cells_after_infection(H, W, grid)
    print(result)