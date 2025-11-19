import sys
from collections import deque

def main():
    input = sys.stdin.readline
    H, W, K = map(int, input().split())
    blocked = set()
    for _ in range(K):
        r, c = map(int, input().split())
        blocked.add((r, c))

    # 特殊情况：起点即终点
    if H == 1 and W == 1:
        print("Yes")
        return

    # BFS
    visited = set()
    queue = deque()
    start = (1, 1)
    goal = (H, W)
    if start in blocked or goal in blocked:
        print("No")
        return

    queue.append(start)
    visited.add(start)

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        i, j = queue.popleft()
        if (i, j) == goal:
            print("Yes")
            return
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 1 <= ni <= H and 1 <= nj <= W and (ni, nj) not in blocked and (ni, nj) not in visited:
                visited.add((ni, nj))
                queue.append((ni, nj))

    print("No")

if __name__ == "__main__":
    main()