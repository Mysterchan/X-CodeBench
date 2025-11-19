def can_form_rectangle(H, W, grid):
    min_row, max_row = H, -1
    min_col, max_col = W, -1
    
    # Determine the boundaries of the black cells
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                if i < min_row:
                    min_row = i
                if i > max_row:
                    max_row = i
                if j < min_col:
                    min_col = j
                if j > max_col:
                    max_col = j
    
    # Check the rectangle area defined by (min_row, min_col) to (max_row, max_col)
    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if grid[i][j] == '.':
                return "No"
    
    # Check for any black cells within the defined rectangular area
    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if grid[i][j] == '?':
                continue  # '?' can be painted either way
            if grid[i][j] == '#':
                continue  # '#' is already black
            
    return "Yes"

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

H, W = map(int, data[0].split())
grid = data[1:H+1]

# Output the result
print(can_form_rectangle(H, W, grid))