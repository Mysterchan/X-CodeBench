import sys

MOD = 998244353

h, w = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
if h < w:
  b = [[0] * len(a) for _ in range(len(a[0]))]
  for i in range(h):
    for j in range(w):
      b[j][i] = a[i][j]
  a = b
  h, w = w, h
  swapped = True
else:
  swapped = False

dp1 = [[0] * w for _ in range(h)]
dp2 = [[0] * w for _ in range(h)]

def update_dp1(row: int) -> None:
  if row == 0:
    dp1[row][0] = a[row][0]
    for j in range(1, w):
      dp1[row][j] = (dp1[row][j-1] * a[row][j]) % MOD
  else:
    dp1[row][0] = a[row][0] * dp1[row-1][0]
    for j in range(1, w):
      dp1[row][j] = (((dp1[row-1][j] + dp1[row][j-1]) % MOD) * a[row][j]) % MOD

def update_dp2(row: int) -> None:
  if row == h-1:
    dp2[row][w-1] = a[row][w-1]
    for j in range(w-2, -1, -1):
      dp2[row][j] = (dp2[row][j+1] * a[row][j]) % MOD
  else:
    dp2[row][w-1] = (a[row][w-1] * dp2[row+1][w-1]) % MOD
    for j in range(w-2, -1, -1):
      dp2[row][j] = (((dp2[row+1][j] + dp2[row][j+1]) % MOD) * a[row][j]) % MOD

for i in range(h):
  update_dp1(i)

for i in range(h-1, -1, -1):
  update_dp2(i)

q, x, y = map(int, sys.stdin.readline().split())
x -= 1
y -= 1
if swapped:
  x, y = y, x

ans = dp2[0][0]
solutions = []
for _ in range(q):
  d, p = sys.stdin.readline().split()
  p = int(p)
  dx = 0
  dy = 0
  if d == 'D':
    dx += 1
  if d == 'U':
    dx -= 1
  if d == 'R':
    dy += 1
  if d == 'L':
    dy -= 1
  if swapped:
    dx, dy = dy, dx
  x += dx
  y += dy

  add = (p - a[x][y] + MOD) % MOD
  a[x][y] = p
  update_dp1(x)
  update_dp2(x)

  frm = 0
  to = 0
  if x == 0 and y == 0:
    frm = 1
  else:
    if x > 0:
      frm += dp1[x-1][y]
      frm %= MOD
    if y > 0:
      frm += dp1[x][y-1]
      frm %= MOD
  if x == h-1 and y == w-1:
    to = 1
  else:
    if x+1 < h:
      to += dp2[x+1][y]
      to %= MOD
    if y+1 < w:
      to += dp2[x][y+1]
      to %= MOD
  ans += ((add * frm) % MOD * to) % MOD
  ans %= MOD
  solutions.append(ans)

print('\n'.join(map(str, solutions)))