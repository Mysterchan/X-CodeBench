import sys
from collections import deque

def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]

    # Directions: up, down, left, right
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    # Count black neighbors for each cell
    black_neighbors = [[0]*W for _ in range(H)]

    # Initialize black cells queue
    queue = deque()

    # First, count black neighbors for each white cell
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                # For black cells, update neighbors' black count
                for dx, dy in directions:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '.':
                        black_neighbors[ni][nj] += 1

    # Initialize queue with white cells that have exactly one black neighbor
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.' and black_neighbors[i][j] == 1:
                queue.append((i,j))

    # BFS-like process to simulate the 10^100 steps (which is effectively until no change)
    while queue:
        i, j = queue.popleft()
        if grid[i][j] == '#':
            continue
        # Paint this cell black
        grid[i][j] = '#'
        # Update neighbors
        for dx, dy in directions:
            ni, nj = i+dx, j+dy
            if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '.':
                black_neighbors[ni][nj] += 1
                # If now exactly one black neighbor, add to queue
                if black_neighbors[ni][nj] == 1:
                    queue.append((ni,nj))

    # Count black cells
    result = sum(row.count('#') for row in grid)
    print(result)

if __name__ == "__main__":
    main()