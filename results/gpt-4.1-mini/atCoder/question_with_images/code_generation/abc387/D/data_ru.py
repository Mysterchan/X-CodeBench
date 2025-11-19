from collections import deque
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
grid = [input().rstrip('\n') for _ in range(H)]

# Найдем координаты S и G
start = None
goal = None
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            goal = (i, j)

# Направления движения:
# Вертикальные: вверх, вниз
vert_moves = [(-1, 0), (1, 0)]
# Горизонтальные: влево, вправо
horiz_moves = [(0, -1), (0, 1)]

# visited[i][j][d] - посещали ли клетку (i,j) с последним ходом направления d
# d = 0 - последний ход был вертикальным
# d = 1 - последний ход был горизонтальным
# Для начальной точки мы можем начать с любого направления, поэтому будем рассматривать оба варианта.

visited = [[[False]*2 for _ in range(W)] for __ in range(H)]

q = deque()

# Инициализируем очередь двумя состояниями: первый ход вертикальный или горизонтальный
# dist[i][j][d] - минимальное количество ходов, чтобы попасть в (i,j) с последним ходом направления d
dist = [[[-1]*2 for _ in range(W)] for __ in range(H)]

# Начинаем с позиции start, без сделанных ходов, но с возможностью сделать первый ход вертикальным или горизонтальным
# Для удобства считаем, что мы "сделали" ход с направлением d, чтобы следующий ход был противоположным
# Но в условии: "Направление первого движения можно выбрать произвольно."
# Значит, мы можем считать, что мы еще не сделали ход, и можем сделать первый ход либо вертикальным, либо горизонтальным.
# Для этого положим в очередь два варианта с dist=0.

si, sj = start
gi, gj = goal

# Помечаем старт как посещенный с обоими направлениями, dist=0
visited[si][sj][0] = True
visited[si][sj][1] = True
dist[si][sj][0] = 0
dist[si][sj][1] = 0
q.append((si, sj, 0))
q.append((si, sj, 1))

while q:
    i, j, last_dir = q.popleft()
    d = dist[i][j][last_dir]
    if (i, j) == (gi, gj):
        print(d)
        sys.exit(0)
    # Следующий ход должен быть противоположного направления
    # Если последний ход был вертикальным (0), следующий ход горизонтальный (1)
    # Если последний ход был горизонтальным (1), следующий ход вертикальный (0)
    next_dir = 1 - last_dir
    moves = horiz_moves if next_dir == 1 else vert_moves
    for di, dj in moves:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W:
            if grid[ni][nj] != '#':
                if not visited[ni][nj][next_dir]:
                    visited[ni][nj][next_dir] = True
                    dist[ni][nj][next_dir] = d + 1
                    q.append((ni, nj, next_dir))

print(-1)