import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

H, W = map(int, data[0].split())
F = [list(map(int, line.split())) for line in data[1:H + 1]]
Q = int(data[H + 1])
queries = [list(map(int, line.split())) for line in data[H + 2:H + 2 + Q]]

# Directions for moving to adjacent blocks
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(start_floor, start_x, start_y, target_x, target_y, target_floor):
    # BFS to find the minimum number of stairs used
    queue = deque([(start_x, start_y, start_floor, 0)])  # (x, y, current_floor, stairs_used)
    visited = set()
    visited.add((start_x, start_y, start_floor))
    
    while queue:
        x, y, current_floor, stairs_used = queue.popleft()
        
        # If we reach the target building and floor
        if x == target_x and y == target_y:
            if current_floor == target_floor:
                return stairs_used
            else:
                stairs_used += abs(current_floor - target_floor)
                return stairs_used
        
        # Move within the same building
        if current_floor < F[x][y]:
            if (x, y, current_floor + 1) not in visited:
                visited.add((x, y, current_floor + 1))
                queue.append((x, y, current_floor + 1, stairs_used + 1))
        
        if current_floor > 1:
            if (x, y, current_floor - 1) not in visited:
                visited.add((x, y, current_floor - 1))
                queue.append((x, y, current_floor - 1, stairs_used + 1))
        
        # Move to adjacent buildings
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W:
                if F[nx][ny] >= current_floor and (nx, ny, current_floor) not in visited:
                    visited.add((nx, ny, current_floor))
                    queue.append((nx, ny, current_floor, stairs_used))
    
    return float('inf')  # If not reachable

results = []
for A, B, Y, C, D, Z in queries:
    A -= 1
    B -= 1
    C -= 1
    D -= 1
    result = bfs(Y, A, B, C, D, Z)
    results.append(result)

print('\n'.join(map(str, results)))