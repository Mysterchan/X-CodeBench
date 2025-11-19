def min_operations(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        operations_needed = 0
        
        total_zero_deficit = 0
        total_one_deficit = 0
        
        for j in range(n):
            a, b, c, d = test_cases[i][1][j]
            
            # Calculate deficit for zeros and ones
            if a < c:
                total_zero_deficit += (c - a)  # How many more zeros we need
            if b < d:
                total_one_deficit += (d - b)  # How many more ones we need
            
            # Calculate surplus of zeros and ones
            if a > c:
                operations_needed += (a - c)  # Excess zeros
            if b > d:
                operations_needed += (b - d)  # Excess ones
        
        # The total operations needed is the maximum of the necessary deficits
        operations_needed += max(total_zero_deficit, total_one_deficit)
        
        results.append(operations_needed)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n = int(data[index])
    stacks = []
    for j in range(n):
        a, b, c, d = map(int, data[index + 1 + j].split())
        stacks.append((a, b, c, d))
    test_cases.append((n, stacks))
    index += n + 1

# Get results
results = min_operations(t, test_cases)

# Print results
for result in results:
    print(result)