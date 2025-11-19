import sys
import typing
sys.setrecursionlimit(10**8)
sys.set_int_max_str_digits(0)
INF = 10**18
from collections import deque
class FenwickTree:

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s

def EulerTour(n, graph, root):

    par = [-1] * n
    stack = [~root, root]
    curr_time = -1
    tour = []
    in_time = [-1] * n
    out_time = [-1] * n

    while stack:
        pos = stack.pop()
        curr_time += 1

        if pos >= 0:
            tour.append(pos)
            if in_time[pos] == -1:
                in_time[pos] = curr_time

            for nex in graph[pos]:
                if nex == par[pos]:
                    continue
                par[nex] = pos
                stack.append(~nex)
                stack.append(nex)

        elif pos < 0:
            out_time[~pos] = curr_time
            if par[~pos] != -1:
                tour.append(par[~pos])

    return tour, in_time, out_time

N = int(input())
G = [list() for _ in range(N)]
graph = [list() for _ in range(N)]
for i in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, i))
    G[v].append((u, i))
    graph[u].append(v)
    graph[v].append(u)

dist = [-1] * N
dist[0] = 0
hen = [-1] * (N - 1)
que = deque([0])
while que:
    pos = que.popleft()
    for nex, henid in G[pos]:
        if dist[nex] == -1:

            hen[henid] = nex
            dist[nex] = dist[pos] + 1
            que.append(nex)

tour, in_time, out_time = EulerTour(N, graph, 0)

L = len(tour)
ft = FenwickTree(L)
for i in range(N):
    pos = in_time[i]
    ft.add(pos, 1)

Q = int(input())
total = N
ansl = []
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x, w = q[1], q[2]
        x -= 1
        total += w

        ft.add(in_time[x], w)
    else:
        y = q[1]
        y -= 1

        pos = hen[y]

        l, r = in_time[pos], out_time[pos]
        bubungi_weight = ft.sum(l, r + 1)
        nokori_weight = total - bubungi_weight
        diff = abs(bubungi_weight - nokori_weight)
        ansl.append(diff)

print(*ansl, sep='\n')