def max_xor_score(H, W, grid):
    from itertools import product

    # Total number of cells
    total_cells = H * W
    max_score = 0

    # Iterate through all possible placements of dominoes
    for mask in range(1 << total_cells):
        covered = set()
        current_xor = 0

        for i in range(H):
            for j in range(W):
                index = i * W + j
                if mask & (1 << index):  # If this cell is covered
                    covered.add((i, j))
                    # Check if we can cover right or down
                    if j + 1 < W and (mask & (1 << (i * W + (j + 1)))):  # Right
                        continue
                    if i + 1 < H and (mask & (1 << ((i + 1) * W + j))):  # Down
                        continue

        # Calculate the XOR of uncovered cells
        for i in range(H):
            for j in range(W):
                if (i, j) not in covered:
                    current_xor ^= grid[i][j]

        max_score = max(max_score, current_xor)

    return max_score

# Read input
H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

# Get the result and print it
result = max_xor_score(H, W, grid)
print(result)