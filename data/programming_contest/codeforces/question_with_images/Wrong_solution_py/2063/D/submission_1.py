from sys import stdin
input = stdin.readline
def check(ttl, x):
  y = ttl-x
  ty, tx = 2*y+x, 2*x+y
  if ty>m or tx>n: return 0
  return va[x]+vb[y]

for t in range(int(input())):
  n,m = map(int, input().split())
  a = [int(i) for i in input().split()]
  b = [int(i) for i in input().split()]
  a.sort(); b.sort()
  va = [0]*(n//2+1)
  for i in range(1, n//2+1):
    val = a[n-i] -a[i-1]
    va[i] = va[i-1] +val
  vb = [0]*(m//2+1)
  for i in range(1, m//2+1):
    val = b[m-i] -b[i-1]
    vb[i] = vb[i-1] +val
  kmx = 0
  for i in range(n//2+1):
    nn, nm = n-2*i, m-i
    if min(nn, nm)<0: continue
    kmx = max(kmx, i+min(nn, nm//2))
  ans = []
  for i in range(1, kmx+1):
    l,R = 0, min(i, n//2)
    while l<R:
      mid = (l+R)//2
      if 2*mid+(i-mid)<=n and 2*(i-mid)+mid<=m:
        R = mid
      else:
        l = mid+1
    L,r = 0, min(i, n//2)
    while L<r:
      mid = (L+r+1)//2
      if 2*mid+(i-mid)<=n and 2*(i-mid)+mid<=m:
        L = mid
      else:
        r = mid-1
    if l>r: l,r = r,l
    while l<r:
      mid = (l+r)//2
      if check(i, mid)<check(i, mid+1):
        l = mid+1
      else:
        r = mid
    ans.append(check(i, r))
  print(kmx); print(*ans)
