import sys
import threading
def main():
    import sys
    from collections import deque

    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    N = int(input())
    C = [input().strip() for _ in range(N)]
    # Map labels 'a'-'z' to 0-25
    # Build bitsets: in_bits[c][v] = bitset of u where u->v label c
    #             out_bits[c][u] = bitset of v where u->v label c
    in_bits = [[0] * N for _ in range(26)]
    out_bits = [[0] * N for _ in range(26)]
    for u in range(N):
        row = C[u]
        for v, ch in enumerate(row):
            if ch != '-':
                c = ord(ch) - 97
                out_bits[c][u] |= (1 << v)
                in_bits[c][v] |= (1 << u)
    # Precompute label masks per node
    in_label_mask = [0] * N
    out_label_mask = [0] * N
    for u in range(N):
        m = 0
        for c in range(26):
            if in_bits[c][u]:
                m |= 1 << c
        in_label_mask[u] = m
        m = 0
        for c in range(26):
            if out_bits[c][u]:
                m |= 1 << c
        out_label_mask[u] = m

    mask_all = (1 << N) - 1

    def bfs_rev(initial):
        dist = [[-1] * N for _ in range(N)]
        visited = [0] * N  # visited[u] is bitset of v's visited
        dq = deque()
        # initialize
        for u, v in initial:
            if not (visited[u] >> v) & 1:
                visited[u] |= (1 << v)
                dist[u][v] = 0
                dq.append((u, v))
        # BFS
        while dq:
            up, vp = dq.popleft()
            dp = dist[up][vp]
            # labels that can match: in_edges into up and out_edges from vp
            lm = in_label_mask[up] & out_label_mask[vp]
            while lm:
                cb = lm & -lm
                lm ^= cb
                c = (cb.bit_length() - 1)
                in_set = in_bits[c][up]    # u where u->up label c
                out_set = out_bits[c][vp]  # v where vp->v label c
                # For each u in in_set:
                x = in_set
                while x:
                    ub = x & -x
                    x ^= ub
                    u = ub.bit_length() - 1
                    # new vs = out_set minus already visited
                    new_vs = out_set & (~visited[u] & mask_all)
                    if new_vs:
                        # mark all
                        y = new_vs
                        while y:
                            vb = y & -y
                            y ^= vb
                            v = vb.bit_length() - 1
                            visited[u] |= (1 << v)
                            dist[u][v] = dp + 1
                            dq.append((u, v))
        return dist

    # Even-length palindromes: targets are (x,x)
    initial_even = [(i, i) for i in range(N)]
    dist_even = bfs_rev(initial_even)
    # Odd-length palindromes: targets are edges (u,v) with any label
    initial_odd = []
    for u in range(N):
        # out_bits[c][u] bits are v's
        # union all labels
        bs = 0
        for c in range(26):
            bs |= out_bits[c][u]
        x = bs
        while x:
            vb = x & -x
            x ^= vb
            v = vb.bit_length() - 1
            initial_odd.append((u, v))
    dist_odd = bfs_rev(initial_odd)

    # Output answers
    out = []
    for i in range(N):
        row = []
        for j in range(N):
            ans = -1
            de = dist_even[i][j]
            if de >= 0:
                ans = 2 * de
            do = dist_odd[i][j]
            if do >= 0:
                v = 2 * do + 1
                if ans < 0 or v < ans:
                    ans = v
            row.append(str(ans))
        out.append(" ".join(row))
    print("\n".join(out))


if __name__ == "__main__":
    main()