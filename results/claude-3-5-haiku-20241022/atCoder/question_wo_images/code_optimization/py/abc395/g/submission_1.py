import heapq

def solve():
    n, k = map(int, input().split())

    C = []
    for i in range(n):
        row = list(map(int, input().split()))
        C.append(row)

    dist = [[C[i][j] for j in range(n)] for i in range(n)]

    for k_fw in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k_fw] + dist[k_fw][j] < dist[i][j]:
                    dist[i][j] = dist[i][k_fw] + dist[k_fw][j]

    INF = float('inf')
    
    # Precompute DP for base terminals (1 to k)
    base_terminals = list(range(k))
    num_base = k
    max_base_mask = 1 << num_base
    
    base_dp = [[INF] * n for _ in range(max_base_mask)]
    
    for i in range(num_base):
        base_dp[1 << i][base_terminals[i]] = 0
    
    for mask in range(1, max_base_mask):
        submask = mask
        while submask > 0:
            complement = mask ^ submask
            if complement > 0:
                for v in range(n):
                    if base_dp[submask][v] < INF and base_dp[complement][v] < INF:
                        base_dp[mask][v] = min(base_dp[mask][v], base_dp[submask][v] + base_dp[complement][v])
            submask = (submask - 1) & mask
        
        current_dist = base_dp[mask][:]
        pq = []
        
        for v in range(n):
            if current_dist[v] < INF:
                heapq.heappush(pq, (current_dist[v], v))
        
        while pq:
            cost, v = heapq.heappop(pq)
            if cost > current_dist[v]:
                continue
            
            for u in range(n):
                new_cost = cost + dist[v][u]
                if new_cost < current_dist[u]:
                    current_dist[u] = new_cost
                    heapq.heappush(pq, (new_cost, u))
        
        base_dp[mask][:] = current_dist
    
    cache = {}
    
    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        
        key = (min(s, t), max(s, t))
        if key in cache:
            print(cache[key])
            continue
        
        # Build DP for base + s + t
        num_terminals = k + 2
        max_mask = 1 << num_terminals
        
        dp = [[INF] * n for _ in range(max_mask)]
        
        # Initialize from base_dp
        full_base_mask = max_base_mask - 1
        for v in range(n):
            dp[full_base_mask][v] = base_dp[full_base_mask][v]
        
        # Add s
        s_bit = 1 << k
        dp[s_bit][s] = 0
        
        # Add t
        t_bit = 1 << (k + 1)
        dp[t_bit][t] = 0
        
        for mask in range(1, max_mask):
            if mask == s_bit or mask == t_bit or mask == full_base_mask:
                continue
            
            submask = mask
            while submask > 0:
                complement = mask ^ submask
                if complement > 0:
                    for v in range(n):
                        if dp[submask][v] < INF and dp[complement][v] < INF:
                            dp[mask][v] = min(dp[mask][v], dp[submask][v] + dp[complement][v])
                submask = (submask - 1) & mask
            
            current_dist = dp[mask][:]
            pq = []
            
            for v in range(n):
                if current_dist[v] < INF:
                    heapq.heappush(pq, (current_dist[v], v))
            
            while pq:
                cost, v = heapq.heappop(pq)
                if cost > current_dist[v]:
                    continue
                
                for u in range(n):
                    new_cost = cost + dist[v][u]
                    if new_cost < current_dist[u]:
                        current_dist[u] = new_cost
                        heapq.heappush(pq, (new_cost, u))
            
            dp[mask][:] = current_dist
        
        full_mask = max_mask - 1
        result = min(dp[full_mask])
        cache[key] = result
        print(result)

solve()