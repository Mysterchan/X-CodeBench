import sys
import threading
from collections import deque

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
        # 0 = unknown
        # 1 = Cry wins
        # 2 = River wins
        state = [0]*(n+1)
        red = [False]*(n+1)

        # Initialize queue for BFS
        q_bfs = deque()

        # Initial states:
        # If node has no outgoing edges => Cry wins immediately
        # If node is red => River wins immediately (initially none red)
        for i in range(1,n+1):
            if outdeg[i] == 0:
                state[i] = 1
                q_bfs.append(i)

        # We will maintain:
        # For each node, count how many children are not River wins (state != 2)
        # This helps to determine if a node is forced to River win
        # Because:
        # - Cry wins if there is at least one child with Cry win (state=1)
        # - River wins if all children are River wins (state=2)
        # So we track how many children are NOT River wins to know when all children are River wins.

        not_river_child_count = [0]*(n+1)
        for u in range(1,n+1):
            cnt = 0
            for v in g[u]:
                if state[v] != 2:
                    cnt += 1
            not_river_child_count[u] = cnt

        # Propagate initial states
        # BFS from terminal nodes (Cry wins)
        while q_bfs:
            u = q_bfs.popleft()
            for p in rg[u]:
                if state[p] != 0:
                    continue
                if state[u] == 1:
                    # If any child is Cry win, parent is Cry win
                    state[p] = 1
                    q_bfs.append(p)
                else:
                    # state[u] == 2
                    # Decrease count of not River children
                    not_river_child_count[p] -= 1
                    if not_river_child_count[p] == 0:
                        # All children are River wins => parent is River win
                        state[p] = 2
                        q_bfs.append(p)

        # Now process queries
        # When a node u is painted red:
        # - If state[u] != 2, set state[u] = 2 (River wins)
        # - Propagate this change backward similarly to BFS
        # Because red node means River wins immediately at that node,
        # and this can force parents to become River wins if all children are River wins.

        for __ in range(q):
            x,u = map(int, input().split())
            if x == 1:
                # Paint u red
                if not red[u]:
                    red[u] = True
                    if state[u] != 2:
                        state[u] = 2
                        q_bfs = deque([u])
                        # Update parents
                        while q_bfs:
                            cur = q_bfs.popleft()
                            for p in rg[cur]:
                                if state[p] == 2:
                                    continue
                                # cur changed to River win, so decrease parent's not_river_child_count
                                not_river_child_count[p] -= 1
                                if not_river_child_count[p] == 0:
                                    state[p] = 2
                                    q_bfs.append(p)
            else:
                # Query if Cry wins starting at u
                # Conditions:
                # - If node is red => River wins => NO
                # - If node has no outgoing edges => Cry wins => YES
                # - Otherwise, check state[u]
                # state[u] == 1 => Cry wins
                # state[u] == 2 => River wins
                # state[u] == 0 should not happen after initialization and propagation
                if red[u]:
                    print("NO")
                else:
                    if outdeg[u] == 0:
                        print("YES")
                    else:
                        print("YES" if state[u] == 1 else "NO")

threading.Thread(target=main).start()