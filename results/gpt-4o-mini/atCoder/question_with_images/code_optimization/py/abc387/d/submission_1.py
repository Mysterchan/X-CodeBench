from collections import deque

H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# Locate start and goal positions
start = goal = None
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            goal = (i, j)

# BFS to find the minimum moves
def bfs(start, goal, first_move_vertical):
    queue = deque([(start[0], start[1], 0)])  # (row, column, move_count)
    visited = set()
    visited.add((start[0], start[1], first_move_vertical))

    while queue:
        r, c, count = queue.popleft()

        if (r, c) == goal:
            return count

        # Determine next possible moves based on current move direction
        if first_move_vertical:
            # Move horizontally next
            directions = [(0, 1), (0, -1)]  # right, left
            next_move_vertical = False
        else:
            # Move vertically next
            directions = [(1, 0), (-1, 0)]  # down, up
            next_move_vertical = True

        # Explore all valid moves
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check bounds and obstacles
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#':
                if (nr, nc, next_move_vertical) not in visited:
                    visited.add((nr, nc, next_move_vertical))
                    queue.append((nr, nc, count + 1))

    return -1

# Run BFS for both starting directions
result1 = bfs(start, goal, True)  # Starting with vertical move
result2 = bfs(start, goal, False) # Starting with horizontal move

# Find the minimum valid result
if result1 == -1 and result2 == -1:
    print(-1)
else:
    if result1 == -1:
        print(result2)
    elif result2 == -1:
        print(result1)
    else:
        print(min(result1, result2))