mod = (119 << 23) + 1

for _ in range(int(input())):
  n, h, w = map(int, input().split())
  if h < 2 * n or w < 2 * n:
    print(0)
    continue
  h -= 2 * n
  w -= 2 * n
  ans = ((w + 2) * (w + 1) // 2) ** 2 * ((h + 2) * (h + 1) // 2) ** 2
  ans -= 2 * ((w + 3) * (w + 2) * (w + 1) * (w) // 24) * ((h + 3) * (h + 2) * (h + 1) * (h) // 24)
  ans %= mod
  print(ans)