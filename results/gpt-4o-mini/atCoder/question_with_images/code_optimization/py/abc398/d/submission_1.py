import sys

input = lambda: sys.stdin.readline().rstrip()

def solve():
    n, r, c = map(int, input().split())
    s = input()

    # Coordinate of smoke initially at (0, 0)
    smoke_pos = (0, 0)

    # Directions mapping
    direction = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

    # Result string initialization
    result = []

    # Track the smoke positions
    smoke_set = set()
    smoke_set.add(smoke_pos)

    for i in range(n):
        # Shift smoke positions according to the direction
        new_smoke_set = set()
        move = direction[s[i]]

        for (x, y) in smoke_set:
            new_pos = (x + move[0], y + move[1])
            new_smoke_set.add(new_pos)

        smoke_set = new_smoke_set

        # If the position of the smoke contains the target position (r, c)
        if (r, c) in smoke_set:
            result.append('1')
        else:
            result.append('0')

        # If there's no smoke at (0, 0), add new smoke there
        if (0, 0) not in smoke_set:
            smoke_set.add((0, 0))

    print("".join(result))

if __name__ == "__main__":
    solve()