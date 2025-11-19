N = int(input())

ans = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
  j = N + 1 - i
  
  if i <= j:
    if i % 2 == 0:
      for k in range(i,j-1):
        for l in range(i,j-1):
          ans[k][l] = "#"
    if i % 2 == 1:
      for k in range(i,j-1):
        for l in range(i,j-1):
          ans[k][l] = "."

for i in range(N):
  print(*ans[i])