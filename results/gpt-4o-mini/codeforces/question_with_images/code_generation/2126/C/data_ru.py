def can_escape(num_cases, cases):
    results = []
    
    for n, k, heights in cases:
        max_height = max(heights)
        current_height = heights[k - 1]
        
        # Time until drowning
        time_until_drowning = current_height + 1
        
        # Check each tower for teleportation
        for i in range(n):
            if heights[i] >= max_height and heights[i] < time_until_drowning:
                results.append("YES")
                break
        else:
            results.append("NO")
    
    return results

# Input reading
t = int(input())
cases = []
for _ in range(t):
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    cases.append((n, k, heights))

# Calculate results
results = can_escape(t, cases)

# Output results
print('\n'.join(results))