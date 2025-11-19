import sys
import threading
from collections import defaultdict
def main():
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline
    (H, W) = map(int, input().split())
    Hgrid = []
    for _ in range(H):
        row = list(map(int, input().split()))
        Hgrid.append(row)
    N = H * W
    flat_h = [0] * N
    for i in range(H):
        base = i * W
        for j in range(W):
            flat_h[base + j] = Hgrid[i][j]
    neighbours = [[] for _ in range(N)]
    for i in range(H):
        for j in range(W):
            idx = i * W + j
            if i > 0:
                neighbours[idx].append((i - 1) * W + j)
            if i + 1 < H:
                neighbours[idx].append((i + 1) * W + j)
            if j > 0:
                neighbours[idx].append(idx - 1)
            if j + 1 < W:
                neighbours[idx].append(idx + 1)
    Q = int(input())
    A = [0] * Q
    B = [0] * Q
    C = [0] * Q
    D = [0] * Q
    Y = [0] * Q
    Z = [0] * Q
    for i in range(Q):
        (a, b, y, c, d, z) = map(int, input().split())
        A[i] = a - 1
        B[i] = b - 1
        C[i] = c - 1
        D[i] = d - 1
        Y[i] = y
        Z[i] = z
    SHIFT_V1 = 0
    SHIFT_V2 = 19
    SHIFT_A = 19 + 19
    SHIFT_B = SHIFT_A + 20
    SHIFT_Q = SHIFT_B + 20
    SHIFT_PI = SHIFT_Q + 20
    sub_by_b = defaultdict(list)
    for qid in range(Q):
        s = A[qid] * W + B[qid]
        t = C[qid] * W + D[qid]
        for v in neighbours[s]:
            a_val = flat_h[s] if flat_h[s] < flat_h[v] else flat_h[v]
            for w in neighbours[t]:
                b_val = flat_h[t] if flat_h[t] < flat_h[w] else flat_h[w]
                if b_val <= a_val:
                    v1 = v
                    v2 = w
                    packed = v1 << SHIFT_V1 | v2 << SHIFT_V2 | a_val << SHIFT_A | b_val << SHIFT_B | qid << SHIFT_Q | 0
                    sub_by_b[b_val].append(packed)
    cells = [(flat_h[i], i) for i in range(N)]
    cells.sort(reverse=True)
    neigh_flat = []
    for idx in range(N):
        neigh_flat.append([v for v in neighbours[idx]])
    parent = list(range(N))
    size = [1] * N
    active = [False] * N

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] < size[y]:
            (x, y) = (y, x)
        parent[y] = x
        size[x] += size[y]
    thresholds = sorted(sub_by_b.keys(), reverse=True)
    ans = [10 ** 18] * Q
    p = 0
    total_cells = len(cells)
    for h in thresholds:
        while p < total_cells and cells[p][0] >= h:
            idx = cells[p][1]
            active[idx] = True
            for nb in neigh_flat[idx]:
                if active[nb]:
                    union(idx, nb)
            p += 1
        for packed in sub_by_b[h]:
            v1 = packed >> SHIFT_V1 & (1 << 19) - 1
            v2 = packed >> SHIFT_V2 & (1 << 19) - 1
            a_val = packed >> SHIFT_A & (1 << 20) - 1
            b_val = packed >> SHIFT_B & (1 << 20) - 1
            qid = packed >> SHIFT_Q & (1 << 20) - 1
            if find(v1) == find(v2):
                cost = a_val - b_val + abs(Y[qid] - a_val) + abs(b_val - Z[qid])
                if cost < ans[qid]:
                    ans[qid] = cost
    out = '\n'.join((str(v) for v in ans))
    sys.stdout.write(out)
if __name__ == '__main__':
    threading.Thread(target=main).start()