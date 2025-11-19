n = int(input())

for i in range(n):
    row = []
    for j in range(n):
        # Determine the distance from the edge
        dist = min(i, j, n - 1 - i, n - 1 - j)
        # If distance is even, it's '#', otherwise '.'
        row.append('#' if dist % 2 == 0 else '.')
    print(''.join(row))