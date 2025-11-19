import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# We will maintain a stack of drawn segments.
# Each segment is represented as (start, end) with start < end.
# The segments drawn do not intersect if and only if their intervals are nested or disjoint in a non-crossing manner.
# The problem reduces to checking if the new segment crosses any existing segment.
# 
# Key insight:
# Two chords (a,b) and (c,d) (with a < b and c < d) intersect if and only if:
# a < c < b < d or c < a < d < b
#
# Since all points are distinct and no endpoints overlap, we can maintain a stack of segments sorted by their start points.
# When adding a new segment (a,b), we pop from the stack all segments whose end is less than b,
# because these segments are nested inside the new segment and do not cause intersection.
# If after popping, the top segment on the stack intersects with the new segment, we cannot add it.
# Otherwise, we add the new segment to the stack.
#
# This approach works because the segments form a non-crossing set of chords on a circle,
# and the stack maintains a structure similar to a "monotonic" chain of intervals.

stack = []

for _ in range(Q):
    a, b = map(int, input().split())
    # Ensure a < b
    if a > b:
        a, b = b, a

    # Pop segments that end before b
    while stack and stack[-1][1] < b:
        stack.pop()

    # Check intersection with top segment if exists
    if stack:
        top_a, top_b = stack[-1]
        # Check if (a,b) intersects with (top_a, top_b)
        # Intersection condition:
        # a < top_a < b < top_b or top_a < a < top_b < b
        if (a < top_a < b < top_b) or (top_a < a < top_b < b):
            print("No")
            continue

    # No intersection, add segment
    stack.append((a, b))
    print("Yes")