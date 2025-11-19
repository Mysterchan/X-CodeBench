from collections import deque

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

# Find start and goal positions
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            goal = (i, j)

# Directions: vertical moves and horizontal moves
# We'll alternate moves: if last move was vertical, next must be horizontal, and vice versa.
# We represent direction as 0 for vertical, 1 for horizontal.
# For vertical moves: up/down; for horizontal moves: left/right.

# visited[i][j][d] = True if cell (i,j) visited with last move direction d
visited = [[[False]*2 for _ in range(W)] for __ in range(H)]

# Initialize queue with two states: starting with vertical move next, and horizontal move next
# Each element: (row, col, last_move_direction, distance)
# last_move_direction: 0 means last move was vertical, so next move must be horizontal
# But since we haven't moved yet, we can consider last_move_direction as the direction we will move next
# To avoid confusion, we can store next_move_direction instead:
# Let's define next_move_direction: 0 means next move vertical, 1 means next move horizontal
# So at start, we can try both next_move_direction = 0 and 1

queue = deque()
# distance is number of moves made so far
queue.append((start[0], start[1], 0, 0))  # next move vertical
queue.append((start[0], start[1], 1, 0))  # next move horizontal
visited[start[0]][start[1]][0] = True
visited[start[0]][start[1]][1] = True

while queue:
    r, c, next_dir, dist = queue.popleft()
    if (r, c) == goal:
        print(dist)
        break

    if next_dir == 0:
        # next move vertical: up/down
        for nr in (r-1, r+1):
            if 0 <= nr < H and grid[nr][c] != '#':
                if not visited[nr][c][1]:
                    visited[nr][c][1] = True
                    queue.append((nr, c, 1, dist+1))
    else:
        # next move horizontal: left/right
        for nc in (c-1, c+1):
            if 0 <= nc < W and grid[r][nc] != '#':
                if not visited[r][nc][0]:
                    visited[r][nc][0] = True
                    queue.append((r, nc, 0, dist+1))
else:
    # If we exit the while loop without break, no path found
    print(-1)