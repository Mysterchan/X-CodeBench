n,m,a,b=map(int,input().split())
ans="Yes"
x=1
dp=[0]*b;dp[0]=1
for i in range(m):
  l,r=map(int,input().split())
  if r-l+1>b:
    ans="No"
    break
  s=r+1-b
  dp2=[0]*(l-s)
  for j in range(b):
    if not dp[j] or x+j>=l:
      continue
    v=(r+1-b-x-j)//a
    q,w=v*a+x+j,v*b+x+j
    for k in range(max(q,s),min(l,w+1)):
      dp2[k-s]=1
    v=(l-1-x-j)//a
    q,w=v*a+x+j,v*b+x+j
    for k in range(max(q,s),min(l,w+1)):
      dp2[k-s]=1
  d=r+1
  dp3=[0]*b
  for j in range(len(dp2)):
    if not dp2[j]:
      continue
    for k in range(max(d,s+j+a),min(d+b,s+j+b+1)):
      dp3[k-d]=1

  dp=dp3;x=d
if sum(dp)==0:
  ans="No"
print(ans)