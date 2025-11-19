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

    def steiner_tree(terminals):

        num_terminals = len(terminals)
        max_mask = 1 << num_terminals

        INF = float('inf')
        dp = [[INF] * n for _ in range(max_mask)]

        for i, terminal in enumerate(terminals):
            dp[1 << i][terminal] = 0

        for mask in range(1, max_mask):

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

            for v in range(n):
                dp[mask][v] = current_dist[v]

        full_mask = max_mask - 1
        result = min(dp[full_mask])

        return result

    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())

        s -= 1
        t -= 1

        terminals = list(range(k)) + [s, t]

        seen = set()
        unique_terminals = []
        for terminal in terminals:
            if terminal not in seen:
                unique_terminals.append(terminal)
                seen.add(terminal)

        result = steiner_tree(unique_terminals)
        print(result)

solve()