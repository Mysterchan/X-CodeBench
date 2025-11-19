import sys
input = sys.stdin.readline

def rect_intersection_area(x1, y1, x2, y2, a, b):
    # Rectangle from (x1,y1) to (x1+a,y1+b)
    # Rectangle from (x2,y2) to (x2+a,y2+b)
    x_overlap = max(0, min(x1+a, x2+a) - max(x1, x2))
    y_overlap = max(0, min(y1+b, y2+b) - max(y1, y2))
    return x_overlap * y_overlap

def covered_area_on_roof(x, y, a, b, w, h):
    # Calculate area of sheet (x,y,a,b) overlapping with roof (0,0,w,h)
    x_overlap = max(0, min(x+a, w) - max(x, 0))
    y_overlap = max(0, min(y+b, h) - max(y, 0))
    return x_overlap * y_overlap

t = int(input())
for _ in range(t):
    w, h, a, b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    # Total roof area
    roof_area = w * h

    # Area covered by the two placed sheets on the roof
    area1 = covered_area_on_roof(x1, y1, a, b, w, h)
    area2 = covered_area_on_roof(x2, y2, a, b, w, h)

    # Intersection area of the two sheets (on the plane)
    inter = rect_intersection_area(x1, y1, x2, y2, a, b)

    # Intersection area on the roof (overlap counted twice)
    # But since sheets do not intersect, inter == 0 guaranteed by problem statement
    # So no need to subtract intersection on roof

    # Total covered area by the two sheets on the roof (no overlap)
    covered = area1 + area2

    # If sheets overlap on roof, subtract intersection on roof
    # But problem guarantees no intersection of sheets, so intersection area = 0

    # Remaining area to cover
    remain = roof_area - covered

    # If remain <= 0, roof is already fully covered by two sheets
    if remain <= 0:
        print("Yes")
        continue

    # Check if remain is divisible by sheet area
    sheet_area = a * b
    if remain % sheet_area != 0:
        print("No")
        continue

    # Now check if we can place the remaining sheets without overlapping existing two sheets
    # Sheets cannot be rotated, must be placed in grid aligned with a,b

    # The roof is tiled by sheets placed at positions:
    # (i*a, j*b) for i in [0..w//a], j in [0..h//b]
    # But sheets can be placed outside roof boundaries to cover roof fully

    # The two placed sheets occupy two positions (not necessarily aligned to grid)
    # But since sheets cannot be rotated and must be placed aligned to grid,
    # the two placed sheets must be at positions aligned to grid? No, problem states sheets cannot be rotated,
    # but does not say sheets must be placed aligned to grid. However, the problem states sheets cannot be rotated,
    # but does not say sheets must be placed aligned to grid. So sheets can be placed anywhere, but must not overlap.

    # However, the problem states sheets cannot be rotated, but does not say sheets must be placed aligned to grid.
    # But the problem states "Your team must cover the roof completely with sheets of size a x b,
    # sheets cannot be rotated, sheets cannot overlap, sheets can go outside roof boundaries."

    # The two sheets are placed arbitrarily (not necessarily aligned to grid),
    # but the rest of the sheets must be placed aligned to grid? The problem does not say sheets must be placed aligned to grid.

    # But the problem states "Your team must cover the roof completely with sheets of size a x b,
    # sheets cannot be rotated, sheets cannot overlap, sheets can go outside roof boundaries."

    # The problem does not say sheets must be placed aligned to grid, but the example and problem context imply sheets are placed in a grid.

    # Since sheets cannot be rotated and must cover the roof fully, the only way is to place sheets in a grid aligned with a,b.

    # The two sheets are placed arbitrarily, but must be part of the tiling.

    # So the problem reduces to:
    # Can we tile the roof with sheets placed at positions (i*a, j*b), i,j integers,
    # such that the two given sheets are among them (i.e. their positions coincide with some grid position),
    # and the rest of the roof is covered by sheets placed at other grid positions without overlapping the two given sheets.

    # But the problem states sheets cannot be rotated, but does not say sheets must be placed aligned to grid.
    # However, the problem states "sheets cannot be rotated (even by 90 degrees)" and "sheets cannot overlap",
    # and "sheets can go outside roof boundaries".

    # The problem states "Your team must cover the roof completely with sheets of size a x b",
    # and the two sheets are already placed arbitrarily (not necessarily aligned to grid),
    # but the rest of the sheets must be placed to cover the roof fully without removing the two sheets.

    # So the problem is: can we cover the roof with sheets of size a x b, placed without rotation,
    # no overlaps, sheets can go outside roof boundaries, and the two given sheets are fixed in their positions.

    # The key is that sheets cannot overlap, so the two given sheets occupy some positions,
    # and the rest of the sheets must be placed to cover the remaining roof area.

    # Since sheets cannot be rotated, and the roof is a rectangle, the only way to cover the roof fully is to place sheets in a grid aligned with a,b.

    # But the two sheets are placed arbitrarily, so if their positions are not aligned with the grid, it's impossible to tile the roof fully.

    # So the first check is: are the two sheets placed at positions aligned with the grid?

    # Check if x1 and y1 are multiples of a and b respectively
    # and x2 and y2 are multiples of a and b respectively

    # But the problem states sheets cannot be rotated, but does not say sheets must be placed aligned to grid.

    # However, the problem states "Your team must cover the roof completely with sheets of size a x b",
    # so the only way to cover the roof fully is to place sheets in a grid aligned with a,b.

    # So the two sheets must be placed at positions (i*a, j*b) for some integers i,j.

    # Check if x1 % a == 0 and y1 % b == 0 and x2 % a == 0 and y2 % b == 0

    # If not, answer is No

    if (x1 % a != 0) or (y1 % b != 0) or (x2 % a != 0) or (y2 % b != 0):
        print("No")
        continue

    # Now, the two sheets occupy two grid positions:
    # (x1//a, y1//b) and (x2//a, y2//b)

    # The roof grid size:
    grid_w = (w + a - 1) // a
    grid_h = (h + b - 1) // b

    # Total number of sheets needed to cover roof:
    total_sheets = grid_w * grid_h

    # Two sheets are already placed at positions (x1//a, y1//b) and (x2//a, y2//b)
    # They do not overlap (guaranteed)

    # Remaining sheets needed:
    remain_sheets = total_sheets - 2

    # We must check if it's possible to place remain_sheets sheets in the grid positions
    # excluding the two occupied positions.

    # Since sheets can go outside roof boundaries, but we only need to cover the roof,
    # and the roof is fully covered by grid_w * grid_h sheets placed at (i*a, j*b), i in [0,grid_w-1], j in [0,grid_h-1]

    # So the only question is if the two sheets are placed at valid grid positions inside the grid.

    # Check if the two sheets are inside the grid:
    i1, j1 = x1 // a, y1 // b
    i2, j2 = x2 // a, y2 // b

    if not (0 <= i1 < grid_w and 0 <= j1 < grid_h):
        print("No")
        continue
    if not (0 <= i2 < grid_w and 0 <= j2 < grid_h):
        print("No")
        continue

    # Since the two sheets do not overlap, and occupy two distinct grid positions,
    # and the rest of the grid positions are free to place sheets,
    # we can place the remaining sheets to cover the roof fully.

    print("Yes")