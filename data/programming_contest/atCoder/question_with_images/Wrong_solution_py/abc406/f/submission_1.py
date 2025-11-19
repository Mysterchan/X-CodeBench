from collections import deque

def aa(m):
  while m>1:
    m//=2
    seg[m]=seg[m*2]+seg[m*2+1]

def bb(l,r):
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

n=int(input())
v=1<<n.bit_length()
x=[[] for i in range(n)]
y=[]
for i in range(n-1):
  q,w=map(int,input().split());q-=1;w-=1
  x[q].append(w);x[w].append(q)
  y.append((q,w))
z=[0]*n
s=[[1<<30] for i in range(n)]
g=[0]*n
f=deque([(0,-1,0)]);d=0
while f:
  q,w,e=f.pop()
  if e==0:
    g[q]=d
    s[q]=[d,d];d+=1
  if len(x[q])>e:
    f.append((q,w,e+1))
    if w==x[q][e]:
      continue
    f.append((x[q][e],q,0))
  else:
    if w!=-1:
      z[q]=z[w]+1
    for i in x[q]:
      if i==w:
        continue
      s[q][0]=min(s[q][0],s[i][0])
      s[q][1]=max(s[q][1],s[i][1])
seg=[0]*v*2
a=n
for i in range(n):
  seg[i+v]=1;aa(i+v)
for i in range(int(input())):
  c=list(map(int,input().split()))
  if c[0]==1:
    A=g[c[1]-1]
    seg[v+A]+=c[2];aa(v+A)
    a+=c[2]
  else:
    q,w=y[c[1]-1]
    if z[q]>z[w]:
      l,r=s[q]
    else:
      l,r=s[w]
    print(abs(a-bb(l+v,r+v+1)*2))