def intersects(a1, b1, a2, b2):
    if a1 > b1:
        a1, b1 = b1, a1
    if a2 > b2:
        a2, b2 = b2, a2
    return (a1 < a2 < b1) ^ (a1 < b2 < b1)

import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
Q = int(data[1])

results = []
segments = []

for i in range(Q):
    A = int(data[2 + 2 * i])
    B = int(data[3 + 2 * i])
    
    # Ensure A is less than B for simplicity
    if A > B:
        A, B = B, A
        
    can_draw = True
    for seg in segments:
        if intersects(A, B, seg[0], seg[1]):
            can_draw = False
            break
            
    if can_draw:
        results.append("Yes")
        segments.append((A, B))
    else:
        results.append("No")

print("\n".join(results))