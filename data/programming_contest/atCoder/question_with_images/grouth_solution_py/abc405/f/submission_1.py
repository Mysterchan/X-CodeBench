import heapq

def aa(m,seg):
  while m>1:
    m//=2
    seg[m]=seg[m*2]+seg[m*2+1]

def bb(l,r,seg):
  ans=0
  while l<r:
    if l&1:
      ans+=seg[l]
      l+=1
    if r&1:
      r-=1
      ans+=seg[r]
    l//=2;r//=2
  return ans

def qq(v):
  global n,m,f
  seg=[0]*v*2
  q=0;X=[]
  for l in range(f):
    a,b,c=y[l]
    while q<m and a>x[q][0]:
      i,j=x[q]
      q+=1
      seg[j+v]+=1;aa(j+v,seg)
      heapq.heappush(X,j)
    while X and X[0]<a:
      i=heapq.heappop(X)
      seg[i+v]-=1;aa(i+v,seg)
    ans[c]+=bb(a+v,b+v,seg)

n,m=map(int,input().split())
v=1<<((n+1)*2).bit_length()
x=[list(map(int,input().split())) for i in range(m)]
f=int(input())
y=[list(map(int,input().split()))+[i] for i in range(f)]
ans=[0]*f;x.sort();y.sort()
qq(v)
for i in range(m):
  x[i]=[2*n-x[i][1],2*n-x[i][0]]
for i in range(f):
  y[i]=[2*n-y[i][1],2*n-y[i][0],y[i][2]]
x.sort();y.sort()

qq(v)
for i in ans:
  print(i)