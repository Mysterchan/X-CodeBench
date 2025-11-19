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

    calculated = [[False] * W for _ in range(H)]

    T = set()
    res = 0
    for x, y in product(range(H), range(W)):
        if S[x][y] == "#":
            T.add((x, y))
            calculated[x][y] = True
            res += 1

    dxdy_combs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    while len(T) > 0:
        nT = set()
        for x, y in T:
            for dx, dy in dxdy_combs:
                nx, ny = x + dx, y + dy
                v = (nx, ny)
                if not is_correct_idx(v, H, W):
                    continue
                if calculated[nx][ny]:
                    continue
                calculated[nx][ny] = True
                if possible(nx, ny, S):
                    res += 1
                    nT.add(v)
        for x, y in nT:
            S[x][y] = "#"
        T = nT
    print(res)

if __name__ == "__main__":
    main()