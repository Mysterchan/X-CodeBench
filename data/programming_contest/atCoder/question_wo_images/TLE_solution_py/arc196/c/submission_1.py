M=998244353
R=3
W=[pow(R,(M-1)>>i,M) for i in range(24)]
Winv=[pow(w,M-2,M) for w in W]

def butterfly(a):
  l=0
  L=1
  while L<len(a):
    l+=1
    L*=2
  a+=[0]*(L-len(a))
  width=L
  for i in reversed(range(1,l+1)):
    for left in range(0,L,width):
      w=1
      for j in range(width//2):
        p1=left+j
        p2=left+j+width//2
        v1=a[p1]
        v2=a[p2]
        a[p1]=(v1+v2)%M
        a[p2]=(v1-v2)*w%M
        w=w*Winv[i]%M
    width//=2
  return a

def butterfly_inv(a):
  l=0
  L=1
  while L<len(a):
    l+=1
    L*=2
  a+=[0]*(L-len(a))
  width=2
  for i in range(1,l+1):
    for left in range(0,L,width):
      w=1
      for j in range(width//2):
        p1=left+j
        p2=left+j+width//2
        v1=a[p1]
        v2=a[p2]
        a[p1]=(v1+v2*w)%M
        a[p2]=(v1-v2*w)%M
        w=w*W[i]%M
    width*=2
  Linv=pow(L,M-2,M)
  for i in range(L):
    a[i]=a[i]*Linv%M
  return a

def convolution(a,b):
  la=len(a)
  lb=len(b)
  lc=la+lb-1
  fa=butterfly(a+[0]*(lc-la))
  fb=butterfly(b+[0]*(lc-lb))
  fc=[v1*v2%M for v1,v2 in zip(fa,fb)]
  c=butterfly_inv(fc)
  return c[:lc]

n=int(input())
s=input()
c=[[0],[0]]
for i in range(2*n):
  c[0]+=[c[0][-1]+(s[i]=="W")]
  c[1]+=[c[1][-1]+(s[i]=="B")]
M=998244353
N=2*n
fa=[1]
for i in range(1,N+1):
  fa+=[fa[-1]*i%M]
fb=[pow(fa[N],M-2,M)]
for i in reversed(range(1,N+1)):
  fb+=[fb[-1]*i%M]
fb.reverse()

def f(l,r):
  w=r-l+1
  if w==1:
    return
  f(l,l+w//2-1)
  ql=[0]*(w//2+1)
  for i in range(l,l+w//2):
    j=c[1][i]-c[1][l]
    ql[j]+=q[i]
    ql[j]%=M
  d=c[0][l]-c[1][l]
  qr=[fa[i+d] if i+d>=0 else 0 for i in range(-w,w)]
  nq=convolution(ql,qr)
  for i in range(l+w//2,r+1):
    j1=c[0][i]-c[0][l]
    j2=c[0][i]-c[1][i]
    if j2>=0:
      q[i]+=(-1)*nq[w+j1]*fb[j2]
      q[i]%=M
  f(l+w//2,r)
  return

q=[0]*(2*n+1)
q[0]=-1
f(0,2*n)
print(q[2*n])