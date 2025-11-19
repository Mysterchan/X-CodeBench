def count_intersections(N, M, lines):
    def intersects(a1, b1, a2, b2):
        return (a1 < a2 < b1) != (a1 < b2 < b1)

    count = 0
    for i in range(M):
        a1, b1 = lines[i]
        for j in range(i + 1, M):
            a2, b2 = lines[j]
            if intersects(a1, b1, a2, b2):
                count += 1

    return count

import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
lines = [tuple(map(int, line.split())) for line in data[1:M + 1]]

result = count_intersections(N, M, lines)
print(result)