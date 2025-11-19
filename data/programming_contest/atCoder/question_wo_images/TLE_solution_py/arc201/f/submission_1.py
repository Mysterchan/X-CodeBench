def cocoa():
  n = int(input())
  x = xy = xyz = yz = z = y = xz = 0
  for _ in range(n):
    a, b, c, d, e = map(int, input().split())
    x += min(a,b,c)
    y += min(b,c,d)
    z += min(c,d,e)
    xy += min(a+d,b,c)
    yz += min(e+b,d,c)
    xz += min(min(a,b)+min(d,e),c)
    xyz += min(a + d,b + e,c,b + d)
    print(min(x, xy // 2, xyz // 3, yz // 2, z, y, xz // 2), end=' ')
  print()

T = int(input())
for _ in range(T):
    cocoa()