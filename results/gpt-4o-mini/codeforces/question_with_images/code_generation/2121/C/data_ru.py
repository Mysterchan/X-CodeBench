def minimize_max_after_operation(test_cases):
    results = []
    
    for n, m, matrix in test_cases:
        # Calculate the maximum values in rows and columns
        max_in_rows = [0] * n
        max_in_cols = [0] * m
        
        for i in range(n):
            for j in range(m):
                max_in_rows[i] = max(max_in_rows[i], matrix[i][j])
                max_in_cols[j] = max(max_in_cols[j], matrix[i][j])
        
        # Calculate the minimum of maximum values after operation
        min_max_value = float('inf')
        
        for r in range(n):
            for c in range(m):
                # max value after operation on row r and column c
                # max_ij becomes max(a_ij - 1) for row r and column c
                max_value_after_operation = max(
                    max_in_rows[r] - 1,  # Reduce the entire row r
                    max_in_cols[c] - 1   # Reduce the entire column c
                )
                # Check the values from other rows and columns
                for k in range(n):
                    if k != r:  # Not reducing row r
                        max_value_after_operation = max(max_value_after_operation, max_in_rows[k])
                for l in range(m):
                    if l != c:  # Not reducing column c
                        max_value_after_operation = max(max_value_after_operation, max_in_cols[l])
                
                min_max_value = min(min_max_value, max_value_after_operation)
        
        results.append(min_max_value)
    
    return results

import sys
input = sys.stdin.read
data = input().strip().split('\n')

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n, m = map(int, data[index].split())
    index += 1
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, data[index].split())))
        index += 1
    test_cases.append((n, m, matrix))

results = minimize_max_after_operation(test_cases)

for res in results:
    print(res)