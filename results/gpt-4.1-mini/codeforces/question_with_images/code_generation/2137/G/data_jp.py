import sys
import threading
from collections import deque

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, m, q = map(int, input().split())
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        outdeg = [0]*n
        for __ in range(m):
            u,v = map(int, input().split())
            u -= 1
            v -= 1
            g[u].append(v)
            rg[v].append(u)
            outdeg[u] += 1

        # States:
        # 0: unknown
        # 1: Cry wins
        # 2: River wins
        # We keep track of states for both players' turns:
        # turn 0: Cry's turn
        # turn 1: River's turn
        # dp[node][turn] = state
        # state: 1= Cry wins, 2= River wins

        # Initialize dp with 0 (unknown)
        dp = [[0]*2 for _ in range(n)]

        # Count of moves from node for each turn (for DP)
        # For each node and turn, how many moves remain to be processed
        cnt = [[len(g[node]) for node in range(n)] for _ in range(2)]

        # Initially, all nodes are blue
        # We will maintain a queue for BFS of states
        # Terminal conditions:
        # - If node has no outgoing edges => Cry wins immediately after any turn
        # - If node is red => River wins immediately after any turn

        # Initially all nodes are blue, so no red nodes
        # So only terminal states are nodes with outdeg=0 => Cry wins for both turns

        # We will maintain a queue of (node, turn) with known states
        qd = deque()
        for v in range(n):
            if outdeg[v] == 0:
                # No outgoing edges => Cry wins immediately after any turn
                dp[v][0] = 1
                dp[v][1] = 1
                qd.append((v,0))
                qd.append((v,1))

        # We also need to track red nodes, initially none
        red = [False]*n

        # BFS to propagate states backward
        def update():
            while qd:
                v, turn = qd.popleft()
                state = dp[v][turn]
                prev_turn = 1 - turn
                for u in rg[v]:
                    if dp[u][prev_turn] != 0:
                        continue
                    if state == 2:
                        # If current node is River win, then from prev node with prev_turn:
                        # If prev_turn player can move to a node where opponent loses, prev_turn player wins
                        # But here state==2 means River wins at v after turn
                        # So if prev_turn player is Cry (turn=0), and next node is River win, then Cry loses
                        # So if next node is River win, prev_turn player cannot win by moving here
                        # So we decrease cnt and if cnt==0, prev_turn player loses (River wins)
                        cnt[prev_turn][u] -= 1
                        if cnt[prev_turn][u] == 0:
                            dp[u][prev_turn] = 2
                            qd.append((u, prev_turn))
                    else:
                        # state == 1 (Cry wins)
                        # If next node is Cry win, then prev_turn player can move here and win
                        # So prev_turn player wins
                        dp[u][prev_turn] = 1
                        qd.append((u, prev_turn))

        update()

        # Now process queries
        # For query type 1 u: paint node u red
        # When node u becomes red:
        # dp[u][0] = 2 (River wins)
        # dp[u][1] = 2 (River wins)
        # We need to propagate this update backward similarly

        for __ in range(q):
            x,u = map(int, input().split())
            u -= 1
            if x == 1:
                # paint u red
                if red[u]:
                    # Already red, no change
                    continue
                red[u] = True
                # If dp[u][0] or dp[u][1] already 2, no need to update
                updated = False
                for turn in (0,1):
                    if dp[u][turn] != 2:
                        dp[u][turn] = 2
                        qd.append((u, turn))
                        updated = True
                if updated:
                    # Reset cnt for nodes that are not yet decided
                    # Actually cnt is only used for nodes with dp=0
                    # We do not reset cnt here, just propagate
                    update()
            else:
                # query type 2: does Cry win starting from node u (Cry's turn)
                # Cry moves first, so turn=0
                # If dp[u][0] == 1 => YES else NO
                print("YES" if dp[u][0] == 1 else "NO")

threading.Thread(target=main).start()