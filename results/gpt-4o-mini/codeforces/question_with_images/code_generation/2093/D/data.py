def get_position(n, d):
    size = 2 ** n
    d -= 1  # to convert to 0-indexed
    x, y = 0, 0
    quadrant_size = size * size // 4

    for _ in range(n):
        if d < quadrant_size:
            # Top-left (0, 0)
            pass
        elif d < 2 * quadrant_size:
            # Top-right (0, 1)
            y += size // 2
            d -= quadrant_size
        elif d < 3 * quadrant_size:
            # Bottom-left (1, 0)
            x += size // 2
            d -= 2 * quadrant_size
        else:
            # Bottom-right (1, 1)
            x += size // 2
            y += size // 2
            d -= 3 * quadrant_size
        size //= 2
        quadrant_size //= 4

    return (x + 1, y + 1)  # convert to 1-indexed

def get_value(n, x, y):
    size = 2 ** n
    x -= 1  # to convert to 0-indexed
    y -= 1  # to convert to 0-indexed
    result = 0
    quadrant_size = size * size // 4

    for _ in range(n):
        if x < size // 2 and y < size // 2:
            # Top-left (0, 0)
            pass
        elif x < size // 2 and y >= size // 2:
            # Top-right (0, 1)
            result += quadrant_size
            y -= size // 2
        elif x >= size // 2 and y < size // 2:
            # Bottom-left (1, 0)
            result += 2 * quadrant_size
            x -= size // 2
        else:
            # Bottom-right (1, 1)
            result += 3 * quadrant_size
            x -= size // 2
            y -= size // 2
        
        size //= 2
        quadrant_size //= 4

    return result + 1  # convert back to 1-indexed

def process_queries(n, queries):
    results = []
    for query in queries:
        if query[0] == '->':
            x, y = map(int, query[1:])
            results.append(get_value(n, x, y))
        elif query[0] == '<-':
            d = int(query[1])
            results.append(get_position(n, d))
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    outputs = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        q = int(data[idx])
        idx += 1
        queries = []
        
        for _ in range(q):
            queries.append(data[idx].split())
            idx += 1
            
        results = process_queries(n, queries)
        
        for result in results:
            if isinstance(result, int):
                outputs.append(str(result))
            else:
                outputs.append(f"{result[0]} {result[1]}")

    print("\n".join(outputs))

if __name__ == "__main__":
    main()