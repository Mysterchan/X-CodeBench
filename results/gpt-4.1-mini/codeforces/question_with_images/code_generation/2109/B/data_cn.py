import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, a, b = map(int, input().split())
    # Mouf wants to minimize rounds, Fouad wants to maximize.
    # Each round Mouf cuts along a row or column line, discarding the part without the monster.
    # Fouad can then move the monster anywhere in the remaining grid.
    #
    # The game ends when only one cell remains.
    #
    # Key insight:
    # - Mouf can cut either horizontally or vertically.
    # - Fouad can move the monster anywhere in the remaining grid after the cut.
    #
    # To minimize rounds, Mouf wants to reduce the grid size as fast as possible.
    # To maximize rounds, Fouad wants to keep the grid as large as possible.
    #
    # After each cut, the dimension along which the cut was made reduces.
    # Fouad can move the monster to the part that is largest (to maximize rounds).
    #
    # The minimal number of rounds is the minimal number of cuts needed to reduce the grid to 1x1,
    # assuming Fouad always moves the monster to the larger part.
    #
    # The problem reduces to:
    # Given initial grid n x m and monster at (a,b),
    # the number of rounds = max(
    #   max(a-1, n - a),  # max distance to top or bottom edge
    #   max(b-1, m - b)   # max distance to left or right edge
    # )
    #
    # Explanation:
    # - Mouf cuts to isolate the monster in a smaller subgrid.
    # - Fouad moves the monster to the largest possible subgrid after the cut.
    # - The number of rounds equals the maximum number of cuts needed to reduce either
    #   the row dimension or the column dimension to 1.
    #
    # Each cut reduces either rows or columns by at least 1.
    # The worst case is the maximum distance from the monster to an edge.
    #
    # This matches the sample outputs.

    ans = max(max(a - 1, n - a), max(b - 1, m - b))
    print(ans)