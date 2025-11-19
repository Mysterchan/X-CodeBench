import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(H)]

# Черные клетки отмечаем True, белые False
black = [[(c == '#') for c in row] for row in grid]

# Соседи по 4 направлениям
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Для каждой белой клетки считаем количество соседей, окрашенных в черный цвет
black_neighbors = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if not black[i][j]:
            cnt = 0
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if 0 <= ni < H and 0 <= nj < W and black[ni][nj]:
                    cnt += 1
            black_neighbors[i][j] = cnt

# Очередь для клеток, которые нужно покрасить в черный (белые с ровно одним черным соседом)
q = deque()
for i in range(H):
    for j in range(W):
        if not black[i][j] and black_neighbors[i][j] == 1:
            q.append((i, j))

while q:
    i, j = q.popleft()
    if black[i][j]:
        continue
    black[i][j] = True
    # Обновляем соседей
    for di, dj in dirs:
        ni, nj = i+di, j+dj
        if 0 <= ni < H and 0 <= nj < W and not black[ni][nj]:
            black_neighbors[ni][nj] += 1
            if black_neighbors[ni][nj] == 1:
                q.append((ni, nj))

# Подсчитываем количество черных клеток
ans = sum(sum(row) for row in black)
print(ans)