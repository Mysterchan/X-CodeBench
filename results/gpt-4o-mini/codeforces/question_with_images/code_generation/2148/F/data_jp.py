def find_minimum_bottom_row(test_cases):
    results = []
    
    for case in test_cases:
        n, arrays = case
        max_length = max(len(arr) for arr in arrays)
        positions = [[] for _ in range(max_length)]
        
        for array in arrays:
            for i in range(len(array)):
                positions[i].append(array[i])
        
        bottom_row = []
        for pos in positions:
            if pos:
                bottom_row.append(min(pos))
        
        results.append(' '.join(map(str, bottom_row)))
    
    return results


# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
index = 1
test_cases = []

for _ in range(t):
    n = int(data[index])
    index += 1
    arrays = []
    for __ in range(n):
        line = list(map(int, data[index].split()))
        arrays.append(line[1:])  # Exclude the first number k_i
        index += 1
    test_cases.append((n, arrays))

# Execute the function and print results
results = find_minimum_bottom_row(test_cases)
print('\n'.join(results))