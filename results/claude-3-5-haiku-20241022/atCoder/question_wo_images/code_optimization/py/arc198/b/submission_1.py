T = int(input())
for _ in range(T):
    x, y, z = map(int, input().split())
    n02 = z * 2
    n00 = x + z - n02
    if n00 < 0:
        print('No')
        continue
    # Reduce excess 0-positions by pairing with 1's (each pair of 1's uses one 0-position)
    if n00 > 0:
        pairs = min(n00, y // 2)
        y -= pairs * 2
        n00 -= pairs
    if n02 < y:
        print('No')
    else:
        print('Yes')