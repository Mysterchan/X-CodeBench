def maximum_gold(t, cases):
    results = []
    for case in cases:
        n, m, k, grid = case
        gold_count = 0
        
        # Check each cell in the grid
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '.':
                    # Calculate boundaries of explosion
                    start_row = max(0, i - k)
                    end_row = min(n - 1, i + k)
                    start_col = max(0, j - k)
                    end_col = min(m - 1, j + k)

                    # Count gold on the borders
                    for x in range(start_row, end_row + 1):
                        for y in range(start_col, end_col + 1):
                            if (x == start_row or x == end_row or 
                                y == start_col or y == end_col):
                                if grid[x][y] == 'g':
                                    gold_count += 1

        results.append(gold_count)
    
    return results

# Input reading section
t = int(input())
cases = []
for _ in range(t):
    n, m, k = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    cases.append((n, m, k, grid))

# Get results
results = maximum_gold(t, cases)

# Output results
for result in results:
    print(result)