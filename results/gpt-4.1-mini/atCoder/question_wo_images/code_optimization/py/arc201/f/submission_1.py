import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    x = y = z = xy = yz = xz = xyz = 0
    res = []
    for __ in range(n):
        a,b,c,d,e = map(int, input().split())
        x += min(a,b,c)
        y += min(b,c,d)
        z += min(c,d,e)
        xy += min(a+d,b,c)
        yz += min(e+b,d,c)
        xz += min(a,b) + min(d,e)
        xyz += min(a + d,b + e,c,b + d)
        # The original code divides xz by 2, but since xz is sum of min(a,b)+min(d,e),
        # and original code does integer division by 2, we do the same here.
        # So xz//2 instead of xz
        res.append(str(min(x, xy//2, xyz//3, yz//2, z, y, xz//2)))
    print(' '.join(res))