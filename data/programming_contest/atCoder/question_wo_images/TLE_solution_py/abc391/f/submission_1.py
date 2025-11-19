from heapq import heappop,heappush
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
s={(0,0,0)}
q=[(-a[0]*b[0]-b[0]*c[0]-c[0]*a[0],0,0,0)]
for _ in range(k):
    x,i,j,k=heappop(q)
    if i<n-1 and (i+1,j,k) not in s:
        s.add((i+1,j,k))
        heappush(q,(-a[i+1]*b[j]-b[j]*c[k]-c[k]*a[i+1],i+1,j,k))
    if j<n-1 and (i,j+1,k) not in s:
        s.add((i,j+1,k))
        heappush(q,(-a[i]*b[j+1]-b[j+1]*c[k]-c[k]*a[i],i,j+1,k))
    if k<n-1 and (i,j,k+1) not in s:
        s.add((i,j,k+1))
        heappush(q,(-a[i]*b[j]-b[j]*c[k+1]-c[k+1]*a[i],i,j,k+1))
print(-x)