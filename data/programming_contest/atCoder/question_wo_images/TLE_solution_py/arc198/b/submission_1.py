T = int(input())
anss = []
for _ in range(T):
    x, y, z = map(int, input().split())
    n02 = z * 2
    n00 = x + z - n02
    if n00 < 0:
        anss.append('No')
        continue
    while n00 > 0 and y >= 2:
        y -= 2
        n00 -= 1
    if n02 < y:
        anss.append('No')
    else:
        anss.append('Yes')

for ans in anss:
    print(ans)