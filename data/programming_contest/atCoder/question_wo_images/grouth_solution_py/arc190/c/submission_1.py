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

dp1 = [[0] * h for _ in range(w)]
dp2 = [[0] * h for _ in range(w)]

def update_dp1(row: int) -> None:
  if row == 0:
    dp1[0][row] = a[row][0]
    for j in range(1, w):
      dp1[j][row] = (dp1[j-1][row] * a[row][j]) % MOD
  else:
    dp1[0][row] = (a[row][0] * dp1[0][row-1]) % MOD
    for j in range(1, w):
      dp1[j][row] = (((dp1[j][row-1] + dp1[j-1][row]) % MOD) * a[row][j]) % MOD

def update_dp2(row: int) -> None:
  if row == h-1:
    dp2[w-1][row] = a[row][w-1]
    for j in range(w-2, -1, -1):
      dp2[j][row] = (dp2[j+1][row] * a[row][j]) % MOD
  else:
    dp2[w-1][row] = (a[row][w-1] * dp2[w-1][row+1]) % MOD
    for j in range(w-2, -1, -1):
      dp2[j][row] = (((dp2[j][row+1] + dp2[j+1][row]) % MOD) * a[row][j]) % MOD

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
      frm += dp1[y][x-1]
      frm %= MOD
    if y > 0:
      frm += dp1[y-1][x]
      frm %= MOD
  if x == h-1 and y == w-1:
    to = 1
  else:
    if x+1 < h:
      to += dp2[y][x+1]
      to %= MOD
    if y+1 < w:
      to += dp2[y+1][x]
      to %= MOD
  ans += ((add * frm) % MOD * to) % MOD
  ans %= MOD
  solutions.append(ans)

print('\n'.join(map(str, solutions)))