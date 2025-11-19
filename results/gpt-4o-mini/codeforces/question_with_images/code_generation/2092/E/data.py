def count_ways(t, test_cases):
    MOD = 10**9 + 7
    results = []
    
    for case in test_cases:
        n, m, k, colored_cells = case
        black_count = 0
        white_count = 0
        
        # Count black and white cells in the given (k) cells
        for (x, y, c) in colored_cells:
            if c == 0:
                white_count += 1
            else:
                black_count += 1
        
        # Determine total colored (not green) cells
        total_colored = black_count + white_count
        
        # Cells are colored in a checkerboard pattern
        total_cells = n * m
        
        # The remaining green cells will be:
        uncolored_cells = total_cells - total_colored
        
        # The number of black and white cells is determined by the parity of total colored
        if (black_count + white_count) % 2 == 1:
            results.append(0)
        else:
            if uncolored_cells % 2 == 0:
                # Both cells can be colored
                results.append(pow(2, uncolored_cells, MOD))
            else:
                # Cannot have odd uncolored cells that maintain the evenness
                results.append(0)

    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

line_index = 1
for _ in range(t):
    n, m, k = map(int, data[line_index].split())
    colored_cells = []
    for j in range(k):
        x, y, c = map(int, data[line_index + 1 + j].split())
        colored_cells.append((x, y, c))
    test_cases.append((n, m, k, colored_cells))
    line_index += k + 1

# Get results
results = count_ways(t, test_cases)

# Print results
for result in results:
    print(result)