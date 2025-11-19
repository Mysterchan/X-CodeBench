import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    xs = []
    ys = []
    for __ in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    # Initial rectangle cost without any move
    base_cost = (max_x - min_x + 1) * (max_y - min_y + 1)

    # If only one monster, cost is 1
    if n == 1:
        print(1)
        continue

    # We want to try moving one monster to reduce the rectangle area.
    # The rectangle is defined by min_x, max_x, min_y, max_y.
    # Moving one monster can potentially reduce the rectangle by removing one extreme.

    # To do this efficiently:
    # We find the 2 smallest and 2 largest x and y coordinates.
    # Because moving one monster can only remove one extreme coordinate if that monster is the unique one at that extreme.

    xs_sorted = sorted(xs)
    ys_sorted = sorted(ys)

    # Candidates for min_x after removing one monster:
    # - If the monster at min_x is unique, then min_x can be increased to xs_sorted[1]
    # - Otherwise min_x stays the same
    # Similarly for max_x, min_y, max_y

    # Count how many monsters have min_x, max_x, min_y, max_y
    count_min_x = xs.count(min_x)
    count_max_x = xs.count(max_x)
    count_min_y = ys.count(min_y)
    count_max_y = ys.count(max_y)

    # Possible new min_x if we remove one monster at min_x (only if count_min_x == 1)
    new_min_x_candidates = [min_x]
    if count_min_x == 1:
        new_min_x_candidates.append(xs_sorted[1])

    # Possible new max_x if we remove one monster at max_x (only if count_max_x == 1)
    new_max_x_candidates = [max_x]
    if count_max_x == 1:
        new_max_x_candidates.append(xs_sorted[-2])

    # Possible new min_y if we remove one monster at min_y (only if count_min_y == 1)
    new_min_y_candidates = [min_y]
    if count_min_y == 1:
        new_min_y_candidates.append(ys_sorted[1])

    # Possible new max_y if we remove one monster at max_y (only if count_max_y == 1)
    new_max_y_candidates = [max_y]
    if count_max_y == 1:
        new_max_y_candidates.append(ys_sorted[-2])

    # We try all combinations of new min_x, max_x, min_y, max_y
    # but we can only remove one monster, so only one of these extremes can be changed at a time.
    # So we try changing min_x, or max_x, or min_y, or max_y individually, or none.

    ans = base_cost

    # No move
    # ans = min(ans, base_cost) # already base_cost

    # Change min_x only
    for nx in new_min_x_candidates:
        if nx != min_x:
            cost = (max_x - nx + 1) * (max_y - min_y + 1)
            if cost < ans:
                ans = cost

    # Change max_x only
    for nx in new_max_x_candidates:
        if nx != max_x:
            cost = (nx - min_x + 1) * (max_y - min_y + 1)
            if cost < ans:
                ans = cost

    # Change min_y only
    for ny in new_min_y_candidates:
        if ny != min_y:
            cost = (max_x - min_x + 1) * (max_y - ny + 1)
            if cost < ans:
                ans = cost

    # Change max_y only
    for ny in new_max_y_candidates:
        if ny != max_y:
            cost = (max_x - min_x + 1) * (ny - min_y + 1)
            if cost < ans:
                ans = cost

    print(ans)