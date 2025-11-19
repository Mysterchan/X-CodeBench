from collections import defaultdict
from math import gcd

def solve(n, x, y):
    D = defaultdict(list)
    for i in range(n):
        xi, yi = x[i], y[i]
        for j in range(i+1, n):
            dx = x[j] - xi
            dy = y[j] - yi
            if dx == 0:
                key = (0, 1)  # vertical line slope
            else:
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0:
                    dx = -dx
                    dy = -dy
                key = (dx, dy)
            D[key].append((i, j))

    ans = 0
    for points in D.values():
        m = len(points)
        # Count combinations of pairs sharing no points efficiently
        # Use a frequency array to count how many pairs each point appears in
        freq = [0] * n
        for p, q in points:
            freq[p] += 1
            freq[q] += 1

        # Total pairs of pairs: m*(m-1)//2
        total_pairs = m * (m - 1) // 2

        # Subtract pairs that share a point
        # Number of pairs sharing a point = sum over points of freq[p]*(freq[p]-1)//2
        shared = 0
        for c in freq:
            if c > 1:
                shared += c * (c - 1) // 2

        ans += total_pairs - shared

    return ans

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    x, y = zip(*[map(int, input().split()) for _ in range(n)])
    print(solve(n, x, y))