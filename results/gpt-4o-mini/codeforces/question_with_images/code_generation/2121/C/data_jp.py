def min_max_after_operation(test_cases):
    results = []
    for n, m, matrix in test_cases:
        max_after_operation = float('inf')
        
        # Iterate through every possible (r, c)
        for r in range(n):
            for c in range(m):
                # Calculate the maximum value after the operation at (r, c)
                max_value = 0
                for i in range(n):
                    for j in range(m):
                        if i == r or j == c:
                            max_value = max(max_value, matrix[i][j] - 1)
                        else:
                            max_value = max(max_value, matrix[i][j])
                max_after_operation = min(max_after_operation, max_value)
        
        results.append(max_after_operation)

    return results

t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, m, matrix))

results = min_max_after_operation(test_cases)
for result in results:
    print(result)