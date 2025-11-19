import sys
import heapq

class Edge:
    __slots__ = ('to', 'rev', 'cap', 'cost')
    def __init__(self, to, rev, cap, cost):
        self.to = to
        self.rev = rev
        self.cap = cap
        self.cost = cost

def solve() -> None:
    input = sys.stdin.readline
    H, W = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    total = sum(sum(row) for row in board)

    left_id = [[-1] * W for _ in range(H)]
    right_id = [[-1] * W for _ in range(H)]
    L = R = 0
    for i in range(H):
        for j in range(W):
            if (i + j) & 1 == 0:
                left_id[i][j] = L
                L += 1
            else:
                right_id[i][j] = R
                R += 1

    N = 2 + L + R
    SOURCE = 0
    SINK = 1
    graph = [[] for _ in range(N)]

    def add_edge(fr: int, to: int, cap: int, cost: int) -> None:
        graph[fr].append(Edge(to, len(graph[to]), cap, cost))
        graph[to].append(Edge(fr, len(graph[fr]) - 1, 0, -cost))

    for i in range(L):
        add_edge(SOURCE, 2 + i, 1, 0)

    for i in range(R):
        add_edge(2 + L + i, SINK, 1, 0)

    for i in range(H):
        for j in range(W):
            if (i + j) & 1 == 0:
                u = left_id[i][j]
                w_u = board[i][j]
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < H and 0 <= nj < W and ((ni + nj) & 1):
                        v = right_id[ni][nj]
                        w_v = board[ni][nj]
                        cost = w_u + w_v
                        add_edge(2 + u, 2 + L + v, 1, cost)

    INF = 10 ** 30
    pot = [INF] * N
    pot[SOURCE] = 0
    for _ in range(N - 1):
        updated = False
        for v in range(N):
            if pot[v] == INF:
                continue
            for e in graph[v]:
                if e.cap > 0 and pot[e.to] > pot[v] + e.cost:
                    pot[e.to] = pot[v] + e.cost
                    updated = True
        if not updated:
            break

    flow = 0
    cost = 0
    max_flow = min(L, R)

    while flow < max_flow:
        dist = [INF] * N
        prevv = [-1] * N
        preve = [-1] * N
        dist[SOURCE] = 0
        pq = [(0, SOURCE)]

        while pq:
            d, v = heapq.heappop(pq)
            if dist[v] < d:
                continue
            for i, e in enumerate(graph[v]):
                if e.cap == 0:
                    continue
                nd = d + e.cost + pot[v] - pot[e.to]
                if dist[e.to] > nd:
                    dist[e.to] = nd
                    prevv[e.to] = v
                    preve[e.to] = i
                    heapq.heappush(pq, (nd, e.to))

        if dist[SINK] == INF:
            break

        for v in range(N):
            if dist[v] < INF:
                pot[v] += dist[v]

        path_cost = 0
        cur = SINK
        while cur != SOURCE:
            e = graph[prevv[cur]][preve[cur]]
            path_cost += e.cost
            cur = prevv[cur]

        if path_cost >= 0:
            break

        add = 1
        flow += add
        cost += add * path_cost

        cur = SINK
        while cur != SOURCE:
            e = graph[prevv[cur]][preve[cur]]
            e.cap -= add
            graph[cur][e.rev].cap += add
            cur = prevv[cur]

    answer = total - cost
    print(answer)

if __name__ == "__main__":
    solve()