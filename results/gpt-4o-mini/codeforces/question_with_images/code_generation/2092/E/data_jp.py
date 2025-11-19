def process_cases(t, test_cases):
    MOD = 10**9 + 7
    results = []
    
    for n, m, k, color_info in test_cases:
        black_count = 0
        white_count = 0
        
        # Track positions colored
        colored = {}
        
        for x, y, c in color_info:
            colored[(x, y)] = c
            if c == 0:
                white_count += 1
            else:
                black_count += 1
        
        # Calculate the number of uncolored cells
        total_cells = n * m
        colored_cells = len(colored)
        uncolored_cells = total_cells - colored_cells
        
        uncolored_black = (n * m + 1) // 2 - black_count
        uncolored_white = n * m // 2 - white_count
        
        if ((black_count + white_count) % 2 == 1):
            results.append(0)
            continue
        
        if uncolored_cells == 0:
            results.append(1)
            continue
            
        # x = count of cells in black area, y = count of cells in white area
        if (black_count + uncolored_cells) % 2 != 0:
            results.append(0)
            continue
        
        total_ways = pow(2, uncolored_cells, MOD)
        results.append(total_ways)
    
    return results


# Read input
t = int(input().strip())
test_cases = []

for _ in range(t):
    n, m, k = map(int, input().strip().split())
    color_info = [tuple(map(int, input().strip().split())) for _ in range(k)]
    test_cases.append((n, m, k, color_info))

# Process the test cases
results = process_cases(t, test_cases)

# Print the results
for result in results:
    print(result)