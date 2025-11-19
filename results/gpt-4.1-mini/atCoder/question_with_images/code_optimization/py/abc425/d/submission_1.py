import sys
input = sys.stdin.readline

H, W = map(int, input().split())
S = [list(input().rstrip()) for _ in range(H)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# Convert '#' to 0 (black), '.' to -1 (white)
black = [[-1]*W for _ in range(H)]
queue = []
ans = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            black[i][j] = 0
            ans += 1

# For each white cell, count black neighbors
black_neighbors = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if black[i][j] == -1:
            cnt = 0
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if 0 <= ni < H and 0 <= nj < W and black[ni][nj] == 0:
                    cnt += 1
            black_neighbors[i][j] = cnt
            if cnt == 1:
                queue.append((i, j))

# BFS-like approach to color cells black
while queue:
    i, j = queue.pop()
    if black[i][j] != -1:
        continue
    black[i][j] = 0
    ans += 1
    for k in range(4):
        ni, nj = i + dy[k], j + dx[k]
        if 0 <= ni < H and 0 <= nj < W and black[ni][nj] == -1:
            black_neighbors[ni][nj] += 1
            if black_neighbors[ni][nj] == 1:
                queue.append((ni, nj))

print(ans)