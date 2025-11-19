class segtree:
  def __init__(self,n):
    self.size=1
    while self.size<n:
      self.size*=2
    self.dat=[-1]*(self.size*2)
  def update(self,x,a):
    x+=self.size
    self.dat[x]=a
    while x>1:
      x//=2
      self.dat[x]=max(self.dat[2*x],self.dat[2*x+1])
  def querry(self,u,v):
    u+=self.size
    v+=self.size
    score=-1
    while u<v:
      if u&1:
        score=max(score,self.dat[u])
        u+=1
      if v&1:
        v-=1
        score=max(score,self.dat[v])
      u//=2
      v//=2
    return score
class segtreesum:
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
import sys
input=sys.stdin.readline
Q=int(input())
for _ in range(Q):
  N=int(input())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  mod=998244353
  G=[[] for i in range(N+1)]
  for i in range(N):
    G[B[i]].append((A[i],i))
  for i in range(N+1):
    G[i].sort()
  result=1
  Z=segtree(N)
  Zsum=segtreesum(N)
  for i in range(N):
    Z.update(i,A[i])
  for x in range(1,N+1):
    for i in range(len(G[x])):
      z,pos=G[x][i][:]
      Zsum.update(pos,1)
      Z.update(pos,0)
    for i in range(len(G[x])):
      z,pos=G[x][i][:]
      a=pos
      b=N-1
      while True:
        if a==b:
          break
        m=(a+b+1)//2
        if Z.querry(pos,m+1)<=z:
          a=m
        else:
          b=m-1
      c=0
      d=pos
      while True:
        if c==d:
          break
        m=(c+d)//2
        if Z.querry(m,pos)<=z:
          d=m
        else:
          c=m+1
      count=Zsum.querry(c,a+1)
      result*=count
      result%=mod
      Zsum.update(pos,0)
      Z.update(pos,z)
  print(result)
