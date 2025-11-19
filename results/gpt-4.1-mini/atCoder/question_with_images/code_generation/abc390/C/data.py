H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# Find the bounding rectangle of all black cells (#)
min_r, max_r = H, -1
min_c, max_c = W, -1

for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            if i < min_r:
                min_r = i
            if i > max_r:
                max_r = i
            if j < min_c:
                min_c = j
            if j > max_c:
                max_c = j

# Check if all cells inside the bounding rectangle can be black
# and all cells outside must be white.
# For cells inside the rectangle:
#   - if cell is '.' (white), impossible
# For cells outside the rectangle:
#   - if cell is '#' (black), impossible

for i in range(H):
    for j in range(W):
        inside = (min_r <= i <= max_r) and (min_c <= j <= max_c)
        if inside:
            # Must be black or paintable black (?)
            if grid[i][j] == '.':
                print("No")
                exit()
        else:
            # Must be white or paintable white (?)
            if grid[i][j] == '#':
                print("No")
                exit()

print("Yes")