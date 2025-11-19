import sys
import math

def main():
    R = int(sys.stdin.readline())
    R_sq = R * R
    count = 0
    # i, j are integers representing the center of the square
    # The four corners of the square centered at (i,j) are:
    # (i±0.5, j±0.5)
    # Each corner must satisfy: x^2 + y^2 <= R^2
    # So max distance squared of corners = max over corners of (x^2 + y^2) <= R^2
    # The farthest corner from origin is the one with max |i±0.5| and |j±0.5|
    # So check if (i+0.5)^2 + (j+0.5)^2 <= R^2 for all corners
    # Actually, since the square is axis-aligned, the farthest corner is (i±0.5, j±0.5)
    # We must check all four corners, but since distance is monotonic in |x| and |y|,
    # the farthest corner is the one with max |i±0.5| and max |j±0.5|.
    # So the corner with (i+0.5, j+0.5) or (i+0.5, j-0.5) or (i-0.5, j+0.5) or (i-0.5, j-0.5)
    # The maximum distance squared among these four corners is max of these four distances.
    # To be inside circle, all four corners must be inside circle.
    # So the maximum of these four distances must be <= R^2.

    # To optimize, for each i, find the range of j such that all corners are inside circle.
    # The maximum distance corner is the one with max |i±0.5| and max |j±0.5|.
    # So for fixed i, the maximum distance corner is at (i_sign*0.5 + i, j_sign*0.5 + j)
    # where i_sign and j_sign are ±1 chosen to maximize distance.
    # Since distance depends on absolute values, max corner is at (i+0.5, j+0.5) or (i+0.5, j-0.5) etc.
    # So for fixed i, the maximum distance corner is at (i+0.5, j+0.5) or (i+0.5, j-0.5) or (i-0.5, j+0.5) or (i-0.5, j-0.5).
    # The maximum distance corner is the one with max |i±0.5| and max |j±0.5|.
    # So for fixed i, max |i±0.5| is fixed, and max |j±0.5| depends on j.
    # To ensure all corners inside circle, the corner with max distance must be inside circle.
    # So for fixed i, find max |i±0.5| = abs_i = max(abs(i-0.5), abs(i+0.5))
    # For j, max |j±0.5| = abs_j = max(abs(j-0.5), abs(j+0.5))
    # The distance squared = abs_i^2 + abs_j^2 <= R^2
    # For fixed i, abs_i is fixed, so abs_j^2 <= R^2 - abs_i^2
    # abs_j <= sqrt(R^2 - abs_i^2)
    # Since abs_j = max(|j-0.5|, |j+0.5|), the minimal abs_j is |j| + 0.5
    # Because |j±0.5| >= |j| - 0.5, but max(|j-0.5|, |j+0.5|) = |j| + 0.5
    # So abs_j = |j| + 0.5
    # So |j| + 0.5 <= sqrt(R^2 - abs_i^2)
    # => |j| <= sqrt(R^2 - abs_i^2) - 0.5
    # So for each i, j ranges from -floor(sqrt(R^2 - abs_i^2) - 0.5) to +floor(sqrt(R^2 - abs_i^2) - 0.5)

    for i in range(-R, R+1):
        abs_i = max(abs(i - 0.5), abs(i + 0.5))
        val = R_sq - abs_i * abs_i
        if val < 0:
            continue
        max_abs_j = math.sqrt(val) - 0.5
        if max_abs_j < 0:
            continue
        max_j = int(math.floor(max_abs_j))
        count += 2 * max_j + 1

    print(count)

if __name__ == "__main__":
    main()