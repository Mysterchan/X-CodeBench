def min_max_after_operation(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, matrix = case
        max_values_row = [max(row) for row in matrix]  # Max in each row
        max_values_col = [max(matrix[i][j] for i in range(n)) for j in range(m)]  # Max in each column
        
        overall_min_max = float('inf')
        
        for r in range(n):
            for c in range(m):
                # Calculate the max value after the operation (decreasing row r and column c)
                max_value_after_op = max(max_values_row[r] - 1, max_values_col[c] - 1)
                
                # Special case: if matrix[r][c] is one of these max values
                # since it will be decreased twice (once for row, once for column)
                if matrix[r][c] == max_values_row[r] and matrix[r][c] == max_values_col[c]:
                    max_value_after_op = max(max_value_after_op, matrix[r][c] - 2)
                
                # Update the overall minimum maximum value found
                overall_min_max = min(overall_min_max, max_value_after_op)
        
        results.append(overall_min_max)
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n, m = map(int, data[index].split())
    index += 1
    matrix = []
    for i in range(n):
        row = list(map(int, data[index].split()))
        matrix.append(row)
        index += 1
    test_cases.append((n, m, matrix))

# Getting results
results = min_max_after_operation(t, test_cases)

# Output result
for result in results:
    print(result)