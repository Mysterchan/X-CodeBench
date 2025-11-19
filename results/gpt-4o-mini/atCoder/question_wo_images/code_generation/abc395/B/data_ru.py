def create_pattern(N):
    # Initialize the grid with all cells as '.'
    grid = [['.' for _ in range(N)] for _ in range(N)]
    
    for i in range(1, N + 1):
        j = N + 1 - i
        if i <= j:
            color = '#' if i % 2 == 1 else '.'
            for row in range(i - 1, j):
                for col in range(i - 1, j):
                    grid[row][col] = color
    
    # Convert each row list to a string and print the result
    for row in grid:
        print(''.join(row))

# Read input
N = int(input().strip())
create_pattern(N)