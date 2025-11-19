def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    M = int(data[idx + 1])
    idx += 2
    
    segments = []
    for _ in range(M):
        A = int(data[idx])
        B = int(data[idx + 1])
        segments.append((A, B))
        idx += 2
    
    Q = int(data[idx])
    idx += 1
    
    queries = []
    for _ in range(Q):
        C = int(data[idx])
        D = int(data[idx + 1])
        queries.append((C, D))
        idx += 2
    
    # Create a mapping of segments to their endpoints
    segment_map = {}
    for i, (A, B) in enumerate(segments):
        segment_map[(A, B)] = i
    
    results = []
    
    for C, D in queries:
        count = 0
        for A, B in segments:
            if (C < A < D) or (C < B < D) or (A < C < B) or (A < D < B):
                count += 1
        results.append(count)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()