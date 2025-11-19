def can_tile_roof(w, h, a, b, x1, y1, x2, y2):
    # Calculate the total area of the roof and the two existing sheets
    roof_area = w * h
    sheet_area = a * b
    total_sheet_area = 2 * sheet_area

    # If the total area of the sheets is greater than or equal to the roof area,
    # it's immediately a "Yes" as they can cover the whole area or more
    if total_sheet_area >= roof_area:
        return "Yes"

    # Calculate the usable width and height left for new sheets
    left_gap = x1  # left space available on the left of the first sheet
    right_gap = w - (x2 + a)  # right space available on the right of the second sheet
    bottom_gap = y1  # bottom space available below the first sheet
    top_gap = h - (y2 + b)  # top space available above the second sheet

    # Check how many sheets can fit in each gap
    total_sheets = (
        (left_gap // a) * (h // b) +  # sheets to the left of the first sheet
        (right_gap // a) * (h // b) +  # sheets to the right of the second sheet
        (bottom_gap // b) * (w // a) +  # sheets below the first sheet
        (top_gap // b) * (w // a)  # sheets above the second sheet
    )

    # If total sheets that can be placed in the available gaps
    # plus the area already covered by the existing sheets can
    # cover the roof, return "Yes"
    if total_sheets >= ((roof_area - total_sheet_area) // sheet_area):
        return "Yes"
    
    # Otherwise, return "No"
    return "No"

# Read number of test cases
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
results = []
index = 1

for _ in range(t):
    w, h, a, b = map(int, data[index].split())
    x1, y1, x2, y2 = map(int, data[index + 1].split())
    index += 2

    result = can_tile_roof(w, h, a, b, x1, y1, x2, y2)
    results.append(result)

# Output all results
print("\n".join(results))