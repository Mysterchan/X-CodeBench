h, w = map(int, input().split())
s = [input() for _ in range(h)]

min_row, max_row = h, -1
min_col, max_col = w, -1

# Find bounding rectangle of black cells
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            if i < min_row:
                min_row = i
            if i > max_row:
                max_row = i
            if j < min_col:
                min_col = j
            if j > max_col:
                max_col = j

# Check all cells inside bounding rectangle
for i in range(min_row, max_row + 1):
    for j in range(min_col, max_col + 1):
        if s[i][j] == '.':
            print("No")
            exit()

print("Yes")