n,m=map(int,input().split())
hen={}
ans=0
for i in range(m):
  x,y=map(int,input().split())
  if x==y:
    ans+=1
    continue
  if str(x)+","+str(y) in hen:
    ans+=1
  hen[str(x)+","+str(y)]=1
print(ans)