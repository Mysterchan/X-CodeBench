def can_reach_max_tower(t, test_cases):
    results = []
    for i in range(t):
        n, k = test_cases[i][0]
        heights = test_cases[i][1]
        start_height = heights[k - 1]
        max_height = max(heights)
        
        if max_height <= start_height:
            results.append("YES")
            continue
        
        time_to_drown = start_height
        max_tower_index = heights.index(max_height)
        teleport_time = abs(heights[max_tower_index] - start_height)

        # Calculate the time it would take to teleport to the highest tower
        if teleport_time + time_to_drown >= max_height:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    test_cases.append(((n, k), heights))

# Get results
results = can_reach_max_tower(t, test_cases)

# Print results
for result in results:
    print(result)