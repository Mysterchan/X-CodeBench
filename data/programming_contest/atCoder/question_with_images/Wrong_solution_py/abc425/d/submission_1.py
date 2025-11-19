from collections import deque
from itertools import product

def is_correct_idx(u, H, W):
    return 0 <= u[0] < H and 0 <= u[1] < W

def possible(x, y, S):
    if S[x][y] != ".":
        return False

    H, W = len(S), len(S[0])
    dxdy_combs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    cnt = 0
    for dx, dy in dxdy_combs:
        nx, ny = x + dx, y + dy
        v = (nx, ny)
        if not is_correct_idx(v, H, W):
            continue
        if S[nx][ny] == "#":
            cnt += 1
        if cnt > 1:
            return False
    return True

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    Q = deque()
    calculated = [[0] * W for _ in range(H)]

    res = 0
    for x, y in product(range(H), range(W)):
        if S[x][y] == "#":
            first_flg = True
            u = (x, y, first_flg)
            Q.append(u)

    dxdy_combs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    while len(Q) >= 1:
        x, y, first_flg = Q.popleft()
        calculated_now = calculated[x][y]
        calculated[x][y] = 1
        if calculated_now == 1:
            continue
        if not (first_flg or possible(x, y, S)):
            continue
        S[x][y] = "#"
        res += 1
        calculated[x][y] = 1

        for dx, dy in dxdy_combs:
            nx, ny = x + dx, y + dy
            v = (nx, ny, False)
            if not is_correct_idx(v, H, W):
                continue
            Q.append(v)

    print(res)

if __name__ == "__main__":
    main()