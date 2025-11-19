import sys
input = sys.stdin.readline

def can_partition(n, intervals):
    # The polyomino is convex and given by intervals [l_i, r_i] for each row i.
    # The total area is even.
    # We want to check if it can be split into two connected congruent polyominoes by translation only.

    # Key observations:
    # 1) The two parts must be congruent by translation, so the shape of one part is exactly the same as the other,
    #    just shifted by some vector (dx, dy).
    # 2) The total area is even, so each part has area = total_area / 2.
    # 3) The polyomino is convex, so each row is a continuous segment.
    # 4) The partition must split the polyomino into two connected parts.
    #
    # The problem reduces to checking if there exists a vector (dx, dy) such that:
    # - The polyomino can be partitioned into two parts A and B = A + (dx, dy)
    # - A and B are connected
    # - A and B are disjoint and cover the whole polyomino
    #
    # Since the polyomino is convex and given by intervals, the only possible translations that can partition it
    # into two congruent parts are either vertical or horizontal shifts.
    #
    # We try two types of splits:
    # 1) Horizontal split: split rows into two halves of equal area, and check if top half matches bottom half shifted vertically.
    # 2) Vertical split: split columns into two halves of equal area, and check if left half matches right half shifted horizontally.
    #
    # Because the polyomino is convex, the vertical split means splitting each row into two parts of equal length.
    # The horizontal split means splitting the rows into two groups with equal total area.
    #
    # We will check both possibilities.

    total_area = 0
    row_lengths = []
    for l, r in intervals:
        length = r - l + 1
        row_lengths.append(length)
        total_area += length

    # Try horizontal split:
    # Find a row index m where sum of areas of rows 1..m = total_area/2
    half_area = total_area // 2
    prefix_sum = 0
    m = -1
    for i in range(n):
        prefix_sum += row_lengths[i]
        if prefix_sum == half_area:
            m = i
            break
        elif prefix_sum > half_area:
            break

    if m != -1:
        # Check if top half and bottom half are congruent by vertical translation
        # top half: rows 0..m
        # bottom half: rows m+1..n-1
        # The bottom half should be exactly the top half shifted down by (m+1) rows
        # So intervals[i] should equal intervals[i + m + 1] for i in [0..m]
        # Check if n == 2*(m+1)
        if n == 2 * (m + 1):
            top = intervals[:m+1]
            bottom = intervals[m+1:]
            # Check if bottom[i] == top[i] for all i
            if all(top[i] == bottom[i] for i in range(m+1)):
                return "YES"

    # Try vertical split:
    # The polyomino is convex, so each row is a continuous segment.
    # We want to split each row into two parts of equal length.
    # So for each row, length must be even.
    # Then we check if left halves and right halves match by horizontal translation.

    # Check if all row lengths are even
    if all(length % 2 == 0 for length in row_lengths):
        # Construct left and right halves
        left_intervals = []
        right_intervals = []
        for l, r in intervals:
            length = r - l + 1
            half_len = length // 2
            left_intervals.append((l, l + half_len - 1))
            right_intervals.append((r - half_len + 1, r))

        # Check if left_intervals and right_intervals are congruent by horizontal translation
        # That means for some dx, for all i: right_intervals[i] = left_intervals[i] + dx
        # Since intervals are continuous, dx = right_intervals[i][0] - left_intervals[i][0]
        # Check if dx is the same for all rows
        dx = right_intervals[0][0] - left_intervals[0][0]
        if all((right_intervals[i][0] - left_intervals[i][0] == dx and
                right_intervals[i][1] - left_intervals[i][1] == dx) for i in range(n)):
            return "YES"

    return "NO"


t = int(input())
results = []
for _ in range(t):
    n = int(input())
    intervals = [tuple(map(int, input().split())) for __ in range(n)]
    results.append(can_partition(n, intervals))

print("\n".join(results))