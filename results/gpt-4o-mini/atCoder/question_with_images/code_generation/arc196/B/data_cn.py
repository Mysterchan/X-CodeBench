def count_arrangements(H, W, grid):
    MOD = 998244353
    count_A = count_B = 0
    
    # Count type A and B tiles
    for row in grid:
        count_A += row.count('A')
        count_B += row.count('B')
    
    # Check for conflicts
    valid = True
    for i in range(H):
        for j in range(W):
            # We need to check (i, j) and (i, (j + 1) % W) for condition 1
            # and (i, j) and ((i + 1) % H, j) for condition 2
            current_a = grid[i][j] == 'A'
            current_b = grid[i][j] == 'B'
            right_a = grid[i][(j + 1) % W] == 'A'
            right_b = grid[i][(j + 1) % W] == 'B'
            down_a = grid[i][j] == 'A'
            down_b = grid[i][j] == 'B'
            next_row_a = grid[(i + 1) % H][j] == 'A'
            next_row_b = grid[(i + 1) % H][j] == 'B'
            
            # Check condition 1
            if current_a ^ right_a:
                valid = False
                break

            # Check condition 2
            if down_a ^ next_row_a:
                valid = False
                break
        if not valid:
            break
    
    if not valid:
        return 0
    
    # Calculate number of arrangements
    arrangements = (pow(4, count_A, MOD) * pow(2, count_B, MOD)) % MOD
    return arrangements

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    idx = 1

    for _ in range(T):
        H, W = map(int, data[idx].split())
        idx += 1
        grid = data[idx:idx + H]
        idx += H

        result = count_arrangements(H, W, grid)
        results.append(result)

    sys.stdout.write('\n'.join(map(str, results)) + '\n')

main()