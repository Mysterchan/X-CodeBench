def get_position(n, d):
    size = 2 ** n
    d -= 1  # Convert to 0-based index
    x, y = 0, 0
    while n > 0:
        quadrant_size = (size // 2) ** 2
        if d < quadrant_size:  # Top-left
            pass
        elif d < 2 * quadrant_size:  # Top-right
            y += size // 2
            d -= quadrant_size
        elif d < 3 * quadrant_size:  # Bottom-left
            x += size // 2
            d -= 2 * quadrant_size
        else:  # Bottom-right
            x += size // 2
            y += size // 2
            d -= 3 * quadrant_size
        n -= 1
        size //= 2
    return x + 1, y + 1  # Convert back to 1-based index

def get_value(n, x, y):
    size = 2 ** n
    x -= 1  # Convert to 0-based index
    y -= 1
    value = 0
    while n > 0:
        quadrant_size = (size // 2) ** 2
        if x < size // 2 and y < size // 2:  # Top-left
            pass
        elif x < size // 2 and y >= size // 2:  # Top-right
            value += quadrant_size
            y -= size // 2
        elif x >= size // 2 and y < size // 2:  # Bottom-left
            value += 2 * quadrant_size
            x -= size // 2
        else:  # Bottom-right
            value += 3 * quadrant_size
            x -= size // 2
            y -= size // 2
        n -= 1
        size //= 2
    return value + 1  # Convert back to 1-based index

import sys
input = sys.stdin.read
data = input().splitlines()

index = 0
t = int(data[index])
index += 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    q = int(data[index])
    index += 1

    for __ in range(q):
        query = data[index].split()
        index += 1
        if query[0] == '->':
            x, y = int(query[1]), int(query[2])
            results.append(get_value(n, x, y))
        else:  # '<-'
            d = int(query[1])
            results.append(' '.join(map(str, get_position(n, d))))

print('\n'.join(map(str, results)))