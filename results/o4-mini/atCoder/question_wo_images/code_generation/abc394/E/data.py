import sys
import threading
def main():
    import sys
    import heapq

    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    N = int(input().strip())
    C = [input().strip() for _ in range(N)]

    # We'll work 0-based internally.
    # Build in_edges and out_edges per node per character.
    # in_edges[v][c] = list of u such that u->v label c
    # out_edges[u][c] = list of v such that u->v label c
    in_edges = [[[] for _ in range(26)] for _ in range(N)]
    out_edges = [[[] for _ in range(26)] for _ in range(N)]
    in_mask = [0] * N
    out_mask = [0] * N

    for u in range(N):
        row = C[u]
        for v, ch in enumerate(row):
            if ch != '-':
                c = ord(ch) - 97
                out_edges[u][c].append(v)
                out_mask[u] |= (1 << c)
                in_edges[v][c].append(u)
                in_mask[v] |= (1 << c)

    INF = 10**9
    # dist[u*N + v] = shortest palindrome length from u to v
    dist = [INF] * (N * N)
    hq = []

    # Initial states: empty palindrome at (u,u) cost 0
    for u in range(N):
        idx = u * N + u
        dist[idx] = 0
        hq.append((0, idx))
    # Single-edge palindromes: (u->v) edges cost 1
    for u in range(N):
        for c in range(26):
            for v in out_edges[u][c]:
                idx = u * N + v
                if dist[idx] > 1:
                    dist[idx] = 1
                    hq.append((1, idx))

    heapq.heapify(hq)

    while hq:
        d, idx = heapq.heappop(hq)
        if d > dist[idx]:
            continue
        u_prime = idx // N
        v_prime = idx - u_prime * N
        # Try to extend palindrome by matching edges at both ends
        # we look for c s.t. exists u->u' and v'->v with same c
        m = in_mask[u_prime] & out_mask[v_prime]
        # iterate over set bits in m
        while m:
            lb = m & -m
            c = (lb.bit_length() - 1)
            m -= lb
            list_u = in_edges[u_prime][c]
            list_v = out_edges[v_prime][c]
            nd = d + 2
            # relax all pairs u in list_u, v in list_v
            for u in list_u:
                base = u * N
                for v in list_v:
                    ni = base + v
                    if nd < dist[ni]:
                        dist[ni] = nd
                        heapq.heappush(hq, (nd, ni))

    # Output
    out = []
    for i in range(N):
        row = []
        base = i * N
        for j in range(N):
            v = dist[base + j]
            if v >= INF:
                row.append("-1")
            else:
                row.append(str(v))
        out.append(" ".join(row))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()