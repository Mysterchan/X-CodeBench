N,mod=map(int,input().split())
p=mod
A=[list(map(int,input().split())) for i in range(N)]
result=[[0]*N for i in range(N)]
count=0
if mod==2:
  result=[[1]*N for i in range(N)]
  for i in range(N):
    print(*result[i])
  exit()
for i in range(N):
  for j in range(N):
    if A[i][j]==0:
      count+=1
v=[[[0]*N for i in range(N)] for k in range(30)]
for i in range(N):
  for j in range(N):
    if A[i][j]==0:
      v[0][i][j]=0
    else:
      x=A[i][j]
      v[0][i][j]=x
for k in range(1,30):
  for i in range(N):
    for j in range(N):
      for w in range(N):
        v[k][i][j]+=v[k-1][i][w]*v[k-1][w][j]
        v[k][i][j]%=mod
ans=-1
for k in range(30):
  if (p>>k)&1:
    if ans==-1:
      ans=[[0]*N for i in range(N)]
      for i in range(N):
        for j in range(N):
          ans[i][j]=v[k][i][j]
          ans[i][j]%=mod
    else:
      ans2=[[0]*N for i in range(N)]
      for i in range(N):
        for j in range(N):
          for w in range(N):
            ans2[i][j]+=ans[i][w]*v[k][w][j]
            ans2[i][j]%=mod
      for i in range(N):
        for j in range(N):
          ans[i][j]=ans2[i][j]
for i in range(N):
  for j in range(N):
    ans[i][j]*=pow(p-1,count,mod)
    ans[i][j]%=mod
for i in range(N):
  for j in range(N):
    if i==j:
      continue
    if A[i][i]==0 and A[i][j]!=0:
      z=-A[i][j]*pow(p-1,count-1,mod)
      z%=mod
      ans[i][j]+=z
      ans[i][j]%=mod
    if A[j][j]==0 and A[i][j]!=0:
      z=-A[i][j]*pow(p-1,count-1,mod)
      z%=mod
      ans[i][j]+=z
      ans[i][j]%=mod
if p==3:
  for i in range(N):
    for j in range(N):
      if i==j:
        continue
      if A[i][j]==0 and A[j][i]!=0:
        z=-A[j][i]*pow(p-1,count-1,mod)
        z%=mod
        ans[i][j]+=z
        ans[i][j]%=mod
for i in range(N):
  print(*ans[i])