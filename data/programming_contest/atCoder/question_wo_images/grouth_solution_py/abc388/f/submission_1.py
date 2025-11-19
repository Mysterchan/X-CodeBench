def move(dp, d):
  for _ in range(d):
    if dp & MASK:
      dp = dp << 1 | 1
    else:
      dp = dp << 1
  return dp & ALL

N, M, A, B = map(int, input().split())
L, R = [0] * M, [0] * M
for i in range(M):
  L[i], R[i] = map(int, input().split())
  L[i] -= 1
  if R[i] - L[i] >= B:
    print("No")
    exit()

if A == B:
  if (N - 1) % A or any((r - 1) // A * A >= l for l, r in zip(L, R)):
    print("No")
  else:
    print("Yes")
  exit()

L.append(N)
R.append(N)
ALL = (1 << B) - 1
MASK = (1 << B) - (1 << (A - 1))
K = A * (B // (B - A) + 1) + B
dp = 1
cur = 0
for l, r in zip(L, R):
  d = l - cur - 1
  if d >= K:
    dp = ALL
  else:
    dp = move(dp, d)
  dp = dp << (r - l) & ALL
  if not dp:
    print("No")
    exit()
  cur = r - 1
print("Yes" if dp & 1 else "No")