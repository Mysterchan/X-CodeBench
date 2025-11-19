def max_xor(H, W, grid):
    from itertools import product

    # Generate all possible states of the grid (0: not covered, 1: covered)
    max_xor_value = 0
    total_cells = H * W

    # Iterate through all possible combinations of covered cells
    for mask in range(1 << total_cells):
        covered = [[False] * W for _ in range(H)]
        current_xor = 0
        valid = True

        for i in range(H):
            for j in range(W):
                index = i * W + j
                if mask & (1 << index):  # If this cell is covered
                    covered[i][j] = True
                    # Check if we can place a domino
                    if j < W - 1 and not covered[i][j + 1]:  # Horizontal domino
                        covered[i][j + 1] = True
                    elif i < H - 1 and not covered[i + 1][j]:  # Vertical domino
                        covered[i + 1][j] = True
                    else:
                        valid = False
                        break
                else:  # If this cell is not covered
                    current_xor ^= grid[i][j]

            if not valid:
                break

        if valid:
            max_xor_value = max(max_xor_value, current_xor)

    return max_xor_value

# Read input
import sys
input = sys.stdin.read
data = input().split()

H = int(data[0])
W = int(data[1])
grid = []

index = 2
for i in range(H):
    row = list(map(int, data[index:index + W]))
    grid.append(row)
    index += W

# Calculate and print the result
result = max_xor(H, W, grid)
print(result)