from sys import stdin, stdout
from collections import deque

def min_stair_moves(H, W, F, Q, queries):
    # Directions for cardinal movement (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Prepare results
    results = []
    
    # We need to process each query
    for a, b, y, c, d, z in queries:
        a -= 1  # Adjust to 0-indexed
        b -= 1
        c -= 1
        d -= 1
        
        # BFS or Dijkstra-like approach for minimum stair usage
        queue = deque()
        visited = set()
        
        # Initialize with the current position in the building (a, b) at floor y
        queue.append((a, b, y))
        visited.add((a, b, y))
        
        min_stairs = float('inf')
        
        while queue:
            x, y, curr_floor = queue.popleft()
            
            # If we reached the destination building at the desired floor
            if x == c and y == d:
                min_stairs = min(min_stairs, abs(curr_floor - z))
                continue
            
            # Move within the same building
            if curr_floor < F[x][y]:
                if (x, y, curr_floor + 1) not in visited:
                    visited.add((x, y, curr_floor + 1))
                    queue.append((x, y, curr_floor + 1))
            if curr_floor > 1:
                if (x, y, curr_floor - 1) not in visited:
                    visited.add((x, y, curr_floor - 1))
                    queue.append((x, y, curr_floor - 1))
            
            # Move to adjacent buildings with walkways
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < H and 0 <= ny < W:
                    if F[nx][ny] >= curr_floor:  # Can walk to this floor
                        if (nx, ny, curr_floor) not in visited:
                            visited.add((nx, ny, curr_floor))
                            queue.append((nx, ny, curr_floor))
        
        results.append(min_stairs)
    
    return results

def main():
    # Read input
    input = stdin.read
    data = input().split()
    
    index = 0
    H = int(data[index])
    W = int(data[index + 1])
    index += 2
    
    F = []
    for i in range(H):
        F.append([int(data[index + j]) for j in range(W)])
        index += W
    
    Q = int(data[index])
    index += 1
    
    queries = []
    for i in range(Q):
        A = int(data[index])
        B = int(data[index + 1])
        Y = int(data[index + 2])
        C = int(data[index + 3])
        D = int(data[index + 4])
        Z = int(data[index + 5])
        queries.append((A, B, Y, C, D, Z))
        index += 6
    
    result = min_stair_moves(H, W, F, Q, queries)
    stdout.write("\n".join(map(str, result)) + "\n")

main()