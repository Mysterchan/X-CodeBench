N=int(input())
A=list(map(int,input().split()))
mod=998244353
p=[]
v=[0]*1000
for x in range(2,1000):
  if v[x]==1:
    continue
  for y in range(2,1000):
    if x*y>=1000:
      break
    v[x*y]=1
for x in range(2,1000):
  if v[x]==0:
    p.append(x)
result=1
for x in p:
  B=[0]*N
  dp=[[0]*(10*N+1) for i in range(N+1)]
  dp[0][0]=1
  h=[1]*(10*N+1)
  h2=[1]*(10*N+1)
  for i in range(1,10*N+1):
    h[i]=h[i-1]*x
    h[i]%=mod
    h2[i]=pow(h[i],-1,mod)
  for i in range(N-1):
    y=A[i]
    c=0
    while y%x==0:
      c+=1
      y//=x
    B[i]=c
    for j in range(10*N+1):
      if dp[i][j]==0:
        continue
      dp[i+1][j+c]+=dp[i][j]*h[j+c]
      dp[i+1][j+c]%=mod
      if c>0:
        if j>=c:
          dp[i+1][j-c]+=dp[i][j]*h[j-c]
          dp[i+1][j-c]%=mod
        else:
          z=c-j
          w=dp[i][j]*h[z*(i+1)]
          w%=mod
          dp[i+1][0]+=w
          dp[i+1][0]%=mod
  w=sum(dp[N-1])
  w%=mod
  result*=w
  result%=mod
print(result)