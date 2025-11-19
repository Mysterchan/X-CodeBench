def max_domino_xor(H, W, grid):
    from itertools import product

    # Total number of cells
    total_cells = H * W

    # Generate all possible placements of dominoes
    max_score = 0
    for mask in range(1 << total_cells):
        covered = [[False] * W for _ in range(H)]
        score = 0
        valid = True
        
        for i in range(H):
            for j in range(W):
                index = i * W + j
                if (mask & (1 << index)) == 0:  # Cell is not covered
                    score ^= grid[i][j]
                else:
                    # Check if we can place a domino
                    if j < W - 1 and (mask & (1 << (index + 1))) == 0:  # Horizontal domino
                        covered[i][j] = True
                        covered[i][j + 1] = True
                    elif i < H - 1 and (mask & (1 << (index + W))) == 0:  # Vertical domino
                        covered[i][j] = True
                        covered[i + 1][j] = True
                    else:
                        valid = False
                        break
            if not valid:
                break
        
        if valid:
            max_score = max(max_score, score)

    return max_score

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

# Get the result and print it
result = max_domino_xor(H, W, grid)
print(result)