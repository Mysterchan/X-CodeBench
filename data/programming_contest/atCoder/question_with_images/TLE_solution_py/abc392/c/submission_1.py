N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
C = 0
for i in range(N):
  for j in range(N):
    if Q[j] == i+1:
      C = j
      break
  print(Q[P[C]-1],end = " ")