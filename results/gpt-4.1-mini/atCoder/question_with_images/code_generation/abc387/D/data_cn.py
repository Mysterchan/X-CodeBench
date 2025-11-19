from collections import deque
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
grid = [input().rstrip('\n') for _ in range(H)]

# 找起點和終點
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            sx, sy = i, j
        elif grid[i][j] == 'G':
            gx, gy = i, j

# 狀態：位置 (x,y) + 上一步移動方向
# 上一步移動方向用0表示未定（起點），1表示垂直移動，2表示水平移動
# 移動方向交替：如果上一步是垂直，下一步必須水平；反之亦然
# 起點可選擇任意方向開始移動，因此起點狀態有兩種方向可選

# BFS
# dist[x][y][d] 表示到達 (x,y) 且上一步移動方向為 d 的最短距離
# d: 0=起點未移動, 1=垂直, 2=水平
dist = [[[-1]*3 for _ in range(W)] for __ in range(H)]
dist[sx][sy][0] = 0
q = deque()
q.append((sx, sy, 0))

# 移動方向
# 垂直方向：上下
vert_moves = [(-1,0),(1,0)]
# 水平方向：左右
hori_moves = [(0,-1),(0,1)]

while q:
    x, y, d = q.popleft()
    cur_dist = dist[x][y][d]
    if (x, y) == (gx, gy):
        print(cur_dist)
        sys.exit(0)
    # 根據上一步方向決定下一步可走方向
    if d == 0:
        # 起點，下一步可選擇垂直或水平
        # 垂直方向
        for dx, dy in vert_moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#':
                if dist[nx][ny][1] == -1:
                    dist[nx][ny][1] = cur_dist + 1
                    q.append((nx, ny, 1))
        # 水平方向
        for dx, dy in hori_moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#':
                if dist[nx][ny][2] == -1:
                    dist[nx][ny][2] = cur_dist + 1
                    q.append((nx, ny, 2))
    elif d == 1:
        # 上一步是垂直，下一步必須水平
        for dx, dy in hori_moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#':
                if dist[nx][ny][2] == -1:
                    dist[nx][ny][2] = cur_dist + 1
                    q.append((nx, ny, 2))
    else:
        # 上一步是水平，下一步必須垂直
        for dx, dy in vert_moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#':
                if dist[nx][ny][1] == -1:
                    dist[nx][ny][1] = cur_dist + 1
                    q.append((nx, ny, 1))

print(-1)