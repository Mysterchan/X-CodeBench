def can_divide_polyhedra(test_cases):
    results = []
    for case in test_cases:
        n, ranges = case
        total_area = 0
        min_col = float('inf')
        max_col = float('-inf')
        
        for l, r in ranges:
            total_area += (r - l + 1)
            min_col = min(min_col, l)
            max_col = max(max_col, r)
        
        if total_area % 2 != 0:
            results.append("NO")
            continue
        
        # Check if we can find a valid split
        half_area = total_area // 2
        current_area = 0
        found_split = False
        
        for l, r in ranges:
            current_area += (r - l + 1)
            if current_area == half_area:
                found_split = True
                break
            elif current_area > half_area:
                break
        
        if found_split:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    ranges = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, ranges))

# Get results
results = can_divide_polyhedra(test_cases)

# Print results
for result in results:
    print(result)