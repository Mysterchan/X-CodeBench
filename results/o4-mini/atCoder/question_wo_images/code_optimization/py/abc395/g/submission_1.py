import sys
import threading
def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    INF = 10**30

    N = int(next(it))
    K = int(next(it))

    # Read cost matrix and compute all-pairs shortest paths (Floyd–Warshall)
    C = [ [0]*N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            C[i][j] = int(next(it))
    dist = C
    for m in range(N):
        dm = dist[m]
        for i in range(N):
            di = dist[i]
            via = di[m]
            for j in range(N):
                # relax dist[i][j] via m
                val = via + dm[j]
                if val < di[j]:
                    di[j] = val

    # Dreyfus–Wagner on the K base terminals (0..K-1)
    full_mask = (1<<K) - 1
    # dp[mask] is a list of length N
    dp = [None] * (1<<K)

    # Initialize single-bit masks
    for b in range(K):
        m = 1<<b
        arr = [INF]*N
        # cost to connect base terminal b to v is dist[b][v]
        db = dist[b]
        for v in range(N):
            arr[v] = db[v]
        dp[m] = arr

    # Build dp for all masks
    for mask in range(1, full_mask+1):
        if dp[mask] is not None:
            continue
        # merge submasks
        best = [INF]*N
        sub = (mask-1) & mask
        while sub:
            comp = mask ^ sub
            if comp:
                # to avoid duplicate work do only sub < comp
                if sub < comp:
                    dsub = dp[sub]
                    dcomp = dp[comp]
                    for v in range(N):
                        s = dsub[v] + dcomp[v]
                        if s < best[v]:
                            best[v] = s
            sub = (sub-1) & mask
        # now relax over dist: best'[u] = min_v(best[v] + dist[v][u])
        newdp = [INF]*N
        for v in range(N):
            bv = best[v]
            if bv < INF:
                dv = dist[v]
                bv_val = bv
                for u in range(N):
                    val = bv_val + dv[u]
                    if val < newdp[u]:
                        newdp[u] = val
        dp[mask] = newdp

    dp_full = dp[full_mask]

    # Precompute for each possible extra terminal s: 
    # g[s][u] = min_w(dp_full[w] + dist[w][s] + dist[w][u])
    g = [None]*N
    for s in range(K, N):
        gs = [INF]*N
        # for each w compute dp_full[w] + dist[w][s]
        # then add dist[w][u] to every u
        for w in range(N):
            dfw = dp_full[w]
            if dfw >= INF: continue
            dws = dist[w][s]
            base = dfw + dws
            dw = dist[w]
            for u in range(N):
                val = base + dw[u]
                if val < gs[u]:
                    gs[u] = val
        g[s] = gs

    # Answer queries
    out = []
    Q = int(next(it))
    for _ in range(Q):
        si = int(next(it)) - 1
        ti = int(next(it)) - 1
        gs = g[si]
        # answer = min_u(g_s[u] + dist[u][t])
        dt = dist  # alias
        d_t = dt[ti]
        ans = INF
        for u in range(N):
            v = gs[u] + d_t[u]
            if v < ans:
                ans = v
        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()