def count_valid_arrangements(H, W, grid):
    MOD = 998244353
    
    # Count the number of A and B tiles
    a_count = 0
    b_count = 0
    
    for row in grid:
        a_count += row.count('A')
        b_count += row.count('B')
    
    # Check for the conditions of valid arrangements
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'A':
                # Check right neighbor
                if grid[i][(j + 1) % W] == 'B':
                    return 0
                # Check bottom neighbor
                if grid[(i + 1) % H][j] == 'B':
                    return 0
    
    # Calculate the number of valid arrangements
    arrangements = pow(4, a_count, MOD) * pow(2, b_count, MOD) % MOD
    return arrangements

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
results = []
index = 1

for _ in range(T):
    H, W = map(int, data[index].split())
    grid = data[index + 1:index + 1 + H]
    index += 1 + H
    result = count_valid_arrangements(H, W, grid)
    results.append(result)

print("\n".join(map(str, results)))