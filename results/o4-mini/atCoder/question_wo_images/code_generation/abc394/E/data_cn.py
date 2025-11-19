import sys
import threading
def main():
    import sys
    import heapq

    input = sys.stdin.readline
    N = int(input())
    C = [input().strip() for _ in range(N)]

    # Build adjacency by label: out_edges[u][c] = list of v where u->v has label c
    #                          in_edges[u][c] = list of v where v->u has label c
    # Labels mapped 0..25
    out_edges = [ [ [] for _ in range(26) ] for _ in range(N) ]
    in_edges  = [ [ [] for _ in range(26) ] for _ in range(N) ]
    in_labels = [ [] for _ in range(N) ]  # labels c present in in_edges[u]

    for u in range(N):
        row = C[u]
        for v, ch in enumerate(row):
            if ch != '-':
                ci = ord(ch) - 97
                out_edges[u][ci].append(v)
                in_edges[v][ci].append(u)

    # Precompute in_labels
    for u in range(N):
        lbls = []
        ie = in_edges[u]
        for c in range(26):
            if ie[c]:
                lbls.append(c)
        in_labels[u] = lbls

    INF = 10**9
    dist = [ [INF]*N for _ in range(N) ]
    # Priority queue for Dijkstra: (d, u, v)
    pq = []

    # Initial states: dist[u][u] = 0; for edges u->v: dist[u][v] = 1
    for u in range(N):
        dist[u][u] = 0
        heapq.heappush(pq, (0, u, u))
    for u in range(N):
        for c in range(26):
            for v in out_edges[u][c]:
                # edge u->v
                if dist[u][v] > 1:
                    dist[u][v] = 1
                    heapq.heappush(pq, (1, u, v))

    # Dijkstra
    while pq:
        d, u, v = heapq.heappop(pq)
        if d != dist[u][v]:
            continue
        # From state (u, v), wrap matching labels to go to (a, b)
        # For each label c that has in_edges to u
        for c in in_labels[u]:
            lst_a = in_edges[u][c]
            lst_b = out_edges[v][c]
            if not lst_b:
                continue
            nd = d + 2
            for a in lst_a:
                # iterate all b in lst_b
                row_dist_a = dist[a]
                for b in lst_b:
                    if row_dist_a[b] > nd:
                        row_dist_a[b] = nd
                        heapq.heappush(pq, (nd, a, b))

    # Output
    out = []
    for i in range(N):
        row = dist[i]
        line = []
        for j in range(N):
            v = row[j]
            if v >= INF:
                line.append("-1")
            else:
                line.append(str(v))
        out.append(" ".join(line))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()