import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Sort points on both lines
    a.sort()
    b.sort()

    # Maximum number of operations is limited by how many triples we can form:
    # Each operation removes 3 points, and we need at least 1 point from y=0 and 2 points from y=2 or vice versa.
    # Since points are distinct and on two lines, the only way to form a non-collinear triangle is:
    # - 1 point from one line and 2 points from the other line.
    # Because points on the same line are collinear.
    #
    # So each triangle must be formed by either:
    # - 1 point from y=0 and 2 points from y=2, or
    # - 2 points from y=0 and 1 point from y=2.
    #
    # The maximum number of operations k_max is min(n//2, m) + min(m//2, n)
    # because:
    # - min(n//2, m) is max triangles with 2 points from y=0 and 1 from y=2
    # - min(m//2, n) is max triangles with 2 points from y=2 and 1 from y=0
    #
    # We want to find f(k) for k=1..k_max, where f(k) is max score after exactly k operations.

    # Precompute prefix sums for a and b to quickly calculate sums of intervals
    # We'll need sums of pairs of points to calculate max area triangles.

    # To maximize area of triangle formed by points (x1,0), (x2,0), (y,2):
    # Area = |x2 - x1| * 2 / 2 = |x2 - x1|
    # Similarly for (x,0), (y1,2), (y2,2):
    # Area = |y2 - y1| * 2 / 2 = |y2 - y1|
    #
    # So the area depends only on the horizontal distance between the two points on the same line.
    #
    # So for triangles with 2 points on y=0 and 1 on y=2:
    # Area = |a_j - a_i| for some i<j
    #
    # For triangles with 2 points on y=2 and 1 on y=0:
    # Area = |b_j - b_i| for some i<j
    #
    # To maximize total area for k operations, we want to pick the k largest distances on y=0 line (for 2 points)
    # and the k largest distances on y=2 line (for 2 points).
    #
    # But we must also consider the number of points available on the other line to form triangles.
    #
    # So:
    # - For 2 points on y=0 and 1 on y=2: max number of such triangles = min(n//2, m)
    # - For 2 points on y=2 and 1 on y=0: max number of such triangles = min(m//2, n)
    #
    # We can form these two sets of triangles independently and then merge results to get f(k).

    # Calculate all possible distances between pairs on y=0 (a)
    dist_a = []
    for i in range(n - 1):
        dist_a.append(a[i+1] - a[i])
    dist_a.sort(reverse=True)

    # Calculate all possible distances between pairs on y=2 (b)
    dist_b = []
    for i in range(m - 1):
        dist_b.append(b[i+1] - b[i])
    dist_b.sort(reverse=True)

    # Prefix sums of distances for quick sum calculation
    prefix_a = [0]
    for d in dist_a:
        prefix_a.append(prefix_a[-1] + d)

    prefix_b = [0]
    for d in dist_b:
        prefix_b.append(prefix_b[-1] + d)

    # Maximum number of operations
    max_ops_a = min(n // 2, m)  # triangles with 2 points from a and 1 from b
    max_ops_b = min(m // 2, n)  # triangles with 2 points from b and 1 from a
    k_max = max_ops_a + max_ops_b

    if k_max == 0:
        print(0)
        continue

    # We want to find f(k) for k=1..k_max
    # f(k) = max sum of areas of k triangles
    # Each triangle area is a distance from dist_a or dist_b
    #
    # We can pick x triangles from dist_a and k-x from dist_b, where:
    # 0 <= x <= max_ops_a
    # 0 <= k-x <= max_ops_b
    #
    # For each k, try all valid x and pick max sum:
    # f(k) = max_{x} (sum of top x distances from dist_a + sum of top (k-x) distances from dist_b)

    # To do this efficiently, we precompute prefix sums and then for each k:
    # iterate x from max(0, k - max_ops_b) to min(k, max_ops_a)
    # and compute prefix_a[x] + prefix_b[k-x]

    res = []
    for k in range(1, k_max + 1):
        best = 0
        start_x = max(0, k - max_ops_b)
        end_x = min(k, max_ops_a)
        for x in range(start_x, end_x + 1):
            val = prefix_a[x] + prefix_b[k - x]
            if val > best:
                best = val
        res.append(best)

    print(k_max)
    print(*res)