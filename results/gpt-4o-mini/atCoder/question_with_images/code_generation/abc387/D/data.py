from collections import deque

def min_moves_to_goal(H, W, grid):
    # Find start (S) and goal (G) positions
    start = goal = None
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'G':
                goal = (r, c)

    # Directions for moving (right, down, left, up)
    horizontal_moves = [(0, 1), (0, -1)]
    vertical_moves = [(1, 0), (-1, 0)]
    
    # BFS setup with initial conditions
    queue = deque([(start[0], start[1], 0, 0)])  # (row, col, depth, move_type)
    visited = set()
    visited.add((start[0], start[1], 0))

    while queue:
        r, c, depth, move_type = queue.popleft()

        if (r, c) == goal:
            return depth

        if move_type == 0:  # Horizontal move next
            for dr, dc in horizontal_moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#' and (nr, nc, 1) not in visited:
                    visited.add((nr, nc, 1))
                    queue.append((nr, nc, depth + 1, 1))
        else:  # Vertical move next
            for dr, dc in vertical_moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#' and (nr, nc, 0) not in visited:
                    visited.add((nr, nc, 0))
                    queue.append((nr, nc, depth + 1, 0))

    return -1

# Read input
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# Get the result and print
result = min_moves_to_goal(H, W, grid)
print(result)