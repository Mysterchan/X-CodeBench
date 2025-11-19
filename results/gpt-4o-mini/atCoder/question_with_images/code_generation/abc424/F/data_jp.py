def can_draw_segments(N, queries):
    results = []
    segments = []

    for A, B in queries:
        if A > B:
            A, B = B, A
        
        # Check if the new segment intersects with any existing segments
        intersects = False
        for (C, D) in segments:
            if (A < C < B < D) or (C < A < D < B):
                intersects = True
                break
        
        if intersects:
            results.append("No")
        else:
            results.append("Yes")
            segments.append((A, B))
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

N, Q = map(int, data[0].split())
queries = [tuple(map(int, line.split())) for line in data[1:Q + 1]]

results = can_draw_segments(N, queries)
print("\n".join(results))