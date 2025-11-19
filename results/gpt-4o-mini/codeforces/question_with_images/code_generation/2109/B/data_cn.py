def duel_rounds(t, test_cases):
    results = []
    for n, m, a, b in test_cases:
        # Calculate the distances to the edges
        top = a - 1
        bottom = n - a
        left = b - 1
        right = m - b
        
        # The maximum distance to any edge
        max_distance = max(top, bottom, left, right)
        
        # The minimum number of rounds is determined by the maximum distance
        # Each round can reduce the grid size by at least 1 in one dimension
        results.append(max_distance + 1)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = [tuple(map(int, line.split())) for line in data[1:t + 1]]

# Get results
results = duel_rounds(t, test_cases)

# Print results
for result in results:
    print(result)