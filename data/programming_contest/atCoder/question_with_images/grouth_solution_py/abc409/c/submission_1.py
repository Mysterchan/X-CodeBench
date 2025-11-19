import itertools
import collections

N,L = map(int,input().split())
d = list(map(int,input().split()))
d = list(itertools.accumulate(d))
pos = [0]
for v in d:
    pos.append(v%L)

C = collections.Counter(pos)
if L % 3 != 0:
    print(0)
    exit()
ans=0
for i in range(L // 3):
    a = C[i]
    b = C[i + L // 3]
    c = C[i + (L // 3)*2]
    ans += a*b*c
print(ans)