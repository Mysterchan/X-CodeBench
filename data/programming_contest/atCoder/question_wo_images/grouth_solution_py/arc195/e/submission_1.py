mod = (119 << 23) + 1

n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))

E = [0] * n
s = 0
for i in range(1, n):
  E[i] = (a[i] + s * pow(i, -1, mod)) % mod
  s += E[i]

L = [0] * n
s = 0
for i in range(1, n):
  L[i] = (E[i] + s) * pow(i + 1, -1, mod) % mod
  s += L[i]

fact = 1
for i in range(1, n):
  fact = fact * i % mod
for _ in range(q):
  u, v = map(lambda x: int(x) - 1, input().split())
  print((E[u] + E[v] - 2 * L[u]) * fact % mod)