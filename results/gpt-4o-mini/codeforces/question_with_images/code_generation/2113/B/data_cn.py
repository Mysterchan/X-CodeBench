def can_cover_roof(t, cases):
    results = []
    for i in range(t):
        w, h, a, b = cases[i][0]
        x1, y1, x2, y2 = cases[i][1]
        
        # Calculate the occupied area by the two tiles
        occupied_area = (a * b) * 2
        total_area = w * h
        
        # Calculate remaining area
        remaining_area = total_area - occupied_area
        
        # Calculate the number of tiles needed to cover the remaining area
        tiles_needed = (remaining_area + (a * b) - 1) // (a * b)
        
        # The number of tiles needed must not exceed the effective space on the roof
        if tiles_needed <= (w // a) * (h // b):
            results.append("Yes")
        else:
            results.append("No")
    
    return results

# Input reading
t = int(input())
cases = []
for _ in range(t):
    w, h, a, b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    cases.append(((w, h, a, b), (x1, y1, x2, y2)))

# Getting results
results = can_cover_roof(t, cases)

# Output results
for result in results:
    print(result)