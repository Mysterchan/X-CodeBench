def min_max_after_operation(test_cases):
    results = []
    for case in test_cases:
        n, m, matrix = case
        row_min = [min(row) for row in matrix]
        col_min = [min(matrix[i][j] for i in range(n)) for j in range(m)]
        
        min_max_value = float('inf')
        
        for r in range(n):
            for c in range(m):
                max_after_operation = max(row_min[r] - 1, col_min[c] - 1)
                min_max_value = min(min_max_value, max_after_operation)
        
        results.append(min_max_value)
    
    return results

# Parse input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n, m = map(int, data[index].split())
    index += 1
    matrix = [list(map(int, data[index + i].split())) for i in range(n)]
    index += n
    test_cases.append((n, m, matrix))

# Get results
results = min_max_after_operation(test_cases)

# Print results
for result in results:
    print(result)