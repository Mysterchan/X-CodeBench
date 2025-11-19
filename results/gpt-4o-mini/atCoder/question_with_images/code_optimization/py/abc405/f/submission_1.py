import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()
n, m = map(int, input().split())

# Read the segments
segments = []
for _ in range(m):
    A, B = map(int, input().split())
    segments.append((A, B))

q = int(input())
queries = []
for _ in range(q):
    C, D = map(int, input().split())
    queries.append((C, D))

# Create a mapping from odd points to the segments they touch
point_to_segments = defaultdict(list)
for index, (A, B) in enumerate(segments):
    point_to_segments[A].append(index)
    point_to_segments[B].append(index)

# Result for each query
results = []

for C, D in queries:
    count = 0
    if C > D:
        C, D = D, C  # Ensure C < D
    
    # Check segments connected to C and D
    for segment_index in point_to_segments[C]:
        A, B = segments[segment_index]
        # Count only those segments that do not share a point with (C, D)
        if A != D and B != D:
            count += 1
    
    for segment_index in point_to_segments[D]:
        A, B = segments[segment_index]
        # Ensure that we don't double count
        if A != C and B != C:
            count += 1

    results.append(count)

# Output the result for each query
sys.stdout.write("\n".join(map(str, results)) + "\n")