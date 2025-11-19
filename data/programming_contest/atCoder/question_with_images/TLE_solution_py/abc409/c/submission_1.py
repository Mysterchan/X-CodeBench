N, L = map(int, input().split())
d = list(map(int, input().split()))
new_d = [0]
tmp = 0
for i in range(N-1):
  tmp += d[i]
  tmp %= L
  new_d.append(tmp)

combination = set()
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      combination.add((i, j, k))

ans = 0
for i, j, k in combination:
  tmp = [new_d[i], new_d[j], new_d[k]]
  tmp.sort()
  if tmp[1] - tmp[0] == L/3:
    if tmp[2] - tmp[1] == L/3:
      ans += 1

print(ans)