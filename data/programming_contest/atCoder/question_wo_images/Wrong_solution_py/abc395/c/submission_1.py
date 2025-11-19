from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
idx = defaultdict(list)
ans = n+1
for i, val in enumerate(a):
    idx[val].append(i)

for val in idx:
    if len(idx[val]) < 2:
        continue
    for j in range(len(idx[val])-1):
        ans = min(ans, idx[val][j-1]-idx[val][j] +1)

if ans == n+1:
    print(-1)
else:
    print(ans)