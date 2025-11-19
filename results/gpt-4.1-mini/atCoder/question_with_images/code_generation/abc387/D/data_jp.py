from collections import deque

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# スタートとゴールの位置を探す
start = goal = None
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            goal = (i, j)

# 移動方向の定義
# 縦移動: 上下 (dx, dy) = (-1,0), (1,0)
# 横移動: 左右 (dx, dy) = (0,-1), (0,1)
vertical_moves = [(-1, 0), (1, 0)]
horizontal_moves = [(0, -1), (0, 1)]

# BFSで状態管理
# 状態は (i, j, last_move_direction)
# last_move_direction: 0=縦移動, 1=横移動, 2=初期状態(まだ移動していない)
# 初期状態は last_move_direction=2 として、最初の移動は縦横どちらでも可能にする

# dist[i][j][d] := マス(i,j)にlast_move_direction=dで到達するまでの移動回数の最小値
INF = 10**9
dist = [[[INF]*3 for _ in range(W)] for __ in range(H)]

si, sj = start
dist[si][sj][2] = 0
q = deque()
q.append((si, sj, 2))

while q:
    i, j, d = q.popleft()
    cur_dist = dist[i][j][d]

    # 次の移動方向を決める
    # d=2(初期)なら縦横どちらも可能
    # d=0(縦移動)なら次は横移動(1)
    # d=1(横移動)なら次は縦移動(0)
    next_dirs = []
    if d == 2:
        next_dirs = [0, 1]
    elif d == 0:
        next_dirs = [1]
    else:
        next_dirs = [0]

    for nd in next_dirs:
        moves = vertical_moves if nd == 0 else horizontal_moves
        for dx, dy in moves:
            ni, nj = i + dx, j + dy
            if 0 <= ni < H and 0 <= nj < W:
                if grid[ni][nj] != '#':
                    if dist[ni][nj][nd] > cur_dist + 1:
                        dist[ni][nj][nd] = cur_dist + 1
                        q.append((ni, nj, nd))

gi, gj = goal
ans = min(dist[gi][gj][0], dist[gi][gj][1])
print(ans if ans != INF else -1)