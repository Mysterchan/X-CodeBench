H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# Initialize min and max bounds for black cells
min_row, max_row = H, -1
min_col, max_col = W, -1

# Find bounds of the black cells
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

# Now check if the rectangle defined by (min_row, min_col) to (max_row, max_col) 
# contains only black cells or uncolored cells (?), and all cells outside are white (.)
is_possible = True
for i in range(min_row, max_row + 1):
    for j in range(min_col, max_col + 1):
        if grid[i][j] == '.':
            is_possible = False
            break
    if not is_possible:
        break

# Check all cells outside the rectangle are white
if is_possible:
    for i in range(H):
        for j in range(W):
            if (i < min_row or i > max_row or j < min_col or j > max_col) and grid[i][j] == '#':
                is_possible = False
                break
        if not is_possible:
            break

print("Yes" if is_possible else "No")