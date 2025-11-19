import sys
from math import gcd
from collections import defaultdict

def main():
    input = sys.stdin.readline
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    # A trapezoid has at least one pair of parallel sides.
    # Since no three points are collinear, any pair of points defines a unique line.
    # We consider all pairs of points and group them by their slope.
    # For each slope group, count how many pairs share the same line offset (intercept).
    # Then count the number of pairs of parallel segments that can form trapezoids.

    # To avoid floating point precision issues, represent slope as a reduced fraction (dy, dx).
    # Also represent the line uniquely by slope and intercept.
    # Intercept can be represented as c = y*dx - x*dy (line equation: dy*x - dx*y + c = 0)
    # We normalize c by gcd with dy and dx to keep consistent representation.

    # Step 1: For each pair of points, compute slope and line offset, group pairs by slope and offset.
    # Step 2: For each slope, we have groups of pairs on different parallel lines.
    # Step 3: Count the number of pairs of pairs from different lines with the same slope.
    # Each such pair corresponds to a pair of parallel segments.
    # Step 4: The number of trapezoids is sum over all slopes of sum over all pairs of lines of (count_line_i * count_line_j)
    # Because each pair of segments from different parallel lines can form trapezoids with the other two points.

    # Since no three points are collinear, each pair of points defines a unique line.
    # So each pair belongs to exactly one line.

    # We'll store for each slope a dictionary: offset -> count of pairs on that line.

    slope_map = defaultdict(lambda: defaultdict(int))

    for i in range(N):
        x1, y1 = points[i]
        for j in range(i+1, N):
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1
            g = gcd(dy, dx)
            dy //= g
            dx //= g
            # Normalize slope direction: dx > 0 or if dx == 0 then dy > 0
            if dx < 0:
                dx = -dx
                dy = -dy
            elif dx == 0 and dy < 0:
                dy = -dy

            # Compute offset c = dy*x - dx*y for one point (x1,y1)
            # This represents the line equation: dy*x - dx*y + c = 0
            c = dy * x1 - dx * y1
            # Normalize c by gcd with dy and dx to keep consistent representation
            g2 = gcd(c, gcd(dy, dx))
            if g2 != 0:
                c //= g2

            slope_map[(dy, dx)][c] += 1

    # Now count trapezoids
    # For each slope, we have multiple lines (offsets) with counts of pairs.
    # Number of trapezoids formed by pairs of lines with counts c1 and c2 is c1 * c2
    # Sum over all pairs of distinct lines for each slope.

    result = 0
    for slope, offset_dict in slope_map.items():
        counts = list(offset_dict.values())
        total_pairs = 0
        s = sum(counts)
        # sum of c_i * c_j for i<j = (s*s - sum(c_i^2)) / 2
        sum_sq = sum(c*c for c in counts)
        total_pairs = (s*s - sum_sq) // 2
        result += total_pairs

    print(result)

if __name__ == "__main__":
    main()