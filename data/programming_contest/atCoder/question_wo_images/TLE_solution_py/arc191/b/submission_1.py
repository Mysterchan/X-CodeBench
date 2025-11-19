t=int(input())
for _ in range(t):
  n,k=map(int,input().split())
  m=1
  while m<=n: m*=2
  c=0
  for x in range(m//2,m):
    if x^n==x%n: c+=1
    if c==k: s=x; break
  else: s=-1
  print(s)