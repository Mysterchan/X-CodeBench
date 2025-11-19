import sys
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    C = [next(it).strip() for _ in range(N)]

    # Build adjacency by letter
    # in_edges[c][v]: list of u such that u -> v has label c
    # out_edges[c][v]: list of w such that v -> w has label c
    in_edges  = [[[] for _ in range(N)] for _ in range(26)]
    out_edges = [[[] for _ in range(N)] for _ in range(26)]
    incoming_mask = [0]*N
    outgoing_mask = [0]*N

    for u in range(N):
        row = C[u]
        for v, ch in enumerate(row):
            if ch != '-':
                ci = ord(ch) - 97
                out_edges[ci][u].append(v)
                in_edges[ci][v].append(u)
                outgoing_mask[u] |= (1 << ci)
                incoming_mask[v] |= (1 << ci)

    INF = 10**9
    total = N * N
    dist = [INF] * (total)

    # We'll use a simple list as queue with a head pointer
    queue = []
    head = 0

    # Initialize distances: zero-length palindromes at (i,i)
    for i in range(N):
        idx = i * N + i
        dist[idx] = 0
        queue.append(idx)

    # One-edge palindromes (single-character)
    for u in range(N):
        row = C[u]
        base = u * N
        for v, ch in enumerate(row):
            if ch != '-':
                idx = base + v
                if dist[idx] > 1:
                    dist[idx] = 1
                    queue.append(idx)

    # BFS over state-space of pairs (i,j) encoded as id = i*N + j
    while head < len(queue):
        curr = queue[head]
        head += 1
        d = dist[curr]
        i, j = divmod(curr, N)

        # Only letters that appear incoming to i and outgoing from j
        mask = incoming_mask[i] & outgoing_mask[j]
        # For each matching letter, expand by two edges
        while mask:
            low = mask & -mask
            c = low.bit_length() - 1
            ns = in_edges[c][i]
            ts = out_edges[c][j]
            nd = d + 2
            if ns and ts:
                for s in ns:
                    base_st = s * N
                    for t in ts:
                        nid = base_st + t
                        if dist[nid] > nd:
                            dist[nid] = nd
                            queue.append(nid)
            mask ^= low

    # Output the N x N result matrix
    out = []
    idx = 0
    for _ in range(N):
        row = []
        for _ in range(N):
            v = dist[idx]
            row.append(str(v if v < INF else -1))
            idx += 1
        out.append(" ".join(row))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()