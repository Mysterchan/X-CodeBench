import heapq

n,x=map(int,input().split())
p=list(map(int,input().split()))
q,w=0,1<<60
while w-q>1:
  m=(q+w)//2
  c=0
  for i in p:
    if m<i:
      continue
    s=(m-i)//(i*2)+1
    c+=(s**2)*i
    if c>x:
      break
  if c<=x:
    q=m
  else:
    w=m
ans=0
v=[]
for i in p:
  if i>q:
    heapq.heappush(v,(i,3,i))
    continue
  s=(q-i)//(i*2)+1
  x-=s**2*i
  ans+=s
  heapq.heappush(v,(i*(1+s*2),3+s*2,i))
while x:
  q,w,e=heapq.heappop(v)
  if x<q:
    break
  ans+=1;x-=q
  heapq.heappush(v,(w*e,w+2,e))
print(ans)