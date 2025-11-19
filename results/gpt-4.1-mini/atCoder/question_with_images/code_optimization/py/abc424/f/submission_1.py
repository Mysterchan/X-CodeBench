import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
ABs = [tuple(map(int, input().split())) for _ in range(Q)]

# Since all 2Q points are distinct, no two segments share endpoints.
# Two chords (A,B) and (C,D) intersect iff:
# A < C < B < D or C < A < D < B (assuming A < B and C < D)
# We can maintain the drawn chords sorted by their left endpoint.
# For each new chord (A,B), check if it intersects with any existing chord.
# Because chords are sorted by left endpoint, only the chord with the largest left endpoint less than A
# or the chord with the smallest left endpoint greater than A can intersect.
# We can use a balanced structure to store chords by their left endpoint.
# Since Python has no built-in balanced tree, we use bisect on a list.

import bisect

drawn = []  # list of (A,B), sorted by A

anss = []
for A, B in ABs:
    A -= 1
    B -= 1
    if A > B:
        A, B = B, A

    # Find position to insert (A,B)
    i = bisect.bisect_left(drawn, (A, B))

    intersect = False
    # Check chord before i
    if i > 0:
        A1, B1 = drawn[i-1]
        # Check intersection: A1 < A < B1 < B
        if A1 < A < B1 < B:
            intersect = True
    # Check chord at i
    if i < len(drawn):
        A2, B2 = drawn[i]
        # Check intersection: A < A2 < B < B2
        if A < A2 < B < B2:
            intersect = True

    if intersect:
        anss.append("No")
    else:
        anss.append("Yes")
        drawn.insert(i, (A, B))

print('\n'.join(anss))