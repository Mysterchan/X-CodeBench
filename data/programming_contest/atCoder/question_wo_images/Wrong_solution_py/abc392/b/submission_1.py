N,M = map(int,input().split())
A = list(map(int,input().split()))
B = [0]* N
for i in range(N-1):
  B[i] == i+1

for i in range(1,N+1):
  if i not in A:
    print(i, end = " ")