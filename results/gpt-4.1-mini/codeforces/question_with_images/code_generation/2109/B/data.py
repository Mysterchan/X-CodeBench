import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, a, b = map(int, input().split())
    # Mouf wants to minimize turns, Fouad wants to maximize turns.
    # Each turn Mouf cuts along a row or column line, discarding the part without the monster.
    # Fouad then moves the monster anywhere in the remaining grid.
    #
    # The key insight:
    # Mouf can cut either horizontally or vertically.
    # Fouad will move the monster to maximize the number of turns.
    #
    # The minimal number of turns is the minimal number of cuts needed to reduce the grid to 1x1.
    # But since Fouad can move the monster anywhere in the remaining grid after each cut,
    # he can always move it to the largest remaining part to maximize the number of turns.
    #
    # The optimal strategy for Mouf is to always cut the larger dimension.
    # Fouad will move the monster to the larger half to maximize turns.
    #
    # Turns needed = (number of cuts to reduce rows to 1) + (number of cuts to reduce columns to 1)
    # Because Mouf can alternate cuts between rows and columns, but Fouad can always move the monster
    # to the larger half, so the number of turns is the sum of the number of cuts needed for rows and columns.
    #
    # Number of cuts to reduce rows from n to 1 = n - 1
    # Number of cuts to reduce columns from m to 1 = m - 1
    #
    # But since Fouad can move the monster anywhere, Mouf can only reduce one dimension by 1 per turn.
    # So total turns = (n - 1) + (m - 1) = n + m - 2

    print(n + m - 2)