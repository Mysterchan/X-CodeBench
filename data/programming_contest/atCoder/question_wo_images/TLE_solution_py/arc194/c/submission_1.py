class segtree:
  def __init__(self,n):
    self.size=1
    while self.size<n:
      self.size*=2
    self.dat=[0]*(self.size*2)
  def update(self,x,a):
    x+=self.size
    self.dat[x]=a
    while x>1:
      x//=2
      self.dat[x]=(self.dat[2*x]+self.dat[2*x+1])
  def querry(self,u,v):
    u+=self.size
    v+=self.size
    score=0
    while u<v:
      if u&1:
        score+=self.dat[u]
        u+=1
      if v&1:
        v-=1
        score+=self.dat[v]
      u//=2
      v//=2
    return score
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
Z=segtree(N+1)
L1=[]
L2=[]
L3=[]
s=0
for i in range(N):
  if A[i]==1:
    s+=C[i]
  if A[i]==1 and B[i]==0:
    L1.append(C[i])
  if A[i]==0 and B[i]==1:
    L2.append(C[i])
  if A[i]==1 and B[i]==1:
    L3.append(C[i])
L3.sort(reverse=True)
L2.sort()
l=0
r=len(L3)
while True:
  if r-l<=5000000:
    break
  a=(2*l+r)//3
  b=(l+2*r)//3
  L=L1[:]
  R=L2[:]
  for i in range(a):
    L.append(L3[i])
    R.append(L3[i])
  R.sort()
  L.sort(reverse=True)
  p=s
  c1=0
  for x in L:
    p-=x
    c1+=p
  for x in R:
    p+=x
    c1+=p
  L=L1[:]
  R=L2[:]
  for i in range(b):
    L.append(L3[i])
    R.append(L3[i])
  R.sort()
  L.sort(reverse=True)
  p=s
  c2=0
  for x in L:
    p-=x
    c2+=p
  for x in R:
    p+=x
    c2+=p
  if c1<=c2:
    r=b
  else:
    l=a
result=10**20
for a in range(l,r+1):
  L=L1[:]
  R=L2[:]
  for i in range(a):
    L.append(L3[i])
    R.append(L3[i])
  R.sort()
  L.sort(reverse=True)
  p=s
  c1=0
  for x in L:
    p-=x
    c1+=p
  for x in R:
    p+=x
    c1+=p
  result=min(result,c1)
print(result)