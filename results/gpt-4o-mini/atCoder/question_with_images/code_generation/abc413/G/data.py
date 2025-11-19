def can_reach_destination(H, W, K, obstacles):
    from collections import deque

    # Create a grid to mark obstacles
    grid = [[0] * (W + 1) for _ in range(H + 1)]
    
    # Mark the obstacles in the grid
    for r, c in obstacles:
        grid[r][c] = 1

    # Directions for moving in the grid (down, up, right, left)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # BFS initialization
    queue = deque([(1, 1)])  # Start from (1, 1)
    visited = set((1, 1))  # Mark the starting cell as visited

    while queue:
        x, y = queue.popleft()
        
        # If we reach the destination
        if (x, y) == (H, W):
            return "Yes"
        
        # Explore all possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new position is within bounds and not an obstacle
            if 1 <= nx <= H and 1 <= ny <= W and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return "No"

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

H, W, K = map(int, data[0].split())
obstacles = [tuple(map(int, line.split())) for line in data[1:K + 1]]

# Output the result
print(can_reach_destination(H, W, K, obstacles))