import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    s = input().strip()

    # Count fixed Rs and Ds
    rr = s.count('R')
    dd = s.count('D')

    # Remaining Rs and Ds to assign to '?'
    r = w - 1 - rr
    d = h - 1 - dd

    # The maximum black cells painted is:
    # total cells on the grid (h*w)
    # minus the cells that cannot be painted black.
    # The unreachable cells are those beyond the forced moves.
    # The formula derived from problem editorial:
    # answer = h + w - 1 + r * d
    # Explanation:
    # - h + w - 1 is the length of the path (cells visited in one path)
    # - r * d is the number of additional cells painted by combining different paths
    #   due to '?' choices.

    ans = h + w - 1 + r * d
    print(ans)