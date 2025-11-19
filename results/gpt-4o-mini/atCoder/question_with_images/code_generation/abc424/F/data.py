def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, Q = map(int, data[0].split())
    queries = [tuple(map(int, line.split())) for line in data[1:Q + 1]]
    
    drawn_segments = []
    results = []
    
    for A, B in queries:
        # Ensure A < B for easier processing
        if A > B:
            A, B = B, A
        
        intersects = False
        for (C, D) in drawn_segments:
            # Check if (A, B) intersects with (C, D)
            if (A < C < B < D) or (C < A < D < B) or (A < D < B < C) or (C < B < D < A):
                intersects = True
                break
        
        if intersects:
            results.append("No")
        else:
            results.append("Yes")
            drawn_segments.append((A, B))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()