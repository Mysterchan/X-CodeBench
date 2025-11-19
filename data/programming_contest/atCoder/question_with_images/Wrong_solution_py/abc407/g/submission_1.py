import sys

int1 = lambda x: int(x)-1
pDB = lambda *x: print(*x, end="\n", file=sys.stderr)
p2D = lambda x: print(*x, sep="\n", end="\n\n", file=sys.stderr)
def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def SI(): return sys.stdin.readline().rstrip()

dij = [(0, 1), (-1, 0), (0, -1), (1, 0)]

inf = -1-(-1 << 62)

md = 998244353

from typing import NamedTuple, Optional, List, Tuple, cast
from heapq import heappush, heappop

class MCFGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int
        cost: int

    class _Edge:
        def __init__(self, dst: int, cap: int, cost: int) -> None:
            self.dst = dst
            self.cap = cap
            self.cost = cost
            self.rev: Optional[MCFGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MCFGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MCFGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int, cost: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MCFGraph._Edge(dst, cap, cost)
        re = MCFGraph._Edge(src, 0, -cost)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(MCFGraph._Edge, e.rev)
        return MCFGraph.Edge(
            re.dst,
            e.dst,
            e.cap+re.cap,
            re.cap,
            e.cost
        )

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def flow(self, s: int, t: int,
             flow_limit: Optional[int] = None) -> Tuple[int, int]:
        return self.slope(s, t, flow_limit)[-1]

    def slope(self, s: int, t: int,
              flow_limit: Optional[int] = None) -> List[Tuple[int, int]]:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = cast(int, sum(e.cap for e in self._g[s]))

        dual = [0]*self._n
        prev: List[Optional[Tuple[int, MCFGraph._Edge]]] = [None]*self._n

        def refine_dual() -> bool:
            pq = [(0, s)]
            visited = [False]*self._n
            dist: List[Optional[int]] = [None]*self._n
            dist[s] = 0
            while pq:
                dist_v, v = heappop(pq)
                if visited[v]:
                    continue
                visited[v] = True
                if v == t:
                    break
                dual_v = dual[v]
                for e in self._g[v]:
                    w = e.dst
                    if visited[w] or e.cap == 0:
                        continue
                    reduced_cost = e.cost-dual[w]+dual_v
                    new_dist = dist_v+reduced_cost
                    dist_w = dist[w]
                    if dist_w is None or new_dist < dist_w:
                        dist[w] = new_dist
                        prev[w] = v, e
                        heappush(pq, (new_dist, w))
            else:
                return False
            dist_t = dist[t]
            for v in range(self._n):
                if visited[v]:
                    dual[v] -= cast(int, dist_t)-cast(int, dist[v])
            return True

        flow = 0
        cost = 0
        prev_cost_per_flow: Optional[int] = None
        result = [(flow, cost)]
        while flow < flow_limit:
            if not refine_dual():
                break
            f = flow_limit-flow
            v = t
            while prev[v] is not None:
                u, e = cast(Tuple[int, MCFGraph._Edge], prev[v])
                f = min(f, e.cap)
                v = u
            v = t
            while prev[v] is not None:
                u, e = cast(Tuple[int, MCFGraph._Edge], prev[v])
                e.cap -= f
                assert e.rev is not None
                e.rev.cap += f
                v = u
            c = -dual[s]
            flow += f
            cost += f*c
            if c == prev_cost_per_flow:
                result.pop()
            result.append((flow, cost))
            prev_cost_per_flow = c
        return result

base=2*10**12

h,w=LI()
aa=LLI(h)

s=h*w
t=s+1
mf=MCFGraph(h*w+2)
tot=0
for i in range(h):
    for j,a in enumerate(aa[i]):
        tot+=a
        u=i*w+j
        if (i+j)&1:
            mf.add_edge(u,t,1,0)
        else:
            mf.add_edge(s,u,1,0)
            for di, dj in dij:
                ni, nj = i+di, j+dj
                if ni < 0 or nj < 0 or ni >= h or nj >= w: continue
                if a+aa[ni][nj]<0:
                    v=ni*w+nj
                    mf.add_edge(u,v,1,base+a+aa[ni][nj])
res=mf.slope(s,t)

ans=tot
f,c=res[0]
for nf,nc in res[1:]:
    df,dc=nf-f,nc-c
    for _ in range(nf-f):
        ans=max(ans,tot+(base*f-c))
        f+=df
        c+=dc
    f,c=nf,nc
print(ans)