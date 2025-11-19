def solve():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(n)]

    # Floyd-Warshall to get all pairs shortest paths
    dist = C
    for mid in range(n):
        d_mid = dist[mid]
        for i in range(n):
            d_i = dist[i]
            via = d_i[mid]
            for j in range(n):
                nd = via + d_mid[j]
                if nd < d_i[j]:
                    d_i[j] = nd

    # Precompute Steiner tree DP for all subsets of terminals 1..K
    # Terminals: 0..k-1 fixed
    # For queries, we add s and t terminals (indices >= k)
    # We'll precompute dp for subsets of terminals 0..k-1 only,
    # then for each query, merge s and t terminals efficiently.

    INF = 10**15
    max_mask = 1 << k

    # dp[mask][v]: minimal cost to connect terminals in mask ending at vertex v
    dp = [[INF] * n for _ in range(max_mask)]
    for i in range(k):
        for v in range(n):
            dp[1 << i][v] = dist[i][v]

    # Merge subsets using subset DP + Dijkstra-like relaxation
    for mask in range(1, max_mask):
        # Skip singletons, already initialized
        if (mask & (mask - 1)) == 0:
            continue

        # Combine smaller subsets
        submask = (mask - 1) & mask
        while submask:
            other = mask ^ submask
            if other:
                dp_sub = dp[submask]
                dp_oth = dp[other]
                for v in range(n):
                    val = dp_sub[v] + dp_oth[v]
                    if val < dp[mask][v]:
                        dp[mask][v] = val
            submask = (submask - 1) & mask

        # Relax dp[mask] with dist using Dijkstra-like approach
        # Use a simple queue since dist is dense and n is small
        # But to be safe, use a heap for efficiency
        import heapq
        pq = []
        dist_mask = dp[mask]
        for v in range(n):
            if dist_mask[v] < INF:
                heapq.heappush(pq, (dist_mask[v], v))

        while pq:
            cost, v = heapq.heappop(pq)
            if cost > dist_mask[v]:
                continue
            d_v = dist[v]
            for u in range(n):
                nd = cost + d_v[u]
                if nd < dist_mask[u]:
                    dist_mask[u] = nd
                    heapq.heappush(pq, (nd, u))

    # For queries, terminals are fixed: 0..k-1 plus s and t
    # We want minimal Steiner tree connecting these terminals.
    # We can use the precomputed dp for terminals 0..k-1,
    # then add s and t terminals by merging their singletons.

    q = int(input())
    # Precompute dp for singletons s and t on the fly:
    # dp_single[v] = dist[s][v] or dist[t][v]

    # To speed up queries, precompute dp_single for all vertices >= k
    # dp_single_s[v] = dist[s][v]
    # dp_single_t[v] = dist[t][v]

    # We'll do the following for each query:
    # Let base_mask = (1<<k) -1
    # For terminals s and t, create dp_single arrays
    # Then merge dp[base_mask], dp_single_s, dp_single_t similarly to subset DP

    # To avoid recomputing merges for each query, we do:
    # result = min over v of dp[base_mask][v] + dist[v][s] + dist[v][t]
    # But this is not correct because Steiner tree must connect s and t as terminals.

    # Instead, we do a small DP over 4 subsets:
    # subsets of {base_mask, s, t}:
    # We have dp for base_mask, and singletons for s and t.
    # Merge base_mask and s -> dp1
    # Merge dp1 and t -> dp2
    # Result = min(dp2)

    # Implement merging function for two dp arrays:
    def merge_dp(dpA, dpB):
        res = [INF] * n
        for v in range(n):
            val = dpA[v] + dpB[v]
            if val < res[v]:
                res[v] = val
        # Relax with dist
        import heapq
        pq = []
        for v in range(n):
            if res[v] < INF:
                heapq.heappush(pq, (res[v], v))
        while pq:
            cost, v = heapq.heappop(pq)
            if cost > res[v]:
                continue
            d_v = dist[v]
            for u in range(n):
                nd = cost + d_v[u]
                if nd < res[u]:
                    res[u] = nd
                    heapq.heappush(pq, (nd, u))
        return res

    base_mask = max_mask - 1
    dp_base = dp[base_mask]

    for _ in range(q):
        s, t = map(int, input().split())
        s -= 1
        t -= 1

        # dp_single arrays for s and t terminals
        dp_s = dist[s][:]
        dp_t = dist[t][:]

        # Merge base_mask and s
        dp_bs = merge_dp(dp_base, dp_s)
        # Merge result and t
        dp_bst = merge_dp(dp_bs, dp_t)

        print(min(dp_bst))


if __name__ == "__main__":
    solve()