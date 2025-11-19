from collections import deque

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# Find start and goal positions
start = None
goal = None
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            goal = (i, j)

# Directions: vertical moves and horizontal moves
# vertical moves: up/down
vertical_moves = [(-1, 0), (1, 0)]
# horizontal moves: left/right
horizontal_moves = [(0, -1), (0, 1)]

# We need to alternate moves: vertical -> horizontal -> vertical -> ...
# The first move direction can be chosen arbitrarily.
# So we consider two states for the first move direction:
# 0: next move is vertical
# 1: next move is horizontal

# visited[i][j][d] = True if cell (i,j) visited with next move direction d
visited = [[[False]*2 for _ in range(W)] for __ in range(H)]

# BFS queue: elements are (i, j, next_move_direction, distance)
# next_move_direction: 0 for vertical next, 1 for horizontal next
queue = deque()

# Initialize queue with start position and both possible next move directions
# distance = 0 at start
queue.append((start[0], start[1], 0, 0))
queue.append((start[0], start[1], 1, 0))
visited[start[0]][start[1]][0] = True
visited[start[0]][start[1]][1] = True

while queue:
    i, j, d, dist = queue.popleft()
    if (i, j) == goal:
        print(dist)
        break

    # Determine next moves based on d
    if d == 0:
        # next move vertical
        for di, dj in vertical_moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W:
                if grid[ni][nj] != '#' and not visited[ni][nj][1]:
                    visited[ni][nj][1] = True
                    queue.append((ni, nj, 1, dist + 1))
    else:
        # next move horizontal
        for di, dj in horizontal_moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W:
                if grid[ni][nj] != '#' and not visited[ni][nj][0]:
                    visited[ni][nj][0] = True
                    queue.append((ni, nj, 0, dist + 1))
else:
    # If we exit the while loop without break, no path found
    print(-1)