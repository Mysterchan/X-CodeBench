def min_days_to_escape(num_cases, cases):
    results = []
    
    for n, x, grid in cases:
        x -= 1  # Convert to 0-based index
        left_bound = x
        right_bound = x
        
        # Expand left bound
        while left_bound > 0 and grid[left_bound - 1] == '.':
            left_bound -= 1
        
        # Expand right bound
        while right_bound < n - 1 and grid[right_bound + 1] == '.':
            right_bound += 1
            
        # Distance from Hamid to nearest walls
        dist_to_left_wall = x - left_bound
        dist_to_right_wall = right_bound - x
        
        # Need to figure out how many days it will take for Hamid to escape
        # Mani will block the escapes to maximize the days
        results.append(max(dist_to_left_wall, dist_to_right_wall))
    
    return results


# Input reading and preparation
t = int(input())
test_cases = []

for _ in range(t):
    n, x = map(int, input().split())
    s = input().strip()
    test_cases.append((n, x, s))

# Process cases
results = min_days_to_escape(t, test_cases)

# Print results for each test case
for result in results:
    print(result)