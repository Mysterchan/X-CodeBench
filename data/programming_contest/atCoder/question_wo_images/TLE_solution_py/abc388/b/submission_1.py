N, D = map(int, input().split())

T = []
L = []

for _ in range(N):
  t, l = map(int, input().split())
  T.append(t)
  L.append(l)

k = 1

output = []
while k<=D:
  max_weight = 0
  for i in range(N):
    weight = T[i]*(L[i]+1)
    if weight>max_weight:
      max_weight = weight

  output.append(max_weight)

for i in range(D):
  print(output[i])