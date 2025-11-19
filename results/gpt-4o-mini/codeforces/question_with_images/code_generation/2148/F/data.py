def lexicographically_minimum_bottom_row(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        arrays = test_cases[i][1]
        
        max_length = max(len(a) for a in arrays)
        grid = [[] for _ in range(max_length)]
        
        # Fill the grid with the values
        for arr in arrays:
            for j in range(len(arr)):
                grid[j].append(arr[j])
                
        bottom_row = []
        
        # Construct the bottom row by taking the minimum values from each column
        for j in range(max_length):
            minimum_value = float('inf')
            for row in grid[j]:
                if row:
                    minimum_value = min(minimum_value, row)
            if minimum_value != float('inf'):
                bottom_row.append(minimum_value)
        
        results.append(" ".join(map(str, bottom_row)))
    
    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    arrays = []
    for _ in range(n):
        line = list(map(int, input().split()))
        arrays.append(line[1:])  # the first element is the length
    test_cases.append((n, arrays))

# Generating output
results = lexicographically_minimum_bottom_row(t, test_cases)
for result in results:
    print(result)