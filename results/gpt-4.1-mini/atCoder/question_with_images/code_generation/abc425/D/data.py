import sys
from collections import deque

def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]

    # Directions: up, down, left, right
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    # Count black neighbors for each white cell
    black_neighbors = [[0]*W for _ in range(H)]

    # Initialize queue with white cells that have exactly one black neighbor
    queue = deque()

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                count = 0
                for dx, dy in directions:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '#':
                        count += 1
                black_neighbors[i][j] = count
                if count == 1:
                    queue.append((i,j))

    # BFS-like process to color white cells black if they have exactly one black neighbor
    while queue:
        i, j = queue.popleft()
        if grid[i][j] == '#':
            continue
        # Color this cell black
        grid[i][j] = '#'
        # Update neighbors
        for dx, dy in directions:
            ni, nj = i+dx, j+dy
            if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '.':
                black_neighbors[ni][nj] += 1
                if black_neighbors[ni][nj] == 1:
                    queue.append((ni,nj))

    # Count black cells
    result = sum(row.count('#') for row in grid)
    print(result)

if __name__ == "__main__":
    main()