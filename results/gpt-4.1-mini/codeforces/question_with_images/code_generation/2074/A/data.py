t = int(input())
for _ in range(t):
    l, r, d, u = map(int, input().split())
    # The points are (-l,0), (r,0), (0,-d), (0,u)
    # For these points to form a square:
    # 1. All sides must be equal.
    # 2. All angles are 90 degrees (which is guaranteed by the axis-aligned points).
    # Since points lie on axes, the shape is a square if and only if l == r == d == u.
    if l == r == d == u:
        print("Yes")
    else:
        print("No")