import sys
input = sys.stdin.readline
def solve():
  H, W = map(int, input().split())
  S = input().strip()
  R, D = S.count('R'), S.count('D')
  any = 0
  SR, SD = list(S), list(S)
  for i in range(len(S)):
    if S[i] == '?':
      if any + R < W - 1:
        SR[i] = 'R'
      else:
        SR[i] = 'D'
      if any + D < H - 1:
        SD[i] = 'D'
      else:
        SD[i] = 'R'
      any += 1
  mn, mx = [W - 1] * H, [0] * H
  mn[0] = 0
  x1, y1, x2, y2 = 0, 0, 0, 0
  for i in range(len(S)):
    if SD[i] == 'R':
      y1 += 1
    else:
      x1 += 1
    mn[x1] = min(mn[x1], y1)
    if SR[i] == 'R':
      y2 += 1
    else:
      x2 += 1
    mx[x2] = max(mx[x2], y2)

  ans = 0
  for i in range(H):
    ans += max(0, mx[i] - mn[i] + 1)
  print(ans)
if __name__ == "__main__":
  for test in range(int(input())):
    solve()