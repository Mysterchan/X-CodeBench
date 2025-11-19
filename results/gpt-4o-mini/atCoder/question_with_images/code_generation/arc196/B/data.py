def count_tiling_ways(test_cases):
    MOD = 998244353
    
    results = []
    
    for case in test_cases:
        H, W = case['H'], case['W']
        grid = case['grid']
        
        # Count A and B types
        count_A = sum(row.count('A') for row in grid)
        count_B = sum(row.count('B') for row in grid)

        # Check for each row, if it fails the conditions
        valid = True

        # Check rows for condition:
        for i in range(H):
            left_segments = sum(1 for j in range(W) if grid[i][j] == 'A')
            right_segments = sum(1 for j in range(W) if grid[i][(j+1) % W] == 'A')
            if (left_segments % 2) != (right_segments % 2):
                valid = False
                break
        
        # Check columns for condition:
        if valid:
            for j in range(W):
                top_segments = sum(1 for i in range(H) if grid[i][j] == 'A')
                bottom_segments = sum(1 for i in range(H) if grid[(i+1) % H][j] == 'A')
                if (top_segments % 2) != (bottom_segments % 2):
                    valid = False
                    break
        
        if valid:
            # Calculate number of ways
            ways = pow(4, count_A, MOD) * pow(2, count_B, MOD) % MOD
            results.append(ways)
        else:
            results.append(0)
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
index = 1
test_cases = []

for _ in range(T):
    H, W = map(int, data[index].split())
    index += 1
    grid = []
    for _ in range(H):
        grid.append(data[index])
        index += 1
    test_cases.append({'H': H, 'W': W, 'grid': grid})

results = count_tiling_ways(test_cases)

# Output the results
sys.stdout.write('\n'.join(map(str, results)) + '\n')