import sys
import math

def main():
    R = int(sys.stdin.readline().strip())
    R_sq = R * R
    count = 0

    # We want to count integer pairs (i,j) such that all four corners of the square centered at (i,j)
    # are inside the circle of radius R centered at (0,0).
    #
    # The four corners are:
    # (i+0.5, j+0.5), (i+0.5, j-0.5), (i-0.5, j+0.5), (i-0.5, j-0.5)
    #
    # The farthest corner from the origin for a given (i,j) is the one with the largest distance.
    # To ensure the entire square is inside the circle, the farthest corner must be inside the circle.
    #
    # The farthest corner from the origin is the one with coordinates:
    # (i + 0.5 * sign(i), j + 0.5 * sign(j))
    # but since the circle is centered at (0,0), the farthest corner is the one with the largest distance.
    #
    # To simplify, we check all four corners for each (i,j).
    #
    # Since the circle radius is R, the maximum |i| or |j| we need to check is floor(R + 0.5)
    # because the corner at (i ± 0.5, j ± 0.5) must be inside the circle.
    #
    # We'll iterate over i in [-max_coord, max_coord] and for each i find the range of j that satisfy the condition.

    max_coord = int(math.floor(R + 0.5))

    for i in range(-max_coord, max_coord + 1):
        # For each i, find the maximum j such that all four corners are inside the circle.
        # The corners are:
        # (i±0.5, j±0.5)
        #
        # The condition is:
        # (i+0.5)^2 + (j+0.5)^2 <= R^2
        # (i+0.5)^2 + (j-0.5)^2 <= R^2
        # (i-0.5)^2 + (j+0.5)^2 <= R^2
        # (i-0.5)^2 + (j-0.5)^2 <= R^2
        #
        # For fixed i, we want to find all integer j such that all four inequalities hold.
        #
        # Let's define:
        # a1 = (i+0.5)^2
        # a2 = (i-0.5)^2
        #
        # For j, the four inequalities become:
        # j^2 + j + 0.25 + a1 <= R^2
        # j^2 - j + 0.25 + a1 <= R^2
        # j^2 + j + 0.25 + a2 <= R^2
        # j^2 - j + 0.25 + a2 <= R^2
        #
        # Rearranged:
        # j^2 + j <= R^2 - 0.25 - a1
        # j^2 - j <= R^2 - 0.25 - a1
        # j^2 + j <= R^2 - 0.25 - a2
        # j^2 - j <= R^2 - 0.25 - a2
        #
        # So j must satisfy all four inequalities.
        #
        # The most restrictive bounds come from the minimum of the right sides.
        #
        # Let's define:
        # M1 = R^2 - 0.25 - a1
        # M2 = R^2 - 0.25 - a2
        #
        # Then j must satisfy:
        # j^2 + j <= min(M1, M2)
        # j^2 - j <= min(M1, M2)
        #
        # Let's call M = min(M1, M2)
        #
        # For j^2 + j <= M:
        # j^2 + j - M <= 0
        # Solve quadratic: j = [-1 ± sqrt(1 + 4M)] / 2
        #
        # For j^2 - j <= M:
        # j^2 - j - M <= 0
        # Solve quadratic: j = [1 ± sqrt(1 + 4M)] / 2
        #
        # The intersection of these intervals gives the valid j range.

        a1 = (i + 0.5) ** 2
        a2 = (i - 0.5) ** 2
        M1 = R_sq - 0.25 - a1
        M2 = R_sq - 0.25 - a2
        M = min(M1, M2)

        if M < 0:
            # No j satisfies the condition for this i
            continue

        sqrt_val = math.sqrt(1 + 4 * M)

        # For j^2 + j <= M:
        j_min1 = math.ceil((-1 - sqrt_val) / 2)
        j_max1 = math.floor((-1 + sqrt_val) / 2)

        # For j^2 - j <= M:
        j_min2 = math.ceil((1 - sqrt_val) / 2)
        j_max2 = math.floor((1 + sqrt_val) / 2)

        # Intersection of intervals [j_min1, j_max1] and [j_min2, j_max2]
        j_min = max(j_min1, j_min2)
        j_max = min(j_max1, j_max2)

        if j_min <= j_max:
            count += (j_max - j_min + 1)

    print(count)

if __name__ == "__main__":
    main()