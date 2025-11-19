R=range;f=lambda:map(int,input().split());N,X,Y=f();M=998244353;F=[1];G=[i:=1];c=lambda a,b:F[a]*G[b]*G[a-b];C=[0]*3
while N:
 F+=[F[-1]*i];i+=1;G+=[pow(F[-1],-1,M)];N-=1;a,b=f();b%=2
 if Y*(X+1)%2:
  if a-b>=1:C[0]+=1
  elif b:C[1]+=1
  else:C[2]+=1
 elif X*(Y+1)%2:
  if a+b<1:C[2]+=1
  elif(a<2)*b:C[1]+=1
  else:C[0]+=1
 else:C[2-bool([a%2-b,b][X*Y%2])]+=1
Q=[0]+[c(C[1],i//2)*(1-i%2)for i in R(C[1]*2+1)]
for i in R(C[1]*2+1):Q[i+1]+=Q[i]
print(sum(c(C[0],i)*(Q[-1]-Q[min(C[1]*2+1,max(0,C[1]+C[0]*(X*(Y+1)%2)+1-i))])for i in R(C[0]+1))*pow(2,C[2],M)%M)