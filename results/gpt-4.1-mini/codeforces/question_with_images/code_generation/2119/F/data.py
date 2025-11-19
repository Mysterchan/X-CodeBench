import sys
import threading
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    T = int(input())
    
    # We will process all test cases efficiently.
    # Key observations and approach:
    # - The lava floods vertices with distance <= t at time t.
    # - At time t, you are at some vertex u.
    #   1) Increase life S by w_u.
    #   2) If S=0 or u is flooded (dist[u] <= t), you die immediately.
    #   3) Must move to an adjacent vertex (arrive at next time t+1).
    #
    # We want to maximize the number of moves before dying.
    #
    # Constraints:
    # - n up to 5*10^5 per test, sum n up to 10^6.
    # - w_i in {1, -1}, w_st=1.
    #
    # Approach:
    # 1) Compute dist[] from root (1) by BFS.
    # 2) The lava flooding time for vertex u is dist[u].
    # 3) We start at st at time 0 with S=1.
    # 4) At each time t, at vertex u:
    #    - S += w_u
    #    - If S=0 or dist[u] <= t: die
    #    - Move to adjacent vertex v, arrive at t+1.
    #
    # We want to find the longest path (sequence of moves) satisfying:
    # For each step i (time i):
    #   S_i = S_{i-1} + w_{u_i} > 0
    #   dist[u_i] > i
    #
    # We must move every step, no staying.
    #
    # This is a DP on tree problem with time constraints.
    #
    # Key insight:
    # - The lava flooding time is dist[u].
    # - We cannot be at u at time t >= dist[u].
    # - So max time at u is dist[u]-1.
    #
    # We want to find a path starting at st at time 0, moving each step,
    # with S always > 0, and t < dist[u].
    #
    # We can model this as a DFS with memoization:
    # For each node u, define dp[u] = max moves starting at u at time t=0 with S=1.
    #
    # But S changes along the path, so we must track S.
    #
    # However, w_i in {1,-1}, and S must remain > 0.
    #
    # We can do a DFS from st, trying all neighbors, tracking S and time.
    #
    # But naive DFS is too slow.
    #
    # Optimization:
    # - Since w_i in {1,-1}, and S must remain > 0,
    #   the minimal S along the path is important.
    # - We can do a BFS or DFS with pruning.
    #
    # Another approach:
    # - Since we must move every step, and lava floods vertices at dist[u],
    #   the maximum time we can stay at u is dist[u]-1.
    # - So the maximum length of path is limited by dist[u].
    #
    # We can do a BFS from st with states (node, S, time).
    # But S can be large, so we must prune.
    #
    # Since w_i in {1,-1}, and S must remain > 0,
    # the minimal S is 1, max S can be up to number of +1 vertices visited.
    #
    # We can do a BFS with pruning:
    # - For each node and time, keep track of max S reached.
    # - If we reach (u,t) with S <= 0 or t >= dist[u], discard.
    # - If we reach (u,t) with S <= previously recorded S, discard.
    #
    # But time can be large, so we must prune carefully.
    #
    # Since we want max moves, we can do a BFS layer by layer:
    # At each time t, we have a set of states (u, S).
    #
    # Implementation:
    # - Precompute dist[] from root.
    # - Use a queue for BFS: states = (u, S)
    # - At time t, process all states.
    # - For each state:
    #   - S += w[u]
    #   - If S <= 0 or dist[u] <= t: die, do not enqueue next states.
    #   - Else, for each neighbor v:
    #       enqueue (v, S) for time t+1 if better than before.
    #
    # To avoid TLE, we keep for each (u) the max S at time t.
    # But time can be large, so we keep only max S per node.
    #
    # If we reach (u) with S <= maxS[u], discard.
    # Else update maxS[u] = S and enqueue.
    #
    # The BFS ends when no new states.
    #
    # The answer is max time t reached.
    #
    # This approach is feasible because:
    # - Each node can be visited multiple times with different S.
    # - But we only keep states with strictly better S.
    #
    # Let's implement this.

    from collections import deque

    for _ in range(T):
        n, st = map(int, input().split())
        w = list(map(int, input().split()))
        adj = [[] for __ in range(n)]
        for __ in range(n-1):
            u,v = map(int, input().split())
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)

        # Compute dist from root (1)
        dist = [-1]*n
        dist[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)

        st -= 1

        # BFS states: (node, S)
        # At time t, we process states.
        # We keep maxS[u] = max life value reached at u so far.
        maxS = [-1]*(n)
        # Initial state:
        # At time 0, at st, S=1
        # But first step: at time 0, life += w[st], so S=1 + w[st] = 2 (since w[st]=1)
        # Check if S=0 or dist[st] <= 0 (dist[st] is distance from root)
        # If dist[st] <= 0 means flooded at time 0, die immediately.
        # dist[st] is distance from root, must be > 0 to survive at time 0.
        # But dist[st] can be 0 only if st=0 (root).
        # Problem states st >= 2, so dist[st]>=1 always.
        # So no immediate death from lava at time 0.
        # So initial S = 1 + w[st] = 2

        initial_S = 1 + w[st]
        if initial_S <= 0 or dist[st] <= 0:
            # Die immediately, no moves possible
            print(0)
            continue

        maxS[st] = initial_S
        queue = deque()
        queue.append((st, initial_S))
        time = 0
        ans = 0

        while queue:
            time += 1
            size = len(queue)
            next_queue = deque()
            for _ in range(size):
                u, S = queue.popleft()
                # Must move to adjacent vertex v
                for v in adj[u]:
                    S2 = S + w[v]
                    # Check death conditions at time t:
                    # S2 > 0 and dist[v] > time
                    if S2 <= 0 or dist[v] <= time:
                        continue
                    if S2 > maxS[v]:
                        maxS[v] = S2
                        next_queue.append((v, S2))
            if not next_queue:
                break
            queue = next_queue
            ans = time

        print(ans)

threading.Thread(target=main).start()