import sys
import math

def main():
    R = int(sys.stdin.readline())
    R_sq = R * R
    count = 0

    # i corresponds to x-coordinate of square center
    # For each i, find max j such that all four corners are inside circle
    # The corners of square centered at (i,j) are:
    # (i±0.5, j±0.5)
    # The farthest corner from origin is the one with max |x| and max |y| in the same quadrant.
    # Since distance is symmetric, we can consider only i,j >= 0 and multiply accordingly.

    # But since the circle is centered at (0,0), and squares are centered at integer coords,
    # we can iterate i from -R to R and for each i find max j.

    # To optimize:
    # For each i in [-R, R], find max j >= 0 such that the corner (i+0.5, j+0.5) is inside circle.
    # Because if (i+0.5, j+0.5) is inside circle, then all other corners (which are closer or equal distance)
    # are also inside circle.

    # Actually, the farthest corner from origin for square at (i,j) is the corner with coordinates:
    # (i + 0.5 * sign(i), j + 0.5 * sign(j))
    # But since we want all four corners inside circle, the corner with max distance is (i+0.5, j+0.5) if i,j >=0,
    # and similarly for other quadrants.

    # To avoid sign complications, we can use absolute values:
    # For square centered at (i,j), the farthest corner from origin is at (|i|+0.5, |j|+0.5)
    # So condition: (|i|+0.5)^2 + (|j|+0.5)^2 <= R^2

    # So we can iterate i from 0 to R, for each i find max j >= 0 satisfying above.
    # Then count squares in all four quadrants:
    # - if i=0 and j=0: count 1
    # - if i=0 and j>0: count 2 (j and -j)
    # - if i>0 and j=0: count 2 (i and -i)
    # - if i>0 and j>0: count 4 (all quadrants)

    max_i = R
    count = 0
    for i in range(0, max_i + 1):
        x = i + 0.5
        # find max j >= 0 with (x)^2 + (j+0.5)^2 <= R^2
        # (j+0.5)^2 <= R^2 - x^2
        val = R_sq - x * x
        if val < 0:
            continue
        max_j = int(math.floor(math.sqrt(val) - 0.5))
        if max_j < 0:
            continue
        for j in range(0, max_j + 1):
            # count squares according to quadrant
            if i == 0 and j == 0:
                count += 1
            elif i == 0 and j > 0:
                count += 2
            elif i > 0 and j == 0:
                count += 2
            else:
                count += 4

    print(count)

if __name__ == "__main__":
    main()