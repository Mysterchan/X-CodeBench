import sys
import math
from collections import deque

input = sys.stdin.readline

class Dinic:
    __slots__ = ['n', 'graph', 'dist', 'e_idx']

    class Edge:
        __slots__ = ['to', 'cap', 'rev']

        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.dist = [-1] * n
        self.e_idx = [0] * n

    def add_edge(self, u, v, cap):
        self.graph[u].append(self.Edge(v, cap, len(self.graph[v])))
        self.graph[v].append(self.Edge(u, 0, len(self.graph[u]) - 1))

    def bfs(self, source, sink):
        dist = self.dist
        graph = self.graph
        for i in range(self.n):
            dist[i] = -1
        dist[source] = 0
        q = deque([source])
        while q:
            cur = q.popleft()
            for e in graph[cur]:
                if e.cap > 0 and dist[e.to] < 0:
                    dist[e.to] = dist[cur] + 1
                    q.append(e.to)
        return dist[sink] >= 0

    def dfs(self, cur, sink, flow):
        if cur == sink:
            return flow
        graph = self.graph
        dist = self.dist
        e_idx = self.e_idx
        while e_idx[cur] < len(graph[cur]):
            e = graph[cur][e_idx[cur]]
            if e.cap > 0 and dist[e.to] == dist[cur] + 1:
                pushed = self.dfs(e.to, sink, min(flow, e.cap))
                if pushed > 0:
                    e.cap -= pushed
                    graph[e.to][e.rev].cap += pushed
                    return pushed
            e_idx[cur] += 1
        return 0

    def max_flow(self, source, sink):
        flow = 0
        INF = 10**18
        dist = self.dist
        while self.bfs(source, sink):
            self.e_idx = [0] * self.n
            while True:
                pushed = self.dfs(source, sink, INF)
                if pushed == 0:
                    break
                flow += pushed
        return flow

def mkxy(N):
    x = [0]*N
    y = [0]*N
    for i in range(N):
        xi, yi = map(int, input().split())
        x[i] = xi
        y[i] = yi
    return x, y

def is_possible(t):
    t2 = t*t
    G = Dinic(V)
    for u in range(N):
        G.add_edge(source, u, 1)
        G.add_edge(u+N, sink, 1)
    for u in range(N):
        sx, sy = TX[u], TY[u]
        for v in range(N):
            dx = sx - BX[v]
            dy = sy - BY[v]
            dist2 = dx*dx + dy*dy
            if dist2 <= t2:
                G.add_edge(u, v+N, 1)
    return G.max_flow(source, sink) == N

N = int(input())
TX, TY = mkxy(N)
BX, BY = mkxy(N)
V = 2*N + 2
source = V - 2
sink = V - 1

left = 0.0
right = 2e18  # large enough upper bound

for _ in range(90):
    mid = (left + right) * 0.5
    if is_possible(mid):
        right = mid
    else:
        left = mid

print(right)