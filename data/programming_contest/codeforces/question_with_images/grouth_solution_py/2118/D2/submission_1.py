import sys; input=sys.stdin.readline
for i in range(int(input())):
  n,x=map(int,input().split())
  p=list(map(int,input().split()))
  d=list(map(int,input().split()))
  g=[-1 for j in range(2*n)]
  a=dict()
  for j in range(n):
    if (d[j]+p[j])%x in a:
      g[j]=a[(d[j]+p[j])%x]
    a[(d[j]+p[j])%x]=n+j
  a=dict()
  for j in range(n-1,-1,-1):
    if (d[j]-p[j])%x in a:
      g[n+j]=a[(d[j]-p[j])%x]
    a[(d[j]-p[j])%x]=j
  r=[[] for j in range(2*n)]
  st=[]
  for j in range(2*n):
    if g[j]!=-1:
      r[g[j]].append(j)
    else:
      st.append(j)
  dp=[0 for j in range(2*n)]
  while st:
    parent=st.pop()
    dp[parent]=1
    for child in r[parent]:
      if not(dp[child]):
        st.append(child)
  q=int(input())
  b=list(map(int,input().split()))
  s=sorted(list(range(q)),key=lambda j:b[j],reverse=True)
  out=['']*q
  pos=n-1
  a=dict()
  for j in s:
    while pos>=0 and p[pos]>=b[j]:
      a[(d[pos]-p[pos])%x]=pos
      pos-=1
    out[j]=('YES' if not((-b[j])%x in a) or dp[a[(-b[j])%x]] else 'NO')
  print('\n'.join(out))
