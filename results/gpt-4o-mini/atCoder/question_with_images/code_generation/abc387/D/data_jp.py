from collections import deque

def min_moves_to_goal(H, W, grid):
    start = None
    goal = None
    
    # Locate S and G positions
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)
    
    # Directions for movement: up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # BFS setup
    queue = deque([(start[0], start[1], 0, 0)])  # (row, col, moves, parity)
    visited = set()  # Visited state considering parity
    visited.add((start[0], start[1], 0))

    while queue:
        i, j, moves, parity = queue.popleft()

        # Increment move count
        if (i, j) == goal:
            return moves
        
        # Next parity
        next_parity = 1 - parity

        # Explore neighbors
        for d in directions:
            ni, nj = i + d[0], j + d[1]

            if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] != '#':
                if moves % 2 == 0:  # Even move: horizontal
                    if d[0] == 0:  # Move horizontally
                        if (ni, nj, next_parity) not in visited:
                            visited.add((ni, nj, next_parity))
                            queue.append((ni, nj, moves + 1, next_parity))
                else:  # Odd move: vertical
                    if d[1] == 0:  # Move vertically
                        if (ni, nj, next_parity) not in visited:
                            visited.add((ni, nj, next_parity))
                            queue.append((ni, nj, moves + 1, next_parity))

    return -1

# Input reading
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# Output the result
print(min_moves_to_goal(H, W, grid))