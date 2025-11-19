import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        s = list(map(int, input().split()))
        a = [None]*m
        b = [None]*m
        c = [None]*m
        for i in range(m):
            a[i] = list(map(int, input().split()))
            b[i] = list(map(int, input().split()))
            c[i] = list(map(int, input().split()))

        # For each k=1..m, we want the max possible lost luggage after k days independently.
        # The problem is to find the maximum possible lost luggage after k days,
        # given the initial s and the daily constraints a,b,c for days 1..k.

        # We model the luggage distribution as a vector x of length n (luggage at each airport).
        # Initially x = s.
        # Each day:
        # 1) Morning flights: luggage moves from each airport j to two neighbors:
        #    - first class flight: from j to prev = ((j-2) mod n)+1
        #    - second class flight: from j to next = (j mod n)+1
        #    Each flight can carry at most a[i,j] or c[i,j] luggage.
        # 2) Afternoon check: if luggage at airport j is x_j, and x_j >= b[i,j], then at least x_j - b[i,j] luggage is found and removed.
        #    So after check, luggage at j is min(x_j, b[i,j]).
        # 3) Evening: luggage arrives at destination airports.

        # We want to maximize sum of luggage after k days, under constraints:
        # - The amount sent on each flight <= capacity
        # - The amount sent from airport j <= luggage at j before flights
        # - After afternoon check, luggage at j <= b[i,j]

        # The problem is a max flow-like problem but with capacity constraints on edges and nodes,
        # and a "cut" operation (min with b[i,j]) after flights.

        # Key insight:
        # The problem can be solved by simulating the maximum possible luggage distribution day by day,
        # using a linear program or max flow approach.
        # But since n <= 12 and m <= 2000, we can simulate day by day using a max flow or linear programming approach.
        # However, we need a fast approach.

        # Another approach:
        # The problem is a max flow on a circle with capacity constraints on edges and nodes.
        # The luggage distribution after flights is:
        # Let x be luggage before flights.
        # Let f1_j be luggage sent from j to prev(j), f2_j be luggage sent from j to next(j).
        # Constraints:
        #   f1_j <= a[i,j]
        #   f2_j <= c[i,j]
        #   f1_j + f2_j <= x_j
        # After flights, luggage at airport j is:
        #   x'_j = f1_{next(j)} + f2_{prev(j)}
        # Then after check:
        #   x''_j = min(x'_j, b[i,j])

        # We want to maximize sum of x''_j.

        # We want to find x'' maximizing sum x''_j, given x and constraints.

        # This is a linear optimization problem with constraints:
        # Variables: f1_j, f2_j for j=1..n
        # Constraints:
        #   0 <= f1_j <= a[i,j]
        #   0 <= f2_j <= c[i,j]
        #   f1_j + f2_j <= x_j
        # x'_j = f1_{next(j)} + f2_{prev(j)}
        # x''_j = min(x'_j, b[i,j])

        # To maximize sum x''_j, since x''_j <= b[i,j], and x''_j <= x'_j,
        # the best is to maximize sum min(x'_j, b[i,j]).

        # Since min is concave, the maximum sum min(x'_j, b[i,j]) is achieved by maximizing x'_j but capped at b[i,j].

        # We can model this as a max flow problem on a bipartite graph:
        # Left nodes: airports j (senders)
        # Right nodes: airports j (receivers)
        # Edges:
        #   from sender j to receiver prev(j): capacity a[i,j]
        #   from sender j to receiver next(j): capacity c[i,j]
        # Sender j has supply x_j (cannot send more than x_j total)
        # Receiver j has demand b[i,j] (cannot receive more than b[i,j])

        # We want to find flows f1_j, f2_j satisfying:
        #   f1_j + f2_j <= x_j
        #   f1_j <= a[i,j]
        #   f2_j <= c[i,j]
        #   For each receiver j: sum of incoming flows <= b[i,j]

        # Maximize sum of flows (which is sum of luggage after check).

        # This is a min-cost flow or max flow with node capacities problem.

        # Since n is small, we can solve this with a simple max flow with node capacities.

        # Construct a flow network for each day:
        # Source -> sender nodes: capacity x_j
        # Sender j -> receiver prev(j): capacity a[i,j]
        # Sender j -> receiver next(j): capacity c[i,j]
        # Receiver j -> sink: capacity b[i,j]

        # Max flow in this network gives max luggage after check.

        # We do this day by day, starting from s, and update s to the flow result.

        # For each k=1..m, we run the simulation for days 1..k independently.

        # But m can be up to 2000, and t up to 100, so total m sum <= 2000.

        # To optimize, we can precompute the results for all days cumulatively.

        # But problem states for each k, the calculation is independent.

        # So we must run the simulation from s for days 1..k each time.

        # To optimize, we can precompute prefix results by simulating day by day and store the luggage after each day.

        # But problem states "these values are independent calculations", so we cannot accumulate.

        # So we must run the simulation from s for days 1..k each time.

        # Since m <= 2000 and n <= 12, and max flow is small, we can implement a fast max flow and run for each k.

        # Implement Dinic max flow for the network described.

        # We'll implement a function to build the graph and run max flow for given day i and input luggage x.

        # Then for each k, run simulation from s for days 1..k.

        # To speed up, we can cache the max flow results for each day with given input x,
        # but x changes each time, so no caching.

        # We'll implement the max flow and run simulation for each k.

        # Since n=12, graph has 2*n + 2 nodes, edges ~4*n.

        # This should be efficient enough.

        # Implementation details:
        # Nodes:
        # 0: source
        # 1..n: sender nodes (airports)
        # n+1..2n: receiver nodes (airports)
        # 2n+1: sink

        # Edges:
        # source -> sender j: capacity x_j
        # sender j -> receiver prev(j): capacity a[i,j]
        # sender j -> receiver next(j): capacity c[i,j]
        # receiver j -> sink: capacity b[i,j]

        # After max flow, the flow into sink is sum luggage after check.

        # The luggage after check at airport j is flow into receiver j node.

        # We'll extract luggage after check from flow on edges receiver j -> sink.

        # Then for next day, luggage before flights is luggage after check.

        # We'll implement max flow with adjacency list and Dinic.

        # Finally, output sum luggage after check for each k.

        def prev_idx(j):
            return (j-2) % n + 1

        def next_idx(j):
            return (j % n) + 1

        class Dinic:
            def __init__(self, N):
                self.N = N
                self.graph = [[] for _ in range(N)]

            def add_edge(self, fr, to, cap):
                self.graph[fr].append([to, cap, len(self.graph[to])])
                self.graph[to].append([fr, 0, len(self.graph[fr]) - 1])

            def bfs(self, s, t, level):
                from collections import deque
                for i in range(len(level)):
                    level[i] = -1
                level[s] = 0
                q = deque([s])
                while q:
                    v = q.popleft()
                    for i, (to, cap, rev) in enumerate(self.graph[v]):
                        if cap > 0 and level[to] < 0:
                            level[to] = level[v] + 1
                            q.append(to)
                return level[t] >= 0

            def dfs(self, v, t, f, level, iter):
                if v == t:
                    return f
                while iter[v] < len(self.graph[v]):
                    to, cap, rev = self.graph[v][iter[v]]
                    if cap > 0 and level[v] < level[to]:
                        d = self.dfs(to, t, min(f, cap), level, iter)
                        if d > 0:
                            self.graph[v][iter[v]][1] -= d
                            self.graph[to][rev][1] += d
                            return d
                    iter[v] += 1
                return 0

            def max_flow(self, s, t):
                flow = 0
                level = [-1]*self.N
                INF = 10**15
                while self.bfs(s, t, level):
                    iter = [0]*self.N
                    while True:
                        f = self.dfs(s, t, INF, level, iter)
                        if f == 0:
                            break
                        flow += f
                return flow

        def simulate_days(k):
            x = s[:]
            for day in range(k):
                dinic = Dinic(2*n+2)
                source = 0
                sink = 2*n+1
                # source -> sender j
                for j in range(n):
                    if x[j] > 0:
                        dinic.add_edge(source, j+1, x[j])
                # sender j -> receiver prev(j)
                for j in range(n):
                    if a[day][j] > 0:
                        dinic.add_edge(j+1, n+prev_idx(j+1), a[day][j])
                # sender j -> receiver next(j)
                for j in range(n):
                    if c[day][j] > 0:
                        dinic.add_edge(j+1, n+next_idx(j+1), c[day][j])
                # receiver j -> sink
                for j in range(n):
                    if b[day][j] > 0:
                        dinic.add_edge(n+j+1, sink, b[day][j])
                # max flow
                dinic.max_flow(source, sink)
                # luggage after check = flow into sink from receiver nodes
                # luggage at airport j after check = sum of flow on edge receiver j -> sink
                new_x = [0]*n
                for j in range(n):
                    # find edge receiver j -> sink
                    for to, cap, rev in dinic.graph[n+j+1]:
                        if to == sink:
                            # reverse edge capacity is flow
                            # flow = capacity of reverse edge in residual graph
                            # original capacity - residual capacity = flow
                            # but we have only residual capacity here
                            # so flow = original capacity - residual capacity
                            # original capacity = cap + flow on reverse edge
                            # but we don't store original capacity directly
                            # so we can get flow by sum of reverse edge capacity
                            # Actually, dinic.graph[sink][rev] is reverse edge
                            # dinic.graph[sink][rev][1] is residual capacity of reverse edge
                            # original capacity of edge receiver->sink = cap + dinic.graph[sink][rev][1]
                            # flow = original capacity - residual capacity = cap - residual capacity
                            rev_edge = dinic.graph[sink][rev]
                            flow = rev_edge[1]
                            # flow on edge receiver->sink = original capacity - residual capacity
                            # original capacity = cap + flow on reverse edge
                            # residual capacity on edge = cap
                            # residual capacity on reverse edge = flow
                            # So flow = original capacity - residual capacity = (cap + flow) - cap = flow
                            # So flow = flow on reverse edge
                            new_x[j] = flow
                            break
                x = new_x
            return sum(x)

        # For each k=1..m, output simulate_days(k)
        # To speed up, we can precompute results for all k by running simulate_days(k) for k=1..m
        # But this is O(m^2), too slow.

        # Instead, we can do binary search on days? No, problem requires all k.

        # Since m <= 2000 and n=12, and max flow is small, we can do direct simulation for each k.

        # To speed up, we can memoize day results:
        # But problem states independent calculation for each k, so no reuse.

        # We'll just run simulate_days(k) for k=1..m.

        # To speed up, we can precompute prefix max flows for days 1..m and store luggage after each day,
        # but problem states independent calculation, so no.

        # We'll implement simulate_days(k) for each k.

        # To speed up, we can implement a cache for day max flows with given x,
        # but x changes each time.

        # We'll just run simulate_days(k) for each k.

        # Since m <= 2000, n=12, and max flow is small, this should pass.

        # Output results
        for k in range(1, m+1):
            print(simulate_days(k))

solve()