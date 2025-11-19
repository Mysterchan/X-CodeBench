def count_arrangements(T, cases):
    MOD = 998244353
    results = []
    
    for case in cases:
        H, W, grid = case
        a_count = sum(row.count('A') for row in grid)
        b_count = sum(row.count('B') for row in grid)

        # Check for conditions
        valid = True
        
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 'A':
                    # Check right and down conditions
                    if (grid[i][(j + 1) % W] == 'B' and grid[(i + 1) % H][j] == 'B'):
                        continue
                    if (grid[i][(j + 1) % W] == 'A' and grid[(i + 1) % H][j] == 'A'):
                        continue
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            arrangements = pow(4, a_count, MOD) * pow(2, b_count, MOD) % MOD
        else:
            arrangements = 0
        
        results.append(arrangements)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
cases = []
index = 1

for _ in range(T):
    H, W = map(int, data[index].split())
    grid = data[index + 1:index + 1 + H]
    cases.append((H, W, grid))
    index += H + 1

# Get results
results = count_arrangements(T, cases)

# Output results
sys.stdout.write('\n'.join(map(str, results)) + '\n')