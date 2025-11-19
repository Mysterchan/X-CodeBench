def count_intersections(N, M, segments, Q, queries):
    def normalize(a, b):
        if a > b:
            a, b = b, a
        return a, b

    def intersects(seg1, seg2):
        a1, b1 = seg1
        a2, b2 = seg2
        return (a1 < a2 < b1) != (a1 < b2 < b1) and (a2 < a1 < b2) != (a2 < b1 < b2)

    results = []
    for c, d in queries:
        count = 0
        for a, b in segments:
            if intersects(normalize(c, d), (a, b)):
                count += 1
        results.append(count)
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
segments = [tuple(map(int, line.split())) for line in data[1:M + 1]]
Q = int(data[M + 1])
queries = [tuple(map(int, line.split())) for line in data[M + 2:M + 2 + Q]]

results = count_intersections(N, M, segments, Q, queries)
print('\n'.join(map(str, results)))