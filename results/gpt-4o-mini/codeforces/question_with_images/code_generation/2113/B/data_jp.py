def can_tile_roof(test_cases):
    results = []
    for w, h, a, b, x1, y1, x2, y2 in test_cases:
        # Calculate total area of the roof
        total_area = w * h
        # Calculate the area of the two sheets
        sheet_area = a * b
        placed_sheets_area = sheet_area * 2
        
        # Check remaining area after placing the two sheets
        remaining_area = total_area - placed_sheets_area
        
        # If the remaining area is negative or not divisible by the area of a single sheet, it's impossible
        if remaining_area < 0 or remaining_area % sheet_area != 0:
            results.append("No")
            continue
        
        # Get the positions of the placed sheets
        placed_sheets = [(x1, y1, x1 + a, y1 + b), (x2, y2, x2 + a, y2 + b)]
        
        # Find outer bounds
        min_x = min(placed_sheets[0][0], placed_sheets[1][0])
        max_x = max(placed_sheets[0][2], placed_sheets[1][2])
        min_y = min(placed_sheets[0][1], placed_sheets[1][1])
        max_y = max(placed_sheets[0][3], placed_sheets[1][3])
        
        # Check if the sheets fit within the roof's dimensions or allow for extention
        if min_x < 0 or min_y < 0 or max_x > w or max_y > h:
            results.append("No")
            continue
        
        results.append("Yes")
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []
line_index = 1
for _ in range(t):
    w, h, a, b = map(int, data[line_index].split())
    x1, y1, x2, y2 = map(int, data[line_index + 1].split())
    test_cases.append((w, h, a, b, x1, y1, x2, y2))
    line_index += 2

results = can_tile_roof(test_cases)
print("\n".join(results))