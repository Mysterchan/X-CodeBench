import sys
import heapq
from collections import defaultdict
from typing import List, Tuple, Dict, Set

INF = 10 ** 30

def dijkstra(
    adj: List[List[Tuple[int, int, int]]],
    source: int,
    target: int,
    banned_nodes: Set[int],
    banned_edges: Set[int],
    weight_getter
) -> Tuple[int, List[int]]:
    n = len(adj)
    dist = [INF] * n
    prev_node = [-1] * n
    prev_edge = [-1] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        if u == target:
            break
        for v, eid, _ in adj[u]:
            if eid in banned_edges:
                continue
            if v in banned_nodes:
                continue
            nd = d + weight_getter(eid)
            if nd < dist[v]:
                dist[v] = nd
                prev_node[v] = u
                prev_edge[v] = eid
                heapq.heappush(heap, (nd, v))
    if target != -1:
        if dist[target] == INF:
            return INF, []
        edges = []
        cur = target
        while cur != source:
            eid = prev_edge[cur]
            if eid == -1:
                return INF, []
            edges.append(eid)
            cur = prev_node[cur]
        edges.reverse()
        return dist[target], edges
    else:
        return dist, None


def shortest_path_without_k(
    n: int,
    edges: List[Tuple[int, int, int, int]],
    k: int
) -> Tuple[int, List[int]]:
    adj = [[] for _ in range(n)]
    banned_nodes = {k - 1}
    for idx, (u, v, l, r) in enumerate(edges):
        if u - 1 == k - 1 or v - 1 == k - 1:
            continue
        adj[u - 1].append((v - 1, idx, l))
        adj[v - 1].append((u - 1, idx, l))
    def w_lower(eid):
        return edges[eid][2]

    dist, path_edges = dijkstra(adj, 0, n - 1, banned_nodes, set(), w_lower)
    return dist, path_edges


def paths_by_yen(
    n: int,
    edges: List[Tuple[int, int, int, int]],
    k: int,
    K: int
) -> List[List[int]]:
    adj = [[] for _ in range(n)]
    for idx, (u, v, l, r) in enumerate(edges):
        if u - 1 == k - 1 or v - 1 == k - 1:
            continue
        adj[u - 1].append((v - 1, idx, l))
        adj[v - 1].append((u - 1, idx, l))

    def w_lower(eid):
        return edges[eid][2]

    dist, P0 = dijkstra(adj, 0, n - 1, {k - 1}, set(), w_lower)
    if dist >= INF:
        return []
    paths = [P0]

    cand = []

    for i in range(1, K):
        last_path = paths[-1]
        for j in range(len(last_path)):
            root_edges = set(last_path[:j])
            banned_edges = set()
            for prev in paths:
                if len(prev) > j and prev[:j] == last_path[:j]:
                    banned_edges.add(prev[j])
            banned_nodes = {k - 1}
            cur = 0
            for eid in last_path[:j]:
                u, v, _, _ = edges[eid]
                u -= 1
                v -= 1
                if cur == u:
                    cur = v
                else:
                    cur = u
                banned_nodes.add(cur)

            spur_node = cur

            temp_banned_edges = set(banned_edges)
            dist_spur, spur_path = dijkstra(
                adj,
                spur_node,
                n - 1,
                banned_nodes,
                temp_banned_edges,
                w_lower
            )
            if dist_spur >= INF:
                continue
            total_len = dist_spur
            for eid in last_path[:j]:
                total_len += w_lower(eid)
            full_path = last_path[:j] + spur_path
            cand.append((total_len, full_path))

        if not cand:
            break
        cand.sort(key=lambda x: x[0])
        best_len, best_path = cand[0]
        if any(best_path == p for p in paths):
            cand.pop(0)
            continue
        paths.append(best_path)
        cand.pop(0)

    return paths


def solve_one(
    n: int,
    m: int,
    k: int,
    edges: List[Tuple[int, int, int, int]]
) -> bool:
    dist0, path0 = shortest_path_without_k(n, edges, k)
    if dist0 >= INF:
        return False

    candidates = paths_by_yen(n, edges, k, 5)
    if not any(path0 == c for c in candidates):
        candidates.insert(0, path0)

    full_adj = [[] for _ in range(n)]
    for idx, (u, v, l, r) in enumerate(edges):
        u -= 1
        v -= 1
        full_adj[u].append((v, idx, l))
        full_adj[v].append((u, idx, l))

    for P in candidates:
        L = 0
        on_path = [False] * m
        for eid in P:
            L += edges[eid][2]  # lower bound
            on_path[eid] = True

        def w(eid):
            return edges[eid][2] if on_path[eid] else edges[eid][3]

        dist1k, _ = dijkstra(full_adj, 0, k - 1, set(), set(), w)
        distkn, _ = dijkstra(full_adj, k - 1, n - 1, set(), set(), w)
        if dist1k >= INF or distkn >= INF:
            continue
        if L < dist1k + distkn:
            return True

    return False


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        k = int(next(it))
        edges = []
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            l = int(next(it))
            r = int(next(it))
            edges.append((u, v, l, r))
        ok = solve_one(n, m, k, edges)
        out_lines.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()
