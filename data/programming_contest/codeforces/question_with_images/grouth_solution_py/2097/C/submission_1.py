import math

def gcd(a, b):
    if b == 0: return (1, 0, a)
    x, y, d = gcd(b, a % b)
    return (y, x - (a // b) * y, d)

for _ in range(int(input())):
    n, x, y, vx, vy = map(int, input().split())
    c = vy * x - vx * y
    if c % n:
        print(-1); continue
    c //= n
    a, b, d = gcd(vy, vx)
    if c % d:
        print(-1); continue
    p, q = a * c // d, -b * c // d
    sp, sq = vx // d, vy // d
    k = max(math.ceil((1 - p) / sp), math.ceil((1 - q) / sq))
    p += sp * k; q += sq * k
    s = p + q
    print(s + s // 2 + abs(p - q) // 2 - 2)
