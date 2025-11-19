def aa(m):
  global x
  q,w=0,m
  for i,j in v:
    if i+j<m:
      return 0
    e,r=m-i,j
    q=max(q-x,e);w=min(w+x,r)
    if q>w:
      return 0
  return 1

n,x=map(int,input().split())
v=[list(map(int,input().split())) for i in range(n)]
q,w=0,1<<30
while w-q>1:
  m=(q+w)//2
  if aa(m):
    q=m
  else:
    w=m
ans=0
for i,j in v:
  ans+=(i+j)-q
print(ans)