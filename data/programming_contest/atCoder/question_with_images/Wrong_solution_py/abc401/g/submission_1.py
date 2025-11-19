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

def compute_dist(u, v):
  return ((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2) ** 0.5

def is_possible(x):
  G = Dinic(N * 2 + 2)
  source = N * 2
  sink = source + 1
  for u in range(N):
    G.add_edge(source, u, 1)
    G.add_edge(u + N, sink, 1)
    for v in range(N, N * 2):
      if D[u][v - N] <= x:
        G.add_edge(u, v, 1)
  return G.max_flow(source, sink, N + 1) == N

def bin_search(left, right, times):
  for _ in range(times):
    mid = (left + right) // 2
    if is_possible(mid):
      right = mid
    else:
      left = mid
  return right

N = int(input())
T = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(N)]
D = [[compute_dist(t, b) for b in B] for t in T]

ans = bin_search(0, (2 ** 0.51) * (10 ** 18), 100)
print(ans)