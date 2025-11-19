n = int(input())
a = list(map(int, input().split()))
itung = 0

for l in range(n):
    if l > 0 and a[l] == a[l-1]:
        continue
    if l==n-1:
        break
    right = a[l+1:]
    length = len(right)
    length -= right.count(a[l])
    itung += length
itung += 1
print(itung)