import sys
input = sys.stdin.read

def solve():
    data = input().split()
    H = int(data[0])
    W = int(data[1])
    grid = []
    for i in range(H):
        row = data[i+2]
        grid.append([int(c) for c in row])

    min_total = float('inf')

    for flip_pattern in range(1 << W):
        col_flips = [int((flip_pattern >> j) & 1) for j in range(W)]

        total = 0

        for row in grid:

            cost_no_flip = sum(1 - (row[j] ^ col_flips[j]) for j in range(W))

            cost_with_flip = sum(1 - ((1 - row[j]) ^ col_flips[j]) for j in range(W))

            total += min(cost_no_flip, cost_with_flip)

        min_total = min(min_total, total)

    print(min_total)

solve()