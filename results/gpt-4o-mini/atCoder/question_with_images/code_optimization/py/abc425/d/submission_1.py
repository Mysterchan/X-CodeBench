H, W = map(int, input().split())
S = [list(input().strip()) for _ in range(H)]
ans = 0

# Directions for up, down, left, right
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# Count initial black cells and mark them in a set for quick access
black_cells = set()
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            black_cells.add((i, j))
            ans += 1
            S[i][j] = 0  # Changing black cells to 0 for indication

# Loop until no new white cells become black
while True:
    new_black_cells = set()
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                black_count = sum((i + dy[k], j + dx[k]) in black_cells for k in range(4))
                if black_count == 1:
                    new_black_cells.add((i, j))
    
    if not new_black_cells:
        break

    for cell in new_black_cells:
        S[cell[0]][cell[1]] = 1  # A flag indicating the cell is newly coated black
        black_cells.add(cell)
        ans += 1

print(ans)