from collections import deque

def can_reach_destination(H, W, K, obstacles):
    grid = [[0] * (W + 1) for _ in range(H + 1)]
    
    for r, c in obstacles:
        grid[r][c] = 1  # Mark obstacles

    if grid[1][1] == 1 or grid[H][W] == 1:
        return "No"

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(1, 1)])
    visited = [[False] * (W + 1) for _ in range(H + 1)]
    visited[1][1] = True

    while queue:
        x, y = queue.popleft()
        if (x, y) == (H, W):
            return "Yes"
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= H and 1 <= ny <= W and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return "No"

# Read input
H, W, K = map(int, input().split())
obstacles = [tuple(map(int, input().split())) for _ in range(K)]

# Get the result and print it
result = can_reach_destination(H, W, K, obstacles)
print(result)