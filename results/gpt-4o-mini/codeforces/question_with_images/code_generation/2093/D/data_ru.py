def answer_queries(t, data_sets):
    results = []
    
    for n, queries in data_sets:
        size = 1 << n  # 2^n
        for query in queries:
            if query[0] == "->":
                x, y = query[1] - 1, query[2] - 1  # Convert to 0-based indexing
                results.append(get_value(x, y, size))
            else:  # "<-"
                d = query[1]
                results.append(get_coordinates(d, size))

    return results

def get_value(x, y, size):
    # Calculate the value at (x, y) in the n-th sized grid.
    original_x, original_y = x, y
    value = 1
    while size > 2:
        half_size = size >> 1  # Integer division by 2
        if x < half_size and y < half_size:  # Top left
            pass  # Do nothing
        elif x < half_size and y >= half_size:  # Top right
            value += (half_size * half_size)  # Skip top left
            y -= half_size
        elif x >= half_size and y < half_size:  # Bottom left
            value += 2 * (half_size * half_size)  # Skip top left and top right
            x -= half_size
        else:  # Bottom right
            value += 3 * (half_size * half_size)  # Skip all previous squares
            x -= half_size
            y -= half_size
        size = half_size

    # Now handle the 2x2 base case
    if x == 0 and y == 0:
        return value  # (1)
    elif x == 0 and y == 1:
        return value + 3  # (4)
    elif x == 1 and y == 0:
        return value + 2  # (3)
    elif x == 1 and y == 1:
        return value + 1  # (2)

def get_coordinates(d, size):
    # Calculate the coordinates of the value d in the n-th sized grid.
    value = d
    x, y = 0, 0
    while size > 2:
        half_size = size >> 1  # Integer division by 2
        if value <= half_size * half_size:
            # Top left
            pass  # Do nothing
        elif value <= 2 * (half_size * half_size):
            value -= (half_size * half_size)
            y += half_size  # Top right
        elif value <= 3 * (half_size * half_size):
            value -= 2 * (half_size * half_size)
            x += half_size  # Bottom left
        else:
            value -= 3 * (half_size * half_size)
            x += half_size  # Bottom right
            y += half_size
        size = half_size

    # Now handle the 2x2 base case
    if value == 1:
        return (x + 1, y + 1)  # (1)
    elif value == 2:
        return (x + 2, y + 2)  # (2)
    elif value == 3:
        return (x + 2, y + 1)  # (3)
    elif value == 4:
        return (x + 1, y + 2)  # (4)

import sys
input = sys.stdin.read

def main():
    data = input().strip().splitlines()
    index = 0
    t = int(data[index])
    index += 1
    data_sets = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        q = int(data[index])
        index += 1
        queries = []
        for __ in range(q):
            parts = data[index].split()
            if parts[0] == '->':
                queries.append((parts[0], int(parts[1]), int(parts[2])))
            else:
                queries.append((parts[0], int(parts[1])))
            index += 1
        data_sets.append((n, queries))
    
    results = answer_queries(t, data_sets)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()