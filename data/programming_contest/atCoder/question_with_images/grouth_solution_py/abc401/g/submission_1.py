from collections import deque

class Dinic:

  def __init__(self, n):
    self.n = n
    self.graph = [[] for _ in range(n)]
    self.dist = [-1] * n
    self.e_idx = [0] * n

  class Edge:

    def __init__(self, to, cap, rev):
      self.to = to
      self.cap = cap
      self.rev = rev

    def change_cap(self, val):
      self.cap += val

  def add_edge(self, u, v, cap):
    from_idx = len(self.graph[u])
    to_idx = len(self.graph[v])
    self.graph[u].append(self.Edge(v, cap, to_idx))
    self.graph[v].append(self.Edge(u, 0, from_idx))

  def run_flow(self, edge, flow):
    r_edge = self.graph[edge.to][edge.rev]
    edge.change_cap(-flow)
    r_edge.change_cap(flow)

  def calc_dist(self, source):
    q = deque([source])
    self.dist[source] = 0
    while q:
      cur = q.popleft()
      for e in self.graph[cur]:
        if not e.cap or self.dist[e.to] >= 0:
          continue
        self.dist[e.to] = self.dist[cur] + 1
        q.append(e.to)

  def ips(self, cur, sink, flow):
    if cur == sink:
      return flow
    for idx in range(self.e_idx[cur], len(self.graph[cur])):
      self.e_idx[cur] = idx
      e = self.graph[cur][idx]
      if self.dist[e.to] <= self.dist[cur] or not e.cap:
        continue
      inc = self.ips(e.to, sink, min(flow, e.cap))
      if inc:
        self.run_flow(e, inc)
        return inc
    return 0

  def max_flow(self, source, sink, INF=float("inf")):
    flow = 0
    while 1:
      self.dist = [-1] * self.n
      self.calc_dist(source)
      if self.dist[sink] < 0:
        return flow
      self.e_idx = [0] * self.n
      while 1:
        inc = self.ips(source, sink, INF)
        if not inc:
          break
        flow += inc

def mkxy(N):
  x, y = [0] * N, [0] * N
  for i in range(N):
    x[i], y[i] = map(int, input().split())
  return x, y

def compute_dist(u, v):
  return ((TX[u] - BX[v]) ** 2 + (TY[u] - BY[v]) ** 2) ** 0.5

def is_possible(target):
  G = Dinic(V)
  source, sink = V - 2, V - 1
  for u in range(N):
    G.add_edge(source, u, 1)
    G.add_edge(u + N, sink, 1)
    for v in range(N):
      if dist[u][v] <= target:
        G.add_edge(u, v + N, 1)
  return G.max_flow(source, sink, 2) == N

def bin_search(left, right):
  while left + 1 < right:
    mid = (left + right) // 2
    if is_possible(ds[mid]):
      right = mid
    else:
      left = mid
  return ds[right]

N = int(input())
TX, TY = mkxy(N)
BX, BY = mkxy(N)
V = N * 2 + 2
dist = [[compute_dist(u, v) for v in range(N)] for u in range(N)]
ds = set()
for row in dist:
  ds |= set(row)
ds = list(ds)
ds.sort()
ans = bin_search(0, len(ds))
print(ans)