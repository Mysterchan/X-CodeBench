import sys

def solve():

    INF = float('inf')

    try:
        line = sys.stdin.readline()
        if not line: return
        N, K = map(int, line.split())
        C = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    except (IOError, ValueError):
        return

    dist = [row[:] for row in C]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    dp = [[INF] * N for _ in range(1 << K)]

    for k in range(K):
        dp[1 << k][k] = 0

    for mask in range(1, 1 << K):

        for i in range(N):
            submask = (mask - 1) & mask
            while submask > 0:
                comp_mask = mask ^ submask
                if dp[submask][i] != INF and dp[comp_mask][i] != INF:
                    dp[mask][i] = min(dp[mask][i], dp[submask][i] + dp[comp_mask][i])
                submask = (submask - 1) & mask

        for i in range(N):
            for j in range(N):
                if dp[mask][i] != INF:
                    dp[mask][j] = min(dp[mask][j], dp[mask][i] + dist[i][j])

    query_cost = [[INF] * N for _ in range(1 << K)]

    for v in range(K, N):
        query_cost[0][v] = 0

    for mask in range(1, 1 << K):
        for v in range(K, N):
            current_min = INF
            for i in range(N):
                if dp[mask][i] != INF:
                    current_min = min(current_min, dp[mask][i] + dist[i][v])
            query_cost[mask][v] = current_min

    try:
        Q = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    full_mask = (1 << K) - 1

    for _ in range(Q):
        s, t = map(int, sys.stdin.readline().split())
        s -= 1
        t -= 1

        min_total_cost = INF

        for submask in range(1 << K):
            comp_mask = full_mask ^ submask
            cost = query_cost[submask][s] + query_cost[comp_mask][t]
            min_total_cost = min(min_total_cost, cost)

        print(min_total_cost)

solve()