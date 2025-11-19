from collections import defaultdict
from math import gcd

INF = 10**10

def solve(n, x, y):
    D = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            if dx < 0:
                dx, dy = -dx, -dy

            if dx == 0:
                key = INF
            else:
                g = gcd(dx, dy)
                key = (dx//g, dy//g)
            D[key].append((i, j))

    S = set()
    for points in D.values():
        m = len(points)
        for i in range(m):
            p, q = points[i]
            for j in range(i+1, m):
                r, s = points[j]
                S.add(tuple(sorted([p, r, q, s])))
    return len(S)

if __name__ == "__main__":
    n = int(input())
    x, y = zip(*[map(int, input().split()) for i in range(n)])
    print(solve(n, x, y))