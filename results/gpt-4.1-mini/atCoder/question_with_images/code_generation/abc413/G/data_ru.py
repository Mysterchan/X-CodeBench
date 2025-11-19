import sys
from collections import deque

def main():
    input = sys.stdin.readline
    H, W, K = map(int, input().split())
    obstacles = set()
    for _ in range(K):
        r, c = map(int, input().split())
        obstacles.add((r, c))

    # Если старт или финиш заблокированы (по условию не может быть, но на всякий случай)
    if (1,1) in obstacles or (H,W) in obstacles:
        print("No")
        return

    # Если старт == финиш
    if H == 1 and W == 1:
        print("Yes")
        return

    visited = set()
    visited.add((1,1))
    queue = deque()
    queue.append((1,1))

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        i,j = queue.popleft()
        if (i,j) == (H,W):
            print("Yes")
            return
        for di,dj in directions:
            ni, nj = i+di, j+dj
            if 1 <= ni <= H and 1 <= nj <= W:
                if (ni,nj) not in obstacles and (ni,nj) not in visited:
                    visited.add((ni,nj))
                    queue.append((ni,nj))

    print("No")

if __name__ == "__main__":
    main()