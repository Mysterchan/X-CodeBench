from collections import deque

def can_reach_destination(H, W, obstacles):
    grid = [[0] * (W + 1) for _ in range(H + 1)]
    
    for r, c in obstacles:
        grid[r][c] = 1  # Mark obstacle
    
    # BFS initialization
    queue = deque([(1, 1)])
    visited = set((1, 1))
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (H, W):
            return "Yes"
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 1 <= nx <= H and 1 <= ny <= W and (nx, ny) not in visited and grid[nx][ny] == 0:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return "No"

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

H, W, K = map(int, data[0].split())
obstacles = [tuple(map(int, line.split())) for line in data[1:K + 1]]

# Output the result
print(can_reach_destination(H, W, obstacles))