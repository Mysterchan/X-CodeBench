import sys
from collections import deque

input = sys.stdin.read
data = input().split()
index = 0

H = int(data[index])
W = int(data[index + 1])
index += 2

F = []
for i in range(H):
    F.append(list(map(int, data[index:index + W])))
    index += W

Q = int(data[index])
index += 1

queries = []
for _ in range(Q):
    A = int(data[index]) - 1
    B = int(data[index + 1]) - 1
    Y = int(data[index + 2])
    C = int(data[index + 3]) - 1
    D = int(data[index + 4]) - 1
    Z = int(data[index + 5])
    queries.append((A, B, Y, C, D, Z))
    index += 6

# Directions for adjacency (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start_floor, start_i, start_j):
    queue = deque([(start_i, start_j, start_floor, 0)])  # (i, j, current_floor, stair_count)
    visited = set()
    visited.add((start_i, start_j, start_floor))
    
    distances = {}
    
    while queue:
        i, j, current_floor, stair_count = queue.popleft()
        
        # Save the minimum stair usage to reach this position and floor
        if (i, j) not in distances:
            distances[(i, j)] = {}
        if current_floor not in distances[(i, j)]:
            distances[(i, j)][current_floor] = stair_count
            
        # If there are already fewer stairs used to reach this state, skip
        elif distances[(i, j)][current_floor] <= stair_count:
            continue
        
        # Move up and down in the same building
        if current_floor < F[i][j]:
            if (i, j, current_floor + 1) not in visited:
                visited.add((i, j, current_floor + 1))
                queue.append((i, j, current_floor + 1, stair_count + 1))
        
        if current_floor > 1:
            if (i, j, current_floor - 1) not in visited:
                visited.add((i, j, current_floor - 1))
                queue.append((i, j, current_floor - 1, stair_count + 1))
        
        # Move to adjacent blocks
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and current_floor <= F[ni][nj]:
                if (ni, nj, current_floor) not in visited:
                    visited.add((ni, nj, current_floor))
                    queue.append((ni, nj, current_floor, stair_count))
    
    return distances

results = []
for A, B, Y, C, D, Z in queries:
    distance_map = bfs(Y, A, B)
    
    # Find the minimum stairs used to reach (C, D, Z)
    if (C, D) in distance_map:
        min_stairs = float('inf')
        for floor in distance_map[(C, D)]:
            stairs_used = distance_map[(C, D)][floor] + abs(Y - floor) + abs(Z - floor)
            min_stairs = min(min_stairs, stairs_used)
        results.append(min_stairs)
    else:
        results.append(-1)

sys.stdout.write('\n'.join(map(str, results)) + '\n')