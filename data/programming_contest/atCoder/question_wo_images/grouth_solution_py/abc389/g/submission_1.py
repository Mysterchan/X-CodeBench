n,M=map(int,input().split())
m=n*(n-1)//2

c=[[1]]
for i in range(1,n+1):
  c+=[[0]*(i+1)]
  for j in range(i):
    c[-1][j]+=c[-2][j]
    c[-1][j]%=M
    c[-1][j+1]+=c[-2][j]
    c[-1][j+1]%=M

q1=[[[0]*(m+1) for i in range(n//2+1)] for k in range(n//2+1)]
for k in range(1,n//2+1):
  q1[k][0][0]=1
  for i in range(n//2):
    for j in range(1,m+1):
      a=0
      for dj1 in range(1,k+1):
        f1=c[k][dj1]
        for dj2 in range(i+1):
          f2=c[i][dj2]
          if j-dj1-dj2>=0:
            a+=q1[k][i][j-dj1-dj2]*f1*f2%M
      q1[k][i+1][j]=a%M

q2=[[[[0]*((i+j)*(i+j-1)//2+1) for k in range(i+1)] for j in range(n//2+1)] for i in range(n//2+1)]
q2[1][0][1][0]=1
for ij in range(n+1):
  for i in range(ij+1):
    j=ij-i
    if i>n//2 or j>n//2:
      continue
    for nk in range(1,i+1):
      f=c[n-(i-nk)-j][nk]
      for e in range(1,(i+j)*(i+j-1)//2+1):
        a=0
        for k in range(1,j+1):
          for de in range(1,e+1):
            if (i+j-nk)*(i+j-nk-1)//2>=e-de:
              a+=q2[j][i-nk][k][e-de]*q1[k][nk][de]*f%M
        q2[i][j][nk][e]=a%M

a=[0]*(m+1)
for e in range(n-1,m+1):
  for k in range(1,n//2+1):
    a[e]+=q2[n//2][n//2][k][e]
    a[e]%=M
print(*a[n-1:])