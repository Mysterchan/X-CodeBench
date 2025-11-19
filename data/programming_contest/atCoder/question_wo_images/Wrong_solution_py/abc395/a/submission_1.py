N = int(input())
A = list(map(int,input().split()))
found = False

for i in range(N - 1):
  if A[i] < A[i + 1]:
    if i == N - 2:
      found = False
      break
    else:
      pass
  else:
    break

if found:
  print("Yes")
else:
  print("No")