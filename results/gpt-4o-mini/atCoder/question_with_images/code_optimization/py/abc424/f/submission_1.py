import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# To keep track of drawn segments
drawn_segments = []

def does_intersect(a1, b1, a2, b2):
    return (a1 < a2 < b1) != (a1 < b2 < b1)

results = []
for A, B in queries:
    A, B = A - 1, B - 1  # Convert to 0-based index
    can_draw = True
    
    for (d1, d2) in drawn_segments:
        if does_intersect(A, B, d1, d2):
            can_draw = False
            break
    
    results.append("Yes" if can_draw else "No")
    
    if can_draw:
        drawn_segments.append((A, B))

print('\n'.join(results))