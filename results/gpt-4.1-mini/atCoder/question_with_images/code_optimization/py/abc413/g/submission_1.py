import sys
from collections import deque

def main():
    input = sys.stdin.readline
    H, W, K = map(int, input().split())
    obstacles = set()
    for _ in range(K):
        r, c = map(int, input().split())
        obstacles.add((r - 1, c - 1))

    # If start or goal is blocked (problem states they are not, but just in case)
    if (0, 0) in obstacles or (H - 1, W - 1) in obstacles:
        print("No")
        return

    # BFS from (0,0) to (H-1,W-1)
    visited = set()
    visited.add((0, 0))
    queue = deque([(0, 0)])

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        x, y = queue.popleft()
        if x == H - 1 and y == W - 1:
            print("Yes")
            return
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in obstacles and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    print("No")

if __name__ == "__main__":
    main()