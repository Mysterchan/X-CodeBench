def min_days_to_escape(test_cases):
    results = []
    
    for n, x, s in test_cases:
        x -= 1  # Convert to 0-based index
        
        # Find the nearest wall on the left
        left_wall = x
        while left_wall >= 0 and s[left_wall] == '.':
            left_wall -= 1
        # Find the nearest wall on the right
        right_wall = x
        while right_wall < n and s[right_wall] == '.':
            right_wall += 1
        
        distance_left = x - left_wall
        distance_right = right_wall - x
        
        # The optimal strategy to escape takes the minimum distance
        result = min(distance_left, distance_right)
        results.append(result)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n, x = map(int, data[index].split())
    s = data[index + 1]
    test_cases.append((n, x, s))
    index += 2

# Get results
results = min_days_to_escape(test_cases)

# Print results
for res in results:
    print(res)