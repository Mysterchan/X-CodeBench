import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    k -= 1  # zero-based index

    max_h = max(h)
    max_indices = [i for i, height in enumerate(h) if height == max_h]

    # If starting tower is already max height, answer YES
    if h[k] == max_h:
        print("YES")
        continue

    # We want to check if there exists a max height tower j such that:
    # We can teleport from k to j starting at time 0, taking |h[k]-h[j]| seconds,
    # and arrive at tower j at time |h[k]-h[j]|, before water level > h[j].
    # Water level at arrival time t is t+1.
    # Condition: t+1 <= h[j] => |h[k]-h[j]| + 1 <= h[j] => |h[k]-h[j]| <= h[j] - 1

    # Since h[j] = max_h, check if |h[k] - max_h| <= max_h - 1
    # If yes, print YES, else NO

    dist = abs(h[k] - max_h)
    if dist <= max_h - 1:
        print("YES")
    else:
        print("NO")