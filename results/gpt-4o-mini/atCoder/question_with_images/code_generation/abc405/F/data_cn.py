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
    
    # Read queries
    Q = int(data[M + 1])
    queries = []
    for i in range(M + 2, M + 2 + Q):
        C, D = map(int, data[i].split())
        queries.append((C, D))
    
    # Create a mapping from even points to their segments
    point_to_segments = {}
    for index, (A, B) in enumerate(segments):
        if A not in point_to_segments:
            point_to_segments[A] = []
        if B not in point_to_segments:
            point_to_segments[B] = []
        point_to_segments[A].append(index)
        point_to_segments[B].append(index)
    
    # Process each query
    results = []
    for C, D in queries:
        shared_segments = set()
        
        # Find segments for C and D
        if C in point_to_segments:
            shared_segments.update(point_to_segments[C])
        if D in point_to_segments:
            shared_segments.update(point_to_segments[D])
        
        # Count the number of unique segments that are shared
        results.append(len(shared_segments))
    
    # Print results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()