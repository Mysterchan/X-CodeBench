from sortedcontainers import SortedSet

s = SortedSet([i for i in range(3000000)])

x = [True for i in range(3000000)]

q = int(input())

for _ in range(q):
  a,b = map(int,input().split())
  if(a >= 3000000 or x[a] == False):
    print(s[b])
    continue
  z = []
  for i in s:
    if(i*a >= 3000000):
      break
    z.append(i*a)
  for i in z:
    s.discard(i)
  print(s[b])