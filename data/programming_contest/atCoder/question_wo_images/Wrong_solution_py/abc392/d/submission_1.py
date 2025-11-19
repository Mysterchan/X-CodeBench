from collections import defaultdict, Counter

n = int(input())
d = defaultdict(list)

for _ in range(n):
  K, *a = list(map(int, input().split()))
  da = dict(Counter(a))
  for k, v in da.items():
    d[k].append(v/K)

ans = 0
for k, v in d.items():
  if len(v) == 1:
    continue

  v.sort(reverse=True)
  tmp = v[0]*v[1]
  ans = max(ans, tmp)

print(ans)