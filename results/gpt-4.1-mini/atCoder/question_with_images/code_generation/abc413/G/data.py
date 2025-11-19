import sys
from collections import deque

def main():
    input = sys.stdin.readline
    H, W, K = map(int, input().split())
    obstacles = set()
    for _ in range(K):
        r, c = map(int, input().split())
        obstacles.add((r, c))

    # If start == goal and no obstacles on start or goal, answer is Yes
    if H == 1 and W == 1:
        print("Yes")
        return

    # BFS from (1,1) to (H,W)
    start = (1, 1)
    goal = (H, W)
    visited = set()
    visited.add(start)
    queue = deque([start])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        i, j = queue.popleft()
        if (i, j) == goal:
            print("Yes")
            return
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 1 <= ni <= H and 1 <= nj <= W and (ni, nj) not in obstacles and (ni, nj) not in visited:
                visited.add((ni, nj))
                queue.append((ni, nj))

    print("No")

if __name__ == "__main__":
    main()