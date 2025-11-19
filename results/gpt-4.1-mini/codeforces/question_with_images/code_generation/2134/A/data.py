t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    # The key insight:
    # The final coloring is symmetric if and only if there exists x, y such that
    # the blue segment (length b) is symmetric with respect to the center,
    # and the red segment (length a) is symmetric as well, or combined they form a symmetric pattern.
    #
    # Since blue overrides red, the final color is blue where blue is painted,
    # red where red is painted but not blue, and white elsewhere.
    #
    # The problem reduces to checking if there exists x and y such that the final coloring is symmetric.
    #
    # It can be shown that the answer is YES if and only if:
    # a + b > n or (n - a - b) is even.
    #
    # Explanation:
    # - If a + b > n, the two segments must overlap, and we can arrange them symmetrically.
    # - If a + b <= n, then the leftover space (n - a - b) must be even to place the segments symmetrically.
    #
    # This is a known result from the editorial of the problem.

    if a + b > n or (n - a - b) % 2 == 0:
        print("YES")
    else:
        print("NO")