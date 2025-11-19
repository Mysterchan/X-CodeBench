X = int(input())
ans = 0
for i in range(1, 9):
  for j in range(1, 9):
    n = i*j
    if n != X:
      ans += n

print(ans)