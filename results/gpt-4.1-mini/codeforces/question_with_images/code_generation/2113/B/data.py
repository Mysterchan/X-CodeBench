def can_tile(w, h, a, b, x1, y1, x2, y2):
    # The roof is w x h, sheets are a x b, placed sheets at (x1,y1) and (x2,y2)
    # Sheets cannot be rotated, must cover entire roof, no overlap, sheets can extend beyond roof.
    # We want to check if it's possible to cover the roof completely without removing the two placed sheets.

    # The key insight:
    # Since sheets cannot be rotated, the roof must be tiled by a grid of a x b sheets aligned in the same orientation.
    # The two placed sheets are fixed and do not overlap.
    # We want to check if the two placed sheets fit into the grid of sheets that cover the roof.
    # The sheets can extend beyond the roof, so the grid can start at some offset (X0, Y0) such that:
    # - The two placed sheets align with the grid (i.e., their bottom-left corners coincide with some grid points)
    # - The grid covers the entire roof (0,0) to (w,h)
    #
    # Since sheets cannot be rotated, the grid points are at:
    # (X0 + i*a, Y0 + j*b) for integers i,j
    #
    # We want to find X0 and Y0 such that:
    # 1) The two placed sheets' bottom-left corners are on grid points:
    #    (x1 - X0) % a == 0 and (y1 - Y0) % b == 0
    #    (x2 - X0) % a == 0 and (y2 - Y0) % b == 0
    #
    # 2) The grid covers the entire roof:
    #    The grid covers from X0 to X0 + n*a >= w
    #    and from Y0 to Y0 + m*b >= h
    #    for some integers n,m >= 1
    #
    # Since the sheets can extend beyond the roof, X0 can be negative or zero, similarly Y0.
    #
    # Approach:
    # - The conditions on X0:
    #   (x1 - X0) % a == 0 and (x2 - X0) % a == 0
    #   => (x1 - X0) % a == (x2 - X0) % a
    #   => x1 % a == x2 % a
    #   So the residues of x1 and x2 modulo a must be equal.
    #
    # - Similarly for Y0:
    #   (y1 - Y0) % b == 0 and (y2 - Y0) % b == 0
    #   => y1 % b == y2 % b
    #
    # If these conditions are not met, answer is "No".
    #
    # If they are met, we can pick X0 = x1 % a (or x2 % a), Y0 = y1 % b (or y2 % b).
    # Then check if the grid starting at X0, Y0 covers the entire roof.
    #
    # The grid covers from X0 to X0 + n*a >= w
    # and from Y0 to Y0 + m*b >= h
    #
    # Since X0 and Y0 are residues mod a and b respectively, they are in [0, a-1] and [0, b-1].
    # So the coverage length in x is from X0 to X0 + n*a, and in y from Y0 to Y0 + m*b.
    #
    # We need to find n,m such that:
    # X0 + n*a >= w
    # Y0 + m*b >= h
    #
    # n = ceil((w - X0)/a), m = ceil((h - Y0)/b)
    #
    # Since n,m >= 1, if w <= X0, n=0, but we need at least one sheet to cover the roof.
    # So if w <= X0, n=0 means no sheet covers the roof fully in x direction, so no.
    # Similarly for y.
    #
    # So check if n >= 1 and m >= 1.
    #
    # If yes, answer "Yes", else "No".

    if (x1 % a) != (x2 % a):
        return "No"
    if (y1 % b) != (y2 % b):
        return "No"

    X0 = x1 % a
    Y0 = y1 % b

    # Calculate n and m
    # If w <= X0, no sheet covers the roof fully in x direction
    if w > X0:
        n = (w - X0 + a - 1) // a
    else:
        n = 0

    if h > Y0:
        m = (h - Y0 + b - 1) // b
    else:
        m = 0

    if n >= 1 and m >= 1:
        return "Yes"
    else:
        return "No"


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w, h, a, b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    print(can_tile(w, h, a, b, x1, y1, x2, y2))