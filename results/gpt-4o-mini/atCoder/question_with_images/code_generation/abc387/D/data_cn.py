from collections import deque

def min_moves_to_goal(H, W, grid):
    start = goal = None
    
    # Find the start and goal positions
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    queue = deque([(start[0], start[1], 0, -1)])  # (current_x, current_y, moves, last_direction)
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, moves, last_direction = queue.popleft()
        
        # Check if reached goal
        if (x, y) == goal:
            return moves
        
        # Determine next movement directions
        if last_direction == -1:  # initial move can be any direction
            next_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        else:
            next_directions = [(1, 0), (-1, 0)] if last_direction in [0, 1] else [(0, 1), (0, -1)]

        for dx, dy in next_directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1, (dx, dy)))
    
    return -1

# Reading input
H, W = map(int, input().strip().split())
grid = [input().strip() for _ in range(H)]

# Output result
print(min_moves_to_goal(H, W, grid))