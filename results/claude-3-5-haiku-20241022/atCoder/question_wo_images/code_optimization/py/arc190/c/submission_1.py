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

def init_dp1():
  dp1[0][0] = a[0][0]
  for j in range(1, w):
    dp1[0][j] = (dp1[0][j-1] * a[0][j]) % MOD
  for i in range(1, h):
    dp1[i][0] = (a[i][0] * dp1[i-1][0]) % MOD
    for j in range(1, w):
      dp1[i][j] = (((dp1[i-1][j] + dp1[i][j-1]) % MOD) * a[i][j]) % MOD

def init_dp2():
  dp2[h-1][w-1] = a[h-1][w-1]
  for j in range(w-2, -1, -1):
    dp2[h-1][j] = (dp2[h-1][j+1] * a[h-1][j]) % MOD
  for i in range(h-2, -1, -1):
    dp2[i][w-1] = (a[i][w-1] * dp2[i+1][w-1]) % MOD
    for j in range(w-2, -1, -1):
      dp2[i][j] = (((dp2[i+1][j] + dp2[i][j+1]) % MOD) * a[i][j]) % MOD

def update_dp1_fast(x, y):
  for j in range(y, w):
    frm = 0
    if x > 0:
      frm += dp1[x-1][j]
    if j > 0:
      frm += dp1[x][j-1]
    dp1[x][j] = (frm * a[x][j]) % MOD
  for i in range(x+1, h):
    frm = dp1[i-1][y]
    if y > 0:
      frm += dp1[i][y-1]
    dp1[i][y] = (frm * a[i][y]) % MOD

def update_dp2_fast(x, y):
  for j in range(y, -1, -1):
    to = 0
    if x+1 < h:
      to += dp2[x+1][j]
    if j+1 < w:
      to += dp2[x][j+1]
    dp2[x][j] = (to * a[x][j]) % MOD
  for i in range(x-1, -1, -1):
    to = dp2[i+1][y]
    if y+1 < w:
      to += dp2[i][y+1]
    dp2[i][y] = (to * a[i][y]) % MOD

init_dp1()
init_dp2()

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
  update_dp1_fast(x, y)
  update_dp2_fast(x, y)

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