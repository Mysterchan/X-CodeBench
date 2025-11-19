def max_xor_score(H, W, grid):
    from itertools import product

    # Total number of cells
    total_cells = H * W
    max_score = 0

    # Iterate through all possible combinations of cells to leave uncovered
    for mask in range(1 << total_cells):
        uncovered_xor = 0
        valid = True
        
        # Check which cells are uncovered based on the mask
        covered = [[False] * W for _ in range(H)]
        for i in range(total_cells):
            if mask & (1 << i):
                row = i // W
                col = i % W
                uncovered_xor ^= grid[row][col]
            else:
                # Mark the cell as covered
                if row > 0 and covered[row - 1][col]:  # Check above
                    valid = False
                if col > 0 and covered[row][col - 1]:  # Check left
                    valid = False
                covered[row][col] = True

        if valid:
            max_score = max(max_score, uncovered_xor)

    return max_score

# Input reading
import sys
input = sys.stdin.read
data = input().split()
H = int(data[0])
W = int(data[1])
grid = []

index = 2
for _ in range(H):
    row = list(map(int, data[index:index + W]))
    grid.append(row)
    index += W

# Calculate and print the result
result = max_xor_score(H, W, grid)
print(result)