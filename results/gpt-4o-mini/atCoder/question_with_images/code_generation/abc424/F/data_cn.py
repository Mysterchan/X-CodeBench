def is_intersecting(a1, b1, a2, b2):
    # Check if the segments (a1, b1) and (a2, b2) intersect
    if a1 > b1:
        a1, b1 = b1, a1
    if a2 > b2:
        a2, b2 = b2, a2
    return (a1 < a2 < b1) or (a1 < b2 < b1) or (a2 < a1 < b2) or (a2 < b1 < b2)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, Q = map(int, data[0].split())
    queries = [tuple(map(int, line.split())) for line in data[1:Q + 1]]
    
    drawn_segments = []
    results = []
    
    for a, b in queries:
        can_draw = True
        for (x, y) in drawn_segments:
            if is_intersecting(a, b, x, y):
                can_draw = False
                break
        if can_draw:
            results.append("Yes")
            drawn_segments.append((a, b))
        else:
            results.append("No")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()