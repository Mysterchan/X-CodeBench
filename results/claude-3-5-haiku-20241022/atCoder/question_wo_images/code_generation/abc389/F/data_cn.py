import sys
from bisect import bisect_left, bisect_right

def solve():
    input = sys.stdin.read().split()
    idx = 0
    
    N = int(input[idx])
    idx += 1
    
    contests = []
    for _ in range(N):
        L = int(input[idx])
        R = int(input[idx + 1])
        contests.append((L, R))
        idx += 2
    
    Q = int(input[idx])
    idx += 1
    
    queries = []
    for _ in range(Q):
        X = int(input[idx])
        queries.append(X)
        idx += 1
    
    # Create events for rating changes
    events = []
    for L, R in contests:
        events.append((L, 1))  # Start of range
        events.append((R + 1, -1))  # End of range (exclusive)
    
    events.sort()
    
    # Build cumulative increase array
    rating_points = []
    current_increase = 0
    
    for rating, delta in events:
        if not rating_points or rating_points[-1][0] != rating:
            rating_points.append([rating, current_increase])
        current_increase += delta
    
    # Process queries
    results = []
    for X in queries:
        final_rating = X
        
        for _ in range(N):
            # Find how many contests increase the rating at current rating
            pos = bisect_right(rating_points, [final_rating, float('inf')]) - 1
            if pos >= 0:
                increases = rating_points[pos][1]
                if increases > 0:
                    final_rating += 1
        
        results.append(final_rating)
    
    for r in results:
        print(r)

solve()