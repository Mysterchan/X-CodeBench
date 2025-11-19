import sys
import threading
def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it)); K = int(next(it))
    # Read cost matrix, 0-based
    C = [ [0]*N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            C[i][j] = int(next(it))
    # Floyd-Warshall for all-pairs shortest paths
    dist = C
    for k in range(N):
        dk = dist[k]
        for i in range(N):
            di = dist[i]
            ik = di[k]
            # Unroll inner loop for speed
            for j in range(N):
                v = ik + dk[j]
                if v < di[j]:
                    di[j] = v
    # Precompute Steiner DP for base terminals {0..K-1}
    INF = 10**40
    full_mask = (1<<K) - 1
    # dp[mask][v]: min cost to connect terminals in mask, tree ending at v (closed w.r.t dist)
    # Only store dp for all masks
    dp = [ [INF]*N for _ in range(1<<K) ]
    # Base: single terminal masks
    for t in range(K):
        d_t = dist[t]
        m = 1<<t
        row = dp[m]
        # dp[m][v] = dist[t][v]
        for v in range(N):
            row[v] = d_t[v]
    # Process masks
    for mask in range(1, full_mask+1):
        # skip single-bit masks
        if mask & (mask-1):
            row = dp[mask]
            # split mask into two non-empty parts
            # iterate submasks
            sub = (mask-1) & mask
            while sub:
                other = mask ^ sub
                if other:
                    row_sub = dp[sub]; row_ot = dp[other]
                    # combine at each v
                    for v in range(N):
                        s = row_sub[v] + row_ot[v]
                        if s < row[v]:
                            row[v] = s
                sub = (sub-1) & mask
            # closure: row[v] = min_u dp[mask][u] + dist[u][v]
            # copy old row
            old = row[:]  # snapshot
            # for each u
            for u in range(N):
                ou = old[u]
                du = dist[u]
                # update row[v]
                for v in range(N):
                    s = ou + du[v]
                    if s < row[v]:
                        row[v] = s
    # f_base is dp[full_mask]
    f_base = dp[full_mask]
    # Precompute g_w for each extra terminal w = K..N-1
    n_ex = N - K
    g_list = [None] * n_ex
    for ex in range(n_ex):
        w = K + ex
        row = [0]*N
        dbw = dist[w]
        # initial g_w[v] = f_base[v] + dist[w][v]
        for v in range(N):
            row[v] = f_base[v] + dbw[v]
        # closure on row
        old = row[:]  # snapshot
        # for each u
        for u in range(N):
            ou = old[u]
            du = dist[u]
            for v in range(N):
                s = ou + du[v]
                if s < row[v]:
                    row[v] = s
        g_list[ex] = row
    # Precompute answers for each pair of extras
    ans_mat = [ [0]*n_ex for _ in range(n_ex) ]
    for i in range(n_ex):
        gi = g_list[i]
        for j in range(i+1, n_ex):
            gj = g_list[j]
            # g2[v] = gi[v] + gj[v] - f_base[v]
            g2 = [0]*N
            for v in range(N):
                g2[v] = gi[v] + gj[v] - f_base[v]
            # closure on g2
            old2 = g2[:]
            for u in range(N):
                ou = old2[u]
                du = dist[u]
                for v in range(N):
                    s = ou + du[v]
                    if s < g2[v]:
                        g2[v] = s
            # answer is min_v g2[v]
            mv = g2[0]
            for v in range(1, N):
                if g2[v] < mv:
                    mv = g2[v]
            ans_mat[i][j] = mv
            ans_mat[j][i] = mv
    # Process queries
    Q = int(next(it))
    out = []
    for _ in range(Q):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        i = s - K; j = t - K
        if i<0 or j<0:
            # s or t in base range => trivial?
            # But by problem, s,t in [K..N-1], so won't happen
            out.append("0")
        else:
            out.append(str(ans_mat[i][j]))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()