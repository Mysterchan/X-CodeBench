def read_input():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    H, W, K = map(int, data[0].split())
    obstacles = set()
    for i in range(1, K + 1):
        r, c = map(int, data[i].split())
        obstacles.add((r - 1, c - 1))  # Store as 0-indexed
    return H, W, obstacles

def can_reach(H, W, obstacles):
    from collections import deque

    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # BFS Initialization
    queue = deque([(0, 0)])  # Start from (0, 0)
    visited = set()
    visited.add((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        # Check if we reached the bottom-right corner
        if x == H - 1 and y == W - 1:
            return True
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in obstacles and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return False

H, W, obstacles = read_input()
result = can_reach(H, W, obstacles)
print("Yes" if result else "No")