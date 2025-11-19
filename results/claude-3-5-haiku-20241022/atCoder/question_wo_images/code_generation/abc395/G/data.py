import sys
from heapq import heappush, heappop

def solve():
    input = sys.stdin.read().split()
    idx = 0
    
    N = int(input[idx])
    K = int(input[idx + 1])
    idx += 2
    
    C = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(input[idx]))
            idx += 1
        C.append(row)
    
    Q = int(input[idx])
    idx += 1
    
    queries = []
    for _ in range(Q):
        s = int(input[idx]) - 1
        t = int(input[idx + 1]) - 1
        queries.append((s, t))
        idx += 2
    
    INF = float('inf')
    
    for s, t in queries:
        # Required vertices: 0..K-1, s, t
        # Map them to indices 0..K+1
        required = list(range(K)) + [s, t]
        num_req = K + 2
        
        # dp[mask][v] = min cost to connect vertices in mask, rooted at v
        dp = [[INF] * N for _ in range(1 << num_req)]
        
        # Initialize: single vertices
        for i in range(num_req):
            v = required[i]
            dp[1 << i][v] = 0
        
        # Fill DP table
        for mask in range(1, 1 << num_req):
            # Combine two submasks at same vertex
            submask = mask
            while submask > 0:
                if submask != mask:
                    comp = mask ^ submask
                    for v in range(N):
                        dp[mask][v] = min(dp[mask][v], dp[submask][v] + dp[comp][v])
                submask = (submask - 1) & mask
            
            # Dijkstra to extend to other vertices
            pq = []
            for v in range(N):
                if dp[mask][v] < INF:
                    heappush(pq, (dp[mask][v], v))
            
            while pq:
                cost, u = heappop(pq)
                if cost > dp[mask][u]:
                    continue
                for v in range(N):
                    if u != v:
                        new_cost = cost + C[u][v]
                        if new_cost < dp[mask][v]:
                            dp[mask][v] = new_cost
                            heappush(pq, (new_cost, v))
        
        # Answer is minimum over all vertices for full mask
        full_mask = (1 << num_req) - 1
        ans = min(dp[full_mask])
        print(ans)

solve()