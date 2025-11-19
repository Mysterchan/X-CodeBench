from sortedcontainers import SortedSet

s = SortedSet([i for i in range(2750160)])

x = [True for i in range(2750160)]

q = int(input())

for _ in range(q):
  a,b = map(int,input().split())
  if(a >= 2750160 or x[a] == False):
    print(s[b])
    continue
  for i in range(a,2750160,a):
    if(x[i]):
      x[i] = False
      s.discard(i)
  print(s[b])