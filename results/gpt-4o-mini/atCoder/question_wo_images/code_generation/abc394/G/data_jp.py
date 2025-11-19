def min_stairs(H, W, F, queries):
    # Precompute distances between all pairs of (i, j) coordinates using BFS
    from collections import deque
    
    # Distances will store the minimum number of stairs used to reach each building at each level
    distances = [[[float('inf')] * (10**6 + 1) for _ in range(W)] for _ in range(H)]
    
    # BFS for each building
    for i in range(H):
        for j in range(W):
            # Initialize the BFS queue and setup for this building
            queue = deque()
            for x in range(1, F[i][j] + 1):
                distances[i][j][x] = 0
                queue.append((i, j, x))
                
            while queue:
                ci, cj, cx = queue.popleft()
                
                # Move vertically within the same building
                if cx > 1 and distances[ci][cj][cx - 1] > distances[ci][cj][cx] + 1:
                    distances[ci][cj][cx - 1] = distances[ci][cj][cx] + 1
                    queue.append((ci, cj, cx - 1))
                if cx < F[ci][cj] and distances[ci][cj][cx + 1] > distances[ci][cj][cx] + 1:
                    distances[ci][cj][cx + 1] = distances[ci][cj][cx] + 1
                    queue.append((ci, cj, cx + 1))
                
                # Move to adjacent buildings
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < H and 0 <= nj < W:
                        # Can move to a building if it's tall enough
                        for nx in range(1, F[ni][nj] + 1):
                            if distances[ni][nj][nx] > distances[ci][cj][cx]:
                                distances[ni][nj][nx] = distances[ci][cj][cx]
                                queue.append((ni, nj, nx))
    
    result = []
    
    for A, B, Y, C, D, Z in queries:
        A, B, C, D = A - 1, B - 1, C - 1, D - 1  # Convert to 0-indexed
        min_stairs_needed = min(distances[A][B][Y] + abs(Y - Z) for Y in range(1, F[A][B] + 1) if F[C][D] >= Y)
        result.append(min_stairs_needed)
    
    return result


# Input reading
import sys
input = sys.stdin.read

data = input().splitlines()
H, W = map(int, data[0].split())
F = [list(map(int, data[i + 1].split())) for i in range(H)]
Q = int(data[H + 1])
queries = [list(map(int, data[i + H + 2].split())) for i in range(Q)]

# Get results from the function
results = min_stairs(H, W, F, queries)

# Output results
sys.stdout.write('\n'.join(map(str, results)) + '\n')