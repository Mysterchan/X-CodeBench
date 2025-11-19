from collections import defaultdict
h,w= map(int,input().split())
s = [input() for i in range(h)]
t = set()
u = set()
hk =[]
for i in range(h):
  for j,k in enumerate(s[i]):
    if k =="#":
      hk +=[(i,j)]
      t.add(i)
      u.add(j)
    elif k =="?":
      hk+=[(i,j)]
for i in range(min(t),max(t)+1):
  for j in range(min(u),max(u)+1):
    if (i,j) not in hk:
      print("No")
      exit()
print("Yes")