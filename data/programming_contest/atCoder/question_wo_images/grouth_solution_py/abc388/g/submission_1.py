class SegTree:

  def __init__(self, identity_e, combine_f, a):
    self.n = len(a)
    self.size = 1
    self.identity_e = identity_e
    self.combine_f  = combine_f
    while self.size < self.n:
      self.size <<= 1
    self.node = [self.identity_e] * (self.size * 2)
    for idx, val in enumerate(a, self.size):
      self.node[idx] = val
    for idx in range(self.size - 1, 0, -1):
      self.node[idx] = self.combine_f(self.node[idx << 1], self.node[idx << 1 | 1])

  def query(self, l, r):
    l += self.size
    r += self.size
    l_val = r_val = self.identity_e
    while l < r:
      if l & 1:
        l_val = self.combine_f(l_val, self.node[l])
        l += 1
      if r & 1:
        r_val = self.combine_f(self.node[r - 1], r_val)
      l >>= 1
      r >>= 1
    return self.combine_f(l_val, r_val)

def mkst():
  d = [N] * N
  j = 1
  for i in range(N - 1):
    while j < N and A[i] * 2 > A[j]:
      j += 1
    if j == N:
      break
    d[i] = j - i
  return SegTree(0, max, d)

def bin_search(l, r):
  left, right = 0, (r - l) // 2 + 1
  while left + 1 < right:
    k = (left + right) // 2
    if st.query(l, l + k) <= r - l - k:
      left = k
    else:
      right = k
  return left

N = int(input())
A = list(map(int, input().split()))
st = mkst()
Q = int(input())
ans = [0] * Q
for q in range(Q):
  l, r = map(int, input().split())
  ans[q] = bin_search(l - 1, r)
print("\n".join(map(str, ans)))