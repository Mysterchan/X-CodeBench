import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    N, K = map(int, sys.stdin.readline().split())
    C = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    Q = int(sys.stdin.readline())
    queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(Q)]

    # Step 1: Compute all-pairs shortest paths (Floyd-Warshall)
    dist = [row[:] for row in C]
    for k in range(N):
        d_k = dist[k]
        for i in range(N):
            d_i = dist[i]
            ik = d_i[k]
            for j in range(N):
                val = ik + d_k[j]
                if val < d_i[j]:
                    d_i[j] = val

    # We want to find minimal Steiner tree connecting:
    # fixed terminals: 1..K (0-based: 0..K-1)
    # plus two terminals s_i, t_i (each in [K..N-1])

    # K <= 8, so number of fixed terminals is small.
    # We'll precompute Steiner tree DP for all subsets of fixed terminals plus one extra terminal.
    # Then for each query, combine results.

    # Precompute Steiner tree DP for fixed terminals only:
    # terminals: 0..K-1
    # We'll build dp_fixed[mask][v]: minimal cost to connect terminals in mask ending at v
    # Then extend to include one extra terminal x.

    # To handle queries efficiently:
    # For each node v, we compute dp_fixed[mask][v] for mask in [1..(1<<K)-1]
    # Then for each query (s,t), we find minimal Steiner tree connecting fixed terminals + s + t.

    # But s,t vary per query, so we need a method to quickly answer queries.

    # Idea:
    # Precompute dp_fixed[mask][v] for fixed terminals only.
    # For each node v, dp_fixed[(1<<K)-1][v] = minimal cost to connect all fixed terminals ending at v.

    # Then for each query (s,t):
    # We want minimal Steiner tree connecting fixed terminals + s + t.
    # This is equivalent to minimal Steiner tree connecting fixed terminals plus two extra terminals s,t.

    # We can use the following approach:
    # For each query:
    # - Consider the set of terminals: fixed terminals + s + t
    # - We want minimal Steiner tree connecting these terminals.

    # Since K <= 8, total terminals per query = K+2 <= 10.
    # We can run Steiner tree DP per query on these terminals.

    # But Q can be up to 5000, and N=80, so running full DP per query is expensive.

    # Optimization:
    # We can precompute shortest paths between all nodes.
    # Then for each query, run Steiner tree DP on the induced complete graph of terminals:
    # terminals = fixed terminals + s + t
    # The complete graph on terminals has edge weights = shortest path distances in original graph.

    # Since terminals <= 10, DP size = 2^(K+2)* (K+2) <= 1024*10 = 10k per query, which is feasible for Q=5000.

    # Implementation details:
    # For each query:
    # - terminals = [0..K-1] + [s-1, t-1]
    # - Build dist_term[i][j] = dist[terminals[i]][terminals[j]]
    # - Run Steiner DP on this small complete graph.

    # Steiner DP:
    # dp[mask][i] = minimal cost to connect terminals in mask ending at terminal i
    # Initialization:
    # dp[1<<i][i] = 0
    # Transition:
    # For mask, for subset submask of mask:
    # dp[mask][i] = min over j in mask\{i} of dp[submask][j] + dp[mask^submask][i] + dist_term[j][i]
    # But this is O(3^t), too slow.

    # Instead, use standard Steiner DP:
    # For mask in increasing order:
    #   For i in terminals:
    #     For j in terminals:
    #       if mask & (1<<j) == 0:
    #         dp[mask | (1<<j)][j] = min(dp[mask | (1<<j)][j], dp[mask][i] + dist_term[i][j])

    # This is O(t * 2^t * t) = O(t^2 * 2^t), with t <= 10, about 100k operations per query, 5000 queries = 5*10^8 operations, might be borderline but possibly okay with fast IO and PyPy.

    # We'll implement this approach.

    # Preprocessing done: dist[][]

    # Prepare fixed terminals indices
    fixed = list(range(K))

    # Process queries
    out = []
    for s, t in queries:
        s -= 1
        t -= 1
        terminals = fixed + [s, t]
        t_len = len(terminals)
        dist_term = [[0]*t_len for _ in range(t_len)]
        for i in range(t_len):
            for j in range(t_len):
                dist_term[i][j] = dist[terminals[i]][terminals[j]]

        INF = 10**15
        dp = [[INF]*t_len for _ in range(1<<t_len)]
        for i in range(t_len):
            dp[1<<i][i] = 0

        for mask in range(1, 1<<t_len):
            for u in range(t_len):
                if dp[mask][u] == INF:
                    continue
                for v in range(t_len):
                    if (mask & (1<<v)) == 0:
                        val = dp[mask][u] + dist_term[u][v]
                        if val < dp[mask | (1<<v)][v]:
                            dp[mask | (1<<v)][v] = val

        full_mask = (1<<t_len) - 1
        ans = min(dp[full_mask])
        out.append(str(ans))

    print('\n'.join(out))


threading.Thread(target=main).start()