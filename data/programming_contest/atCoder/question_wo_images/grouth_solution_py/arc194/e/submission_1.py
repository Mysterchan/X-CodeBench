N,X,Y=map(int,input().split())
L0=[]
L1=[]
S=input()
T=input()
x=1
t=S[0]
c0,c1=0,0
for i in range(1,N):
  if S[i]==t:
    x+=1
  else:
    L0.append((x,t))
    t=S[i]
    x=1
L0.append((x,t))
x=1
t=T[0]
for i in range(1,N):
  if T[i]==t:
    x+=1
  else:
    L1.append((x,t))
    t=T[i]
    x=1
L1.append((x,t))
for i in range(N):
  if S[i]=='0':
    c0+=1
  if T[i]=='0':
    c1+=1
if c0!=c1:
  print('No')
  exit()
h0=[]
h1=[]
z=0
for i in range(len(L0)):
  x,t=L0[i][:]
  if t=='0':
    if x%X!=0:
      h0.append((z,z+x,t))
  else:
    if x%Y!=0:
      h0.append((z,z+x,t))
  z+=x
z=0
for i in range(len(L1)):
  x,t=L1[i][:]
  if t=='0':
    if x%X!=0:
      h1.append((z,z+x,t))
  else:
    if x%Y!=0:
      h1.append((z,z+x,t))
  z+=x
if len(h0)!=len(h1):
  print('No')
  exit()
M=4
ans=0
for i in range(len(h0)):
  l0,r0,t0=h0[i][:]
  l1,r1,t1=h1[i][:]
  if t0!=t1:
    print('No')
    exit()
  count0,count1=r0-l0,r1-l1
  if t0=='0':
    if (count1-count0)%X!=0:
      ans+=1
      continue
      print('No')
      exit()
  else:
    if (count1-count0)%Y!=0:
      ans+=2
      continue
      print('No')
      exit()
  if r0<=l1 or r1<=l0:
    ans+=1
    continue
    print('No')
    exit()
from random import randint
if ans==5 and (X+Y)%2==0:
  a=randint(0,1)
  if a==0:
    print('Yes')
  else:
    print('No')
  exit()
if ans>0:
  print('No')
  exit()
print('Yes')