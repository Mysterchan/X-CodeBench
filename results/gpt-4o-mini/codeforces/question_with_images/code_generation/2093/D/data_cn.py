def calculate_position(n, x, y):
    size = 1 << n  # 2^n
    x -= 1  # To convert to 0-based index
    y -= 1  # To convert to 0-based index
    
    idx = 0
    while size > 2:
        size //= 2
        if x < size and y < size:
            idx += 0 * size * size
        elif x < size and y >= size:
            idx += 1 * size * size
            y -= size
        elif x >= size and y < size:
            idx += 2 * size * size
            x -= size
        else:
            idx += 3 * size * size
            x -= size
            y -= size
    
    idx += (x * 2 + y + 1)
    return idx + 1  # Adjust for 1-based index


def calculate_coordinates(n, d):
    size = 1 << n  # 2^n
    d -= 1  # Convert to 0-based
    d_pos = 0
    
    while size > 2:
        size //= 2
        if d < size * size:
            pass  # stays in the same top-left quadrant
        elif d < 2 * size * size:
            d_pos += size * size
            d -= size * size
        elif d < 3 * size * size:
            d_pos += 2 * size * size
            d -= 2 * size * size
        else:
            d_pos += 3 * size * size
            d -= 3 * size * size
    
    x = d_pos // 2
    y = d_pos % 2
    return (x + 1, y + 1)  # Convert back to 1-based index


def process_cases(t, cases):
    results = []
    for _ in range(t):
        n = cases.pop(0)
        q = cases.pop(0)
        for __ in range(q):
            query = cases.pop(0).split()
            if query[0] == "->":
                x = int(query[1])
                y = int(query[2])
                results.append(calculate_position(n, x, y))
            else:  # "<-"
                d = int(query[1])
                results.append(" ".join(map(str, calculate_coordinates(n, d))))
    return results


t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    cases.append(n)
    q = int(input())
    cases.append(q)
    for __ in range(q):
        cases.append(input().strip())

results = process_cases(t, cases)
print("\n".join(map(str, results)))