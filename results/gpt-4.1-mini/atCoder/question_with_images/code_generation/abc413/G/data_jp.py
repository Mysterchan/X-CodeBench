import sys
from collections import deque

def main():
    input = sys.stdin.readline
    H, W, K = map(int, input().split())
    blocked = set()
    for _ in range(K):
        r, c = map(int, input().split())
        blocked.add((r, c))

    # BFS from (1,1) to (H,W)
    start = (1, 1)
    goal = (H, W)
    if start == goal:
        print("Yes")
        return

    visited = set()
    visited.add(start)
    queue = deque([start])

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        i, j = queue.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 1 <= ni <= H and 1 <= nj <= W:
                if (ni, nj) not in blocked and (ni, nj) not in visited:
                    if (ni, nj) == goal:
                        print("Yes")
                        return
                    visited.add((ni, nj))
                    queue.append((ni, nj))
    print("No")

if __name__ == "__main__":
    main()