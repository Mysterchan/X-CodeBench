import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    s = input().strip()

    # Convert to 0-based index
    x -= 1

    # Find nearest wall to the left of x
    left_wall = -1
    for i in range(x - 1, -1, -1):
        if s[i] == '#':
            left_wall = i
            break

    # Find nearest wall to the right of x
    right_wall = n
    for i in range(x + 1, n):
        if s[i] == '#':
            right_wall = i
            break

    # Distance to left wall (or edge if no wall)
    dist_left = x - left_wall - 1 if left_wall != -1 else x
    # Distance to right wall (or edge if no wall)
    dist_right = right_wall - x - 1 if right_wall != n else n - x - 1

    # Mani tries to maximize days, so he will build walls to force Hamid to take the longer path
    # Hamid tries to minimize days, so he will choose the shorter path to escape

    # The number of days needed is the minimal number of walls Hamid must destroy to escape,
    # plus the initial day when Mani builds a wall (except if Hamid can escape immediately)

    # If Hamid can escape immediately (no wall on one side), days = 1
    if left_wall == -1 or right_wall == n:
        print(1)
        continue

    # Otherwise, Mani will build a wall on the side with smaller distance to force Hamid to go the other way
    # So the answer is max(dist_left, dist_right) + 1
    # +1 because Mani builds a wall each day, and Hamid destroys one wall per day and moves there

    print(max(dist_left, dist_right) + 1)