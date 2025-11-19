def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read N and M
    N, M = map(int, data[0].split())
    
    # Read segments
    segments = []
    for i in range(1, M + 1):
        A, B = map(int, data[i].split())
        segments.append((A, B))
    
    # Read number of queries
    Q = int(data[M + 1])
    
    # Read queries
    queries = []
    for i in range(M + 2, M + 2 + Q):
        C, D = map(int, data[i].split())
        queries.append((C, D))
    
    # Create a mapping from even points to their segments
    point_to_segment = {}
    for index, (A, B) in enumerate(segments):
        point_to_segment[A] = index
        point_to_segment[B] = index
    
    results = []
    
    # Process each query
    for C, D in queries:
        count = 0
        # Check the segments that C and D would intersect
        for point in (C, D):
            if point in point_to_segment:
                count += 1
        results.append(count)
    
    # Output results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()