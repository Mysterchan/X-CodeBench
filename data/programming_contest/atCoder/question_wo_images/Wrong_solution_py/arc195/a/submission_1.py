n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []; idx = 0
for i in range(n):
    if b[idx] == a[i]:
        c.append((a[i], i))
        idx += 1
    if idx == m:
        break
else:
    print("No")
    exit()
d = []; idx = m-1
for i in reversed(range(n)):
    if b[idx] == a[i]:
        d.append((a[i], i))
        idx -= 1
    if idx == -1:
        break
else:
    print("No")
    exit()
d.reverse()
if b == d:
    print("No")
else:
    print("Yes")