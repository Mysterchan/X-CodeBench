def minimum_operations(test_cases):
    results = []
    
    for n, mountains in test_cases:
        total_zeros = total_ones = 0
        excess_zeros = excess_ones = 0
        
        for a, b, c, d in mountains:
            total_zeros += a
            total_ones += b
            
            # Current excess in this mountain
            if a > c:
                excess_zeros += a - c
            if b > d:
                excess_ones += b - d
        
        # Calculate the required operations
        total_required_operations = max(excess_zeros, excess_ones)
        results.append(total_required_operations)
    
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
    index += 1
    mountains = []
    for _ in range(n):
        a, b, c, d = map(int, data[index].split())
        mountains.append((a, b, c, d))
        index += 1
    test_cases.append((n, mountains))

# Get results and print them
results = minimum_operations(test_cases)
for result in results:
    print(result)