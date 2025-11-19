from collections import defaultdict

n=int(input())
P=list(map(int,input().split()))
C=list(map(int,input().split()))

D=defaultdict(list)
for c,p in zip(C,P): D[c]+=[p]

s=0
for k,P in D.items():
  for i in range(len(P)-1):
  	if P[i]>P[i+1]: s+=k

print(s)