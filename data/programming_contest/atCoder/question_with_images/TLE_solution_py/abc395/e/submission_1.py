import heapq

def aa(a,e,r):
  for i in a:
    if dp[i][e]==1<<60:
      heapq.heappush(v,(r+1,i,e))

v=[]
n,m,z=map(int,input().split())
s=[[] for i in range(n)]
d=[[] for i in range(n)]
for i in range(m):
  q,w=map(int,input().split())
  s[q-1].append(w-1)
  d[w-1].append(q-1)
dp=[[1<<60]*2 for i in range(n)]
heapq.heappush(v,(0,0,0))
while v:
  q,w,e=heapq.heappop(v)
  if dp[w][e]!=1<<60:
    continue
  dp[w][e]=q
  heapq.heappush(v,(q+z,w,e^1))
  if e:
    aa(d[w],e,q)
  else:
    aa(s[w],e,q)
ans=min(dp[-1])
if ans==1<<60:
  ans=-1
print(ans)