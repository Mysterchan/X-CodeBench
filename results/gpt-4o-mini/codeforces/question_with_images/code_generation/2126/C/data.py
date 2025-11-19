def can_reach_max_height(t, test_cases):
    results = []
    for i in range(t):
        n, k = test_cases[i][0]
        heights = test_cases[i][1]
        
        k_index = k - 1
        max_height = max(heights)
        
        if heights[k_index] >= max_height:
            results.append("YES")
            continue
        
        if heights[k_index] < max_height:
            # Time before water covers
            time_until_cover = heights[k_index] + 1
            
            # Time it takes to reach the tower with max height
            can_reach = False
            for j in range(n):
                if heights[j] == max_height:
                    teleport_time = abs(heights[k_index] - heights[j])
                    if teleport_time < time_until_cover:
                        can_reach = True
                        break
            
            results.append("YES" if can_reach else "NO")
    
    return results

# Read inputs
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    test_cases.append(((n, k), heights))

# Get results
results = can_reach_max_height(t, test_cases)

# Output results
for result in results:
    print(result)