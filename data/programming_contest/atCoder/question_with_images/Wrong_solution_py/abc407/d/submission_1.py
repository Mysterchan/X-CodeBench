import random
from time import time

def main():
    H, W = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    total_score = 0
    for row in grid:
        for val in row:
            total_score ^= val

    putturns = []
    for i in range(H):
        for j in range(W):
            if i+1 < H:
                putturns.append(((i,j), (i+1,j)))
            if j+1 < W:
                putturns.append(((i,j), (i,j+1)))

    putted = []
    putted_set = set()
    used_cells = set()
    used_dominos = set()

    current_score = total_score
    best_score = current_score

    start = time()
    loops = 0
    ok = 90

    if H == W == 1:
        exit(print(1))

    while time() - start < 1.9225:
        if random.randint(0,1):
            d = random.choice(putturns)
            a, b = d
            if d not in used_dominos and a not in used_cells and b not in used_cells:
                used_dominos.add(d)
                used_cells.add(a)
                used_cells.add(b)
                putted.append(d)
                current_score ^= grid[a[0]][a[1]]
                current_score ^= grid[b[0]][b[1]]

        else:
            if putted:
                idx = random.randint(0, len(putted) - 1)
                d = putted.pop(idx)
                a, b = d
                used_dominos.remove(d)
                used_cells.remove(a)
                used_cells.remove(b)
                current_score ^= grid[a[0]][a[1]]
                current_score ^= grid[b[0]][b[1]]

        if current_score > best_score or random.random() * 100 < ok:
            best_score = current_score

        ok *= 0.9994

    print(best_score)

if __name__ == '__main__':
    main()