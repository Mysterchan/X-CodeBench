def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, k = map(int, data[0].split())
    
    C = []
    for i in range(1, n + 1):
        C.append(list(map(int, data[i].split())))

    # Apply Floyd-Warshall to compute shortest paths
    for m in range(n):
        for i in range(n):
            for j in range(n):
                if C[i][m] + C[m][j] < C[i][j]:
                    C[i][j] = C[i][m] + C[m][j]

    q = int(data[n + 1])
    results = []
    
    for i in range(q):
        s, t = map(int, data[n + 2 + i].split())
        
        s -= 1
        t -= 1
        
        # Collect all terminals
        terminals = list(range(k)) + [s, t]
        
        # Create a terminal set
        num_terminals = len(terminals)
        max_mask = 1 << num_terminals
        
        INF = float('inf')
        dp = [[INF] * n for _ in range(max_mask)]

        for i, terminal in enumerate(terminals):
            dp[1 << i][terminal] = 0

        for mask in range(max_mask):
            for submask in range(mask):
                if (submask | mask) == mask:  # submask is a subset of mask
                    complement = mask ^ submask
                    if complement > 0:
                        for v in range(n):
                            if dp[submask][v] < INF and dp[complement][v] < INF:
                                dp[mask][v] = min(dp[mask][v], dp[submask][v] + dp[complement][v])

            # Prim's-like update for current mask
            current_dist = dp[mask][:]
            for u in range(n):
                for v in range(n):
                    if current_dist[u] < INF:
                        new_cost = current_dist[u] + C[u][v]
                        if new_cost < current_dist[v]:
                            current_dist[v] = new_cost

            dp[mask] = current_dist

        result = min(dp[max_mask - 1])
        results.append(result)

    print('\n'.join(map(str, results)))

solve()