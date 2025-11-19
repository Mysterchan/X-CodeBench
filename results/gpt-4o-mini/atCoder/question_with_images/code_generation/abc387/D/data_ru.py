from collections import deque

def min_moves_to_target(H, W, grid):
    # Directions for vertical and horizontal moves
    vertical_moves = [(1, 0), (-1, 0)]
    horizontal_moves = [(0, 1), (0, -1)]
    
    # Find start and goal positions
    start = goal = None
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)

    # BFS initialization
    queue = deque([(start[0], start[1], 0, True)])  # (x, y, moves, is_vertical)
    visited = set()
    visited.add((start[0], start[1], True))  # (x, y, is_vertical)

    while queue:
        x, y, moves, is_vertical = queue.popleft()

        # Check if we reached the goal
        if (x, y) == goal:
            return moves

        # Determine next moves based on current direction
        if is_vertical:
            next_moves = vertical_moves
            next_is_vertical = False
        else:
            next_moves = horizontal_moves
            next_is_vertical = True

        # Explore all possible next moves
        for dx, dy in next_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#':
                if (nx, ny, next_is_vertical) not in visited:
                    visited.add((nx, ny, next_is_vertical))
                    queue.append((nx, ny, moves + 1, next_is_vertical))

    return -1

# Read input
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# Get the result and print it
result = min_moves_to_target(H, W, grid)
print(result)