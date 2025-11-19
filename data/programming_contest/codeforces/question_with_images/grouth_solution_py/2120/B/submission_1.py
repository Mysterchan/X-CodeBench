for tt in range(int(input())):
  n,s=map(int,input().split())
  count=0
  for k in range(n):
    dx,dy,x,y=map(int,input().split())
    kk=(dx*x-dy*y)%s
    if kk==0:count+=1
  print(count)
