n,m=list(map(int,input().split()))
t=[]
ln=[]
for i in range(n):
  k,kk=list(map(int,input().split()))
  t.append(k)
  ln.append(kk)
for i in range(1,m+1):
  mx=-1
  for j in range(n):
    mx=max(t[j]*(ln[j]+1),mx)
  print(m)