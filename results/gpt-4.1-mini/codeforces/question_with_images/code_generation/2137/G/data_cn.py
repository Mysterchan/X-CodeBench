import sys
import threading
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, m, q = map(int, input().split())
        g = [[] for __ in range(n+1)]
        rg = [[] for __ in range(n+1)]
        outdeg = [0]*(n+1)
        for __ in range(m):
            u,v = map(int, input().split())
            g[u].append(v)
            rg[v].append(u)
            outdeg[u] += 1

        # States:
        # 0: unknown
        # 1: Cry wins
        # 2: River wins
        state = [0]*(n+1)
        red = [False]*(n+1)

        # Initialize:
        # If node has no out edges => Cry wins immediately if token arrives after player's move
        # If node is red => River wins immediately
        # If node is both red and no out edges => River wins immediately

        # We will maintain:
        # For each node, count of children not yet known to be River wins (for Cry's turn)
        # and count of children not yet known to be Cry wins (for River's turn)
        # But since the game alternates moves, and Cry moves first, we can model states as:
        # state[u] = 1 if Cry can force a win starting from u
        # state[u] = 2 if River can force a win starting from u

        # The game ends immediately if after a move token is on a red node or a node with no out edges (Cry wins if no out edges, River wins if red)
        # So terminal nodes:
        # red nodes => River wins
        # no out edges and not red => Cry wins

        # We will do a backward propagation from terminal nodes to determine states.

        # For each node, we keep track of how many children are not yet losing for the current player.
        # Because the graph is DAG, we can process in topological order or use a queue.

        # We use a queue to propagate states backward.

        # For each node, we keep:
        # cnt_cry: number of children not yet known to be River wins (for Cry's turn)
        # cnt_river: number of children not yet known to be Cry wins (for River's turn)
        cnt_cry = [0]*(n+1)
        cnt_river = [0]*(n+1)
        for u in range(1,n+1):
            cnt_cry[u] = len(g[u])
            cnt_river[u] = len(g[u])

        from collections import deque
        qd = deque()

        # Initialize terminal states
        for u in range(1,n+1):
            if red[u]:
                state[u] = 2
                qd.append(u)
            elif outdeg[u] == 0:
                state[u] = 1
                qd.append(u)

        # But initially all nodes are blue, so only no out edges nodes are Cry wins
        # So we initialize again:
        for u in range(1,n+1):
            if outdeg[u] == 0:
                state[u] = 1
                qd.append(u)

        # We will implement a function to update states after red[u] changes

        def update_states():
            # Recompute states from scratch
            # Because red nodes can only increase, we can do incremental update
            # But to keep code simple and efficient, we do incremental update only for changed nodes

            # Actually, we will do incremental update after each red update:
            # For each newly red node u:
            # if state[u] != 2:
            #   state[u] = 2
            #   qd.append(u)
            # Then propagate backward

            while qd:
                u = qd.popleft()
                st = state[u]
                for p in rg[u]:
                    if state[p] != 0:
                        continue
                    # p's turn: Cry moves first, then River, so turns alternate
                    # We don't track turn explicitly, but the state meaning is:
                    # If from p, there is a child with state == 1 (Cry wins), then p can move there and win if it's Cry's turn
                    # If all children lead to River wins, then p loses (River wins)
                    # But since Cry moves first, the parity of moves matters:
                    # Actually, the problem states Cry moves first, then River, alternating.
                    # The state is from the perspective of the player to move at node u.
                    # So we need to know whose turn it is at node u.

                    # But the problem states the token is placed at node s, Cry moves first.
                    # So the turn parity is determined by the distance from s.
                    # But queries ask for arbitrary s, so we must consider both turns.

                    # To handle this, we can model two states per node:
                    # state[u][0]: if it's Cry's turn at u, can Cry force a win?
                    # state[u][1]: if it's River's turn at u, can Cry force a win?

                    # But the problem only asks if Cry wins starting from u with Cry to move.

                    # So we need to model two states per node.

                    # Let's redo the approach with two states per node.

                    pass

        # Because above approach is complicated, let's implement the standard two-state DP for DAG games:

        # For each node u:
        # dp[u][0]: True if player to move (Cry) can force a win starting at u
        # dp[u][1]: True if player to move (River) can force a win starting at u

        # Terminal conditions:
        # If node u is red => River wins immediately => dp[u][0] = dp[u][1] = False (Cry loses)
        # If node u has no out edges and not red => Cry wins immediately => dp[u][0] = dp[u][1] = True (Cry wins)
        # Because if no out edges, after move token is there, Cry wins immediately.

        # For other nodes:
        # dp[u][0] = any dp[v][1] for v in g[u] (Cry tries to move to a node where River loses)
        # dp[u][1] = all dp[v][0] for v in g[u] (River tries to move to nodes where Cry loses)

        # We can do a topological order and compute dp.

        # Since red nodes can be updated, we need to support dynamic updates.

        # But red nodes only increase, so we can do incremental updates.

        # Let's implement two arrays:
        # dp0[u]: dp[u][0]
        # dp1[u]: dp[u][1]

        # We also keep counts:
        # For dp0[u], Cry's turn, dp0[u] = any dp1[v] == True
        # For dp1[u], River's turn, dp1[u] = all dp0[v] == True

        # So for dp0[u], we keep count of children v with dp1[v] == True
        # For dp1[u], we keep count of children v with dp0[v] == True

        # We can maintain:
        # cnt_dp1_true[u]: number of children v with dp1[v] == True
        # cnt_dp0_true[u]: number of children v with dp0[v] == True

        # For dp0[u]:
        # dp0[u] = (cnt_dp1_true[u] > 0)
        # For dp1[u]:
        # dp1[u] = (cnt_dp0_true[u] == outdeg[u])

        # When dp0 or dp1 of a node changes, we update parents accordingly.

        # Initialize dp0 and dp1:

        dp0 = [False]*(n+1)
        dp1 = [False]*(n+1)
        cnt_dp1_true = [0]*(n+1)
        cnt_dp0_true = [0]*(n+1)

        # Initialize red array and outdeg already known

        # Initialize dp for terminal nodes:
        # If red[u]: dp0[u] = dp1[u] = False
        # elif outdeg[u] == 0: dp0[u] = dp1[u] = True
        # else dp0[u] = dp1[u] = False initially

        # We will do a queue to propagate dp changes

        # First, all nodes dp0 and dp1 = False
        # Then set terminal nodes accordingly

        # We need to process queries online:
        # For query type 1 u: set red[u] = True, update dp0[u], dp1[u] to False if not already, propagate changes
        # For query type 2 u: output YES if dp0[u] == True else NO

        # Build parents list (reverse graph) rg already built

        # Initialize dp arrays and counts

        # First set dp0 and dp1 for terminal nodes

        # For nodes with outdeg == 0 and not red: dp0[u] = dp1[u] = True
        # For red nodes: dp0[u] = dp1[u] = False

        # Then for other nodes, dp0[u] and dp1[u] = False initially

        # Then compute cnt_dp1_true and cnt_dp0_true for each node

        # Then propagate dp changes until stable

        # Implement function to update dp for a node and propagate changes

        # Let's implement:

        for u in range(1,n+1):
            if red[u]:
                dp0[u] = False
                dp1[u] = False
            elif outdeg[u] == 0:
                dp0[u] = True
                dp1[u] = True
            else:
                dp0[u] = False
                dp1[u] = False

        # Initialize counts
        for u in range(1,n+1):
            cnt_dp1_true[u] = 0
            cnt_dp0_true[u] = 0
        for u in range(1,n+1):
            for v in g[u]:
                if dp1[v]:
                    cnt_dp1_true[u] += 1
                if dp0[v]:
                    cnt_dp0_true[u] += 1

        # Function to update dp0[u] and dp1[u] and propagate changes
        from collections import deque
        def propagate(nodes):
            qd = deque(nodes)
            while qd:
                u = qd.popleft()
                old_dp0 = dp0[u]
                old_dp1 = dp1[u]

                # Update dp0[u]
                dp0[u] = (cnt_dp1_true[u] > 0) if not red[u] else False
                # Update dp1[u]
                dp1[u] = (cnt_dp0_true[u] == outdeg[u]) if (not red[u] and outdeg[u] > 0) else (False if red[u] else (True if outdeg[u]==0 else False))

                if dp0[u] != old_dp0 or dp1[u] != old_dp1:
                    for p in rg[u]:
                        # Update counts for p
                        if dp1[u] != old_dp1:
                            if dp1[u]:
                                cnt_dp1_true[p] += 1
                            else:
                                cnt_dp1_true[p] -= 1
                        if dp0[u] != old_dp0:
                            if dp0[u]:
                                cnt_dp0_true[p] += 1
                            else:
                                cnt_dp0_true[p] -= 1
                        qd.append(p)

        # Initially propagate all nodes to stabilize dp
        propagate(range(1,n+1))

        # Now process queries
        for __ in range(q):
            x,u = map(int, input().split())
            if x == 1:
                # paint u red
                if not red[u]:
                    red[u] = True
                    # dp0[u] and dp1[u] become False if not already
                    old_dp0 = dp0[u]
                    old_dp1 = dp1[u]
                    dp0[u] = False
                    dp1[u] = False
                    if old_dp0 != dp0[u] or old_dp1 != dp1[u]:
                        # update parents counts
                        for p in rg[u]:
                            if old_dp1 != dp1[u]:
                                if dp1[u]:
                                    cnt_dp1_true[p] += 1
                                else:
                                    cnt_dp1_true[p] -= 1
                            if old_dp0 != dp0[u]:
                                if dp0[u]:
                                    cnt_dp0_true[p] += 1
                                else:
                                    cnt_dp0_true[p] -= 1
                        propagate(rg[u])
            else:
                # query type 2: output YES if dp0[u] == True else NO
                print("YES" if dp0[u] else "NO")

threading.Thread(target=main).start()