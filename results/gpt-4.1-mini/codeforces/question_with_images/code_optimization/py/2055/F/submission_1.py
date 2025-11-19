import sys
input = sys.stdin.readline

def can_partition(n, ranges):
    # Extract l_i and r_i arrays
    l = [x[0] for x in ranges]
    r = [x[1] for x in ranges]

    total_area = sum(r[i] - l[i] + 1 for i in range(n))
    half_area = total_area // 2

    # Try vertical partition (split by columns)
    # Check if there exists a column c such that sum of squares in columns <= c equals half_area
    # Since polyomino is convex, columns form intervals per row
    # We can binary search for c by prefix sums of columns

    # Collect all column boundaries
    cols = []
    for i in range(n):
        cols.append(l[i])
        cols.append(r[i] + 1)
    cols = sorted(set(cols))

    # Precompute prefix sums of area up to each column boundary
    # For each column boundary c, compute how many squares are in columns < c
    # We do this by summing over rows: count of squares in [l_i, r_i] intersected with [min_col, c-1]

    # To do this efficiently, we can process columns in order and keep track of coverage

    # Since columns can be large (up to 1e9), we only consider column boundaries from input
    # We'll do a prefix sum over these boundaries

    prefix_area = [0]  # prefix_area[i] = total squares in columns < cols[i]
    for i in range(1, len(cols)):
        c_start = cols[i-1]
        c_end = cols[i] - 1
        width = c_end - c_start + 1
        if width <= 0:
            prefix_area.append(prefix_area[-1])
            continue
        # Count how many rows cover this column segment
        count = 0
        for row in range(n):
            # intersection of [l[row], r[row]] and [c_start, c_end]
            left = max(l[row], c_start)
            right = min(r[row], c_end)
            if left <= right:
                count += right - left + 1
        prefix_area.append(prefix_area[-1] + count)

    # Now try to find a column c in cols such that prefix_area at c equals half_area
    # If found, vertical partition possible
    for i in range(1, len(cols)):
        if prefix_area[i] == half_area:
            # Check connectivity of both parts
            # Left part: columns < cols[i]
            # Right part: columns >= cols[i]
            # Because polyomino is convex, each part is connected if intervals per row are continuous and overlap vertically

            # Check left part connectivity:
            # For left part, rows with l_i <= cols[i]-1 and r_i >= l_i
            # The left part in row i is [l_i, min(r_i, cols[i]-1)]
            # Check if these intervals form a connected shape vertically:
            # i.e. intervals overlap or touch in consecutive rows

            def check_connected_side(start_col, end_col):
                prev_l = None
                prev_r = None
                for row in range(n):
                    left_bound = max(l[row], start_col)
                    right_bound = min(r[row], end_col)
                    if left_bound > right_bound:
                        # no squares in this row for this side
                        continue
                    if prev_l is None:
                        prev_l, prev_r = left_bound, right_bound
                    else:
                        # intervals must overlap or touch
                        if right_bound < prev_l - 1 or left_bound > prev_r + 1:
                            return False
                        # merge intervals
                        prev_l = min(prev_l, left_bound)
                        prev_r = max(prev_r, right_bound)
                return True

            if check_connected_side(-10**15, cols[i]-1) and check_connected_side(cols[i], 10**15):
                return True

    # Try horizontal partition (split by rows)
    # Since polyomino is convex, rows form intervals
    # We try to find k (1 <= k < n) such that sum of area in rows [0..k-1] = half_area
    # and top part and bottom part are congruent by vertical translation

    prefix_rows_area = [0]
    for i in range(n):
        prefix_rows_area.append(prefix_rows_area[-1] + (r[i] - l[i] + 1))

    for k in range(1, n):
        if prefix_rows_area[k] == half_area:
            # Check if top part and bottom part are congruent by vertical translation
            # Translation vector is (k, 0)
            # So for all i in [0..k-1], intervals must match intervals in [k..2k-1] shifted by k rows
            # But bottom part is rows [k..n-1], so n must be even and n=2k for perfect split
            if n == 2 * k:
                # Check intervals equality
                congruent = True
                for i in range(k):
                    if l[i] != l[i + k] or r[i] != r[i + k]:
                        congruent = False
                        break
                if congruent:
                    return True

    return False

t = int(input())
for _ in range(t):
    n = int(input())
    ranges = [tuple(map(int, input().split())) for __ in range(n)]
    print("YES" if can_partition(n, ranges) else "NO")