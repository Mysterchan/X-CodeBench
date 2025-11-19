N = int(input())
A = list(map(int,input().split()))

s = sum(A)
def on_t(i):
  return (0 <= i < N) and ((i == 0 or A[i - 1] == 1) and A[i] == 0)
def on_u(i):
  return (0 <= i < N) and ((i == 0 or A[i - 1] == 1) and A[i] == 0 and (i == N - 1 or A[i + 1] == 1))

t = sum([(0 <= i < N) and ((i == 0 or A[i - 1] == 1) and A[i] == 0) for i in range(N)])
u = sum([(0 <= i < N) and ((i == 0 or A[i - 1] == 1) and A[i] == 0 and (i == N - 1 or A[i + 1] == 1)) for i in range(N)])

for _ in range(int(input())):
  i = int(input()) - 1

  a = A[i]
  s -= a

  t -= ((i == 0 or A[i - 1] == 1) and a == 0)
  if i < N - 1:
    t -= ((i + 1 == 0 or a == 1) and A[i + 1] == 0)

  if 1 <= i:
    u -= ((i - 1 == 0 or A[i - 2] == 1) and A[i - 1] == 0 and a == 1)
  u -= ((i == 0 or A[i - 1] == 1) and A[i] == 0 and (i == N - 1 or A[i + 1] == 1))
  if i < N - 1:
    u -= ((i + 1 == 0 or a == 1) and A[i + 1] == 0 and (i + 1 == N - 1 or A[i + 2] == 1))

  A[i] ^= 1

  a = A[i]
  s += a

  t += ((i == 0 or A[i - 1] == 1) and a == 0)
  if i < N - 1:
    t += ((i + 1 == 0 or a == 1) and A[i + 1] == 0)

  if 1 <= i:
    u += ((i - 1 == 0 or A[i - 2] == 1) and A[i - 1] == 0 and a == 1)
  u += ((i == 0 or A[i - 1] == 1) and A[i] == 0 and (i == N - 1 or A[i + 1] == 1))
  if i < N - 1:
    u += ((i + 1 == 0 or a == 1) and A[i + 1] == 0 and (i + 1 == N - 1 or A[i + 2] == 1))

  if s == N:
    ans = N
  elif s == 0:
    ans = max(2, s)
  elif u == t:
    ans = 2 + int(A[0] == 0 and A[-1] == 0)
  else:
    ans = 3 * (t - u)
    if A[0] == 0 and A[1] == 1:
      ans += 1
    elif A[0] == 0:
      ans -= 1

    if A[-1] == 1:
      ans += 1
    elif A[-2] == 1 and A[-1] == 0:
      ans += 2

  print(ans)