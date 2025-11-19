h, w = map(int, input().split())
s = [input().strip() for _ in range(h)]

# Find the bounding box of all black cells
top, bottom = h, -1
left, right = w, -1

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            top = min(top, i)
            bottom = max(bottom, i)
            left = min(left, j)
            right = max(right, j)

# Check if all cells in the bounding box are valid
for i in range(top, bottom + 1):
    for j in range(left, right + 1):
        if s[i][j] == '.':
            print("No")
            exit()

print("Yes")