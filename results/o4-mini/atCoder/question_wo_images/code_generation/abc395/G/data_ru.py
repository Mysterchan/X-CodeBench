import sys
import threading

def main():
    import sys
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    C = [ [0]*N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            C[i][j] = int(next(it))
    Q = int(next(it))
    queries = [ (int(next(it))-1, int(next(it))-1) for _ in range(Q) ]
    INF = 10**30
    maxmask = 1<<K
    # dp0[mask][v]: minimal cost to connect base-terminals in mask, ending at v
    dp0 = [ [INF]*N for _ in range(maxmask) ]
    # Initialize single-bit masks: shortest path distances from terminal i
    for i in range(K):
        mask = 1<<i
        dist = dp0[mask]
        # initialize with direct edges from terminal i
        ci = C[i]
        for v in range(N):
            dist[v] = ci[v]
        # Dijkstra to get all-pairs shortest from terminal i
        used = [False]*N
        for _ in range(N):
            u = -1
            du = INF
            # find min unused
            for x in range(N):
                if not used[x] and dist[x] < du:
                    du = dist[x]; u = x
            if u < 0:
                break
            used[u] = True
            cu = C[u]
            # relax neighbors
            nd = du
            for v in range(N):
                # dist[v] > dist[u] + C[u][v]
                tv = nd + cu[v]
                if tv < dist[v]:
                    dist[v] = tv
    full = (1<<K) - 1
    # Compute dp for all masks >=2 bits
    for mask in range(1, maxmask):
        if mask & (mask-1) == 0:
            continue  # skip single-bit, already done
        dist = dp0[mask]
        # merge submasks
        # iterate proper non-empty submasks
        sub = (mask-1) & mask
        while sub:
            other = mask ^ sub
            if other:
                dsub = dp0[sub]; doth = dp0[other]
                # combine at each v
                for v in range(N):
                    tv = dsub[v] + doth[v]
                    if tv < dist[v]:
                        dist[v] = tv
            sub = (sub-1) & mask
        # run Dijkstra on dist
        used = [False]*N
        for _ in range(N):
            u = -1
            du = INF
            for x in range(N):
                if not used[x] and dist[x] < du:
                    du = dist[x]; u = x
            if u < 0:
                break
            used[u] = True
            cu = C[u]
            nd = du
            for v in range(N):
                tv = nd + cu[v]
                if tv < dist[v]:
                    dist[v] = tv
    # Answer queries: ans = min_v dp0[full][v] + C[v][s] + C[v][t]
    dp_full = dp0[full]
    out = []
    for (s, t) in queries:
        best = INF
        # local references
        df = dp_full
        Cs = C[s]
        Ct = C[t]
        for v in range(N):
            tv = df[v] + Cs[v] + Ct[v]
            if tv < best:
                best = tv
        out.append(str(best))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()