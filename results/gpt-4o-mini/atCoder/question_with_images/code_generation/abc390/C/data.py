def can_form_rectangle(H, W, grid):
    # Find the boundaries of the black cells
    top, bottom, left, right = H + 1, -1, W + 1, -1
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                top = min(top, i)
                bottom = max(bottom, i)
                left = min(left, j)
                right = max(right, j)

    # Check if all cells within the found boundaries can be black
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if grid[i][j] == '.':  # Found a white cell in the rectangle
                return "No"
            if grid[i][j] == '?':  # Counted a question mark, can be painted
                continue
    
    return "Yes"


# Read input
import sys
input = sys.stdin.read
data = input().strip().splitlines()

H, W = map(int, data[0].split())
grid = data[1:H + 1]

# Solve the problem
result = can_form_rectangle(H, W, grid)
print(result)