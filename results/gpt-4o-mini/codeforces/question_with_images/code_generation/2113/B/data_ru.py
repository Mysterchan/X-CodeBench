def can_tile_roof(w, h, a, b, x1, y1, x2, y2):
    sheet1 = (x1, y1, x1 + a, y1 + b)
    sheet2 = (x2, y2, x2 + a, y2 + b)

    min_x = min(sheet1[0], sheet2[0])
    max_x = max(sheet1[2], sheet2[2])
    min_y = min(sheet1[1], sheet2[1])
    max_y = max(sheet1[3], sheet2[3])

    # Check if the area between the sheets can be filled
    # Total area of roof
    roof_area = w * h
    # Total area of two sheets
    sheets_area = (sheet1[2] - sheet1[0]) * (sheet1[3] - sheet1[1]) + (sheet2[2] - sheet2[0]) * (sheet2[3] - sheet2[1])

    return sheets_area >= roof_area

t = int(input())
results = []

for _ in range(t):
    w, h, a, b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    if can_tile_roof(w, h, a, b, x1, y1, x2, y2):
        results.append("Yes")
    else:
        results.append("No")

print("\n".join(results))