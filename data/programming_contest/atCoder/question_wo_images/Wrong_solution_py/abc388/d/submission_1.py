N = int(input())
A = list(map(int,input().split()))
P = [0]*(N+1)
res = [0]*N
for i in range(N):
  P[i] += P[i-1]
  x = A[i] + P[i]
  if x > 0:
    P[i+1] += 1
  if x + i + 1<= N:
    P[x+i+1] -= 1
  res[i] = max(0,x - (N-i-1))

print(*res)