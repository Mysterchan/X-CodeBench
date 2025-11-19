def solve():
    n = int(input())
    x = xy = xyz = yz = z = y = xz = 0
    results = []
    
    for _ in range(n):
        a, b, c, d, e = map(int, input().split())
        
        # Update cumulative values
        x += min(a, b, c)
        y += min(b, c, d)
        z += min(c, d, e)
        xy += min(a + d, b, c)
        yz += min(e + b, d, c)
        xz += min(min(a, b) + min(d, e), c)
        xyz += min(a + d, b + e, c, b + d)
        
        # Calculate answer for current k
        results.append(str(min(x, xy // 2, xyz // 3, yz // 2, z, y, xz // 2)))
    
    print(' '.join(results))

T = int(input())
for _ in range(T):
    solve()