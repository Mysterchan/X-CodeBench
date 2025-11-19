def min_crossings(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, x, y, a, b = case
        
        # Calculate crossings for horizontal lasers
        crossing_y = sum(1 for ai in a if ai < y)  # All horizontal lasers below target y
        
        # Calculate crossings for vertical lasers
        crossing_x = sum(1 for bi in b if bi < x)  # All vertical lasers left of target x
        
        # The minimum number of crossings is the sum of necessary crossings
        results.append(crossing_y + crossing_x)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

# Parse the input
t = int(data[0])
test_cases = []
index = 1
for _ in range(t):
    n, m, x, y = map(int, data[index].split())
    a = list(map(int, data[index + 1].split()))
    b = list(map(int, data[index + 2].split()))
    test_cases.append((n, m, x, y, a, b))
    index += 3

# Get the results
results = min_crossings(t, test_cases)

# Print the results
for result in results:
    print(result)