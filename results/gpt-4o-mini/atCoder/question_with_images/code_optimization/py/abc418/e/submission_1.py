from collections import defaultdict
from math import gcd

def solve(n, x, y):
    D = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            if dx < 0:
                dx, dy = -dx, -dy
            elif dx == 0:
                dy = abs(dy)
            g = gcd(dx, dy)
            key = (dx // g, dy // g)
            D[key].append((i, j))
    
    count = 0
    for points in D.values():
        m = len(points)
        if m < 2:
            continue
        count += m * (m - 1) // 2 * (n - 2)  # Choose 2 lines, then choose 2 other points
    
    return count

if __name__ == "__main__":
    n = int(input())
    x, y = zip(*[map(int, input().split()) for _ in range(n)])
    print(solve(n, x, y))