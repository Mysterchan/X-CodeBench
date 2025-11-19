import sys
from collections import deque

def solve() -> None:
    input = sys.stdin.read
    data = input().split()
    idx = 0
    H = int(data[idx])
    W = int(data[idx + 1])
    idx += 2
    
    heights = []
    for i in range(H):
        heights.append(list(map(int, data[idx:idx + W])))
        idx += W
    
    Q = int(data[idx])
    idx += 1
    
    queries = []
    for _ in range(Q):
        A = int(data[idx]) - 1
        B = int(data[idx + 1]) - 1
        Y = int(data[idx + 2])
        C = int(data[idx + 3]) - 1
        D = int(data[idx + 4]) - 1
        Z = int(data[idx + 5])
        queries.append((A, B, Y, C, D, Z))
        idx += 6
    
    # Directions for adjacent blocks
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    results = []
    
    for A, B, Y, C, D, Z in queries:
        if (A, B) == (C, D):
            results.append(abs(Y - Z))
            continue
        
        # BFS to find the minimum stairs used
        queue = deque()
        visited = set()
        
        # Start from (A, B) at floor Y
        queue.append((A, B, Y, 0))  # (row, col, current_floor, stairs_used)
        visited.add((A, B, Y))
        
        min_stairs = float('inf')
        
        while queue:
            r, c, floor, stairs_used = queue.popleft()
            
            # Check if we reached the destination
            if (r, c) == (C, D):
                min_stairs = min(min_stairs, stairs_used + abs(floor - Z))
                continue
            
            # Move within the same building
            if floor > 1:
                if (r, c, floor - 1) not in visited:
                    visited.add((r, c, floor - 1))
                    queue.append((r, c, floor - 1, stairs_used + 1))
            if floor < heights[r][c]:
                if (r, c, floor + 1) not in visited:
                    visited.add((r, c, floor + 1))
                    queue.append((r, c, floor + 1, stairs_used + 1))
            
            # Move to adjacent buildings
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    if floor <= heights[nr][nc]:
                        if (nr, nc, floor) not in visited:
                            visited.add((nr, nc, floor))
                            queue.append((nr, nc, floor, stairs_used))
        
        results.append(min_stairs)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()