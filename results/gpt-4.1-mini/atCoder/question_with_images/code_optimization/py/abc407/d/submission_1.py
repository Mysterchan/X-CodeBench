import sys
read = sys.stdin.read
from operator import xor
from functools import reduce

def main():
    input_data = read().strip().split()
    h, w = map(int, input_data[:2])
    A = list(map(int, input_data[2:]))

    n = h * w
    allxor = reduce(xor, A)
    ans = allxor

    # Precompute neighbors for each cell (right and down)
    neighbors = []
    for i in range(h):
        for j in range(w):
            idx = i * w + j
            if j + 1 < w:
                neighbors.append((idx, idx + 1))
            if i + 1 < h:
                neighbors.append((idx, idx + w))

    # Use bitmask dp to represent which cells are covered
    # dp[mask] = maximum xor of covered cells' values (xor of all covered cells)
    # We want to maximize allxor ^ dp[mask]
    # Since HW <= 20, dp size = 2^20 = ~1 million, feasible with pruning

    from collections import deque

    dp = dict()
    dp[0] = 0
    queue = deque([0])

    while queue:
        mask = queue.popleft()
        val = dp[mask]
        # Find first uncovered cell
        # To speed up, we can try all edges and add if both uncovered
        for u, v in neighbors:
            if (mask & (1 << u)) == 0 and (mask & (1 << v)) == 0:
                nmask = mask | (1 << u) | (1 << v)
                nval = val ^ A[u] ^ A[v]
                if nmask not in dp or dp[nmask] < nval:
                    dp[nmask] = nval
                    queue.append(nmask)

    for val in dp.values():
        score = allxor ^ val
        if score > ans:
            ans = score

    print(ans)

if __name__ == '__main__':
    main()