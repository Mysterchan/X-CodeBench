import sys
import threading
from collections import deque

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, m, q = map(int, input().split())
        g = [[] for __ in range(n)]
        rg = [[] for __ in range(n)]
        outdeg = [0]*n
        for __ in range(m):
            u,v = map(int, input().split())
            u -= 1
            v -= 1
            g[u].append(v)
            rg[v].append(u)
            outdeg[u] += 1

        # States:
        # 0 - unknown
        # 1 - River wins (losing for Cry)
        # 2 - Cry wins
        state = [0]*n
        # color: False=blue, True=red
        red = [False]*n

        # Initialize:
        # River wins if node is red or node is terminal and red (terminal red => River wins)
        # Terminal blue nodes => Cry wins (since Cry wins if reach terminal blue)
        # Terminal nodes: outdeg==0
        # According to problem:
        # - If node is red => River wins immediately
        # - If node is terminal and blue => Cry wins
        # - If node is terminal and red => River wins

        # We will do a retrograde analysis (backward BFS) to find states:
        # For each node:
        # - If red => River wins (state=1)
        # - Else if terminal => Cry wins (state=2)
        # - Else unknown (0)

        # We also need to track for each node:
        # - How many children are not losing for Cry (for Cry's turn)
        # - How many children are not losing for River (for River's turn)
        # But since the game alternates moves, and Cry moves first,
        # we can model states as:
        # state=1 means River wins from this node (losing for Cry)
        # state=2 means Cry wins from this node

        # The game ends when:
        # - The token reaches a red node (River wins)
        # - The token reaches a terminal node (Cry wins if blue, River wins if red)
        # - If node is both red and terminal => River wins

        # We will use a queue to propagate states backward.

        # For each node, we keep track of how many children are not losing for Cry
        # For Cry's turn, if any child is losing for River (state=1), Cry can move there and win.
        # For River's turn, if all children are winning for Cry (state=2), River loses, else River can move to a node winning for River.

        # But since the problem states the game ends immediately if token reaches red or terminal node,
        # and the graph is DAG, we can do a standard retrograde analysis.

        # We will store:
        # deg[u] = number of children of u
        # cnt_cry_win[u] = number of children where Cry wins (state=2)
        # cnt_river_win[u] = number of children where River wins (state=1)

        # But simpler approach:
        # We can do a queue of nodes with known states:
        # Initially:
        # - All red nodes: state=1 (River wins)
        # - All terminal blue nodes: state=2 (Cry wins)
        # - All terminal red nodes: state=1 (River wins)

        # Then propagate backward:
        # For each node u:
        # - If it's Cry's turn (first move from u), Cry wants to move to a node where Cry wins (state=2)
        #   So if any child v has state=2, then u state=2 (Cry wins)
        #   Else u state=1 (River wins)
        # But since the game alternates moves, and Cry moves first, we need to consider parity of moves.

        # The problem states:
        # - Cry moves first
        # - Players alternate moves
        # So the state depends on whose turn it is.

        # To handle this, we can model states for each node and turn parity:
        # state[u][parity]: who wins if token is at u and it's parity's turn (0 for Cry, 1 for River)
        # But q can be large, so we need efficient updates.

        # However, the problem only asks: "If game starts at u, who wins?"
        # Since Cry moves first, the initial turn parity is 0 (Cry's turn).

        # So we need to compute state[u][0] (Cry's turn at u).

        # Let's implement a standard two-player game DP on DAG with parity:

        # For each node u:
        # state[u][0] = True if player to move (Cry) can force a win from u
        # state[u][1] = True if player to move (River) can force a win from u

        # Terminal conditions:
        # If u is red => River wins immediately => state[u][0] = False (Cry loses), state[u][1] = True (River wins)
        # If u is terminal and blue => Cry wins immediately => state[u][0] = True, state[u][1] = False
        # If u is terminal and red => River wins immediately => state[u][0] = False, state[u][1] = True

        # For other nodes:
        # state[u][p] = any(state[v][1-p] == True for v in g[u])  # player p can move to a node where opponent loses

        # If no moves:
        # state[u][p] = False (player p loses)

        # We can precompute state[u][0] and state[u][1] by topological order.

        # Updates:
        # When a node becomes red, we need to update states accordingly.

        # Since q can be large, we need an efficient way to update states after coloring a node red.

        # Approach:
        # We will maintain state[u][0], state[u][1]
        # Initially compute states for all nodes.

        # When a node u becomes red:
        # - state[u][0] = False
        # - state[u][1] = True
        # If previously state[u][0] or state[u][1] changed, we propagate changes backward.

        # We will keep track of in-edges to propagate changes.

        # Implementation details:

        # For each node u:
        # - outdeg[u] = number of children
        # - For each parity p in {0,1}:
        #   - count of children v where state[v][1-p] == False (losing for opponent)
        #   - If count > 0 => state[u][p] = True
        #   - Else state[u][p] = False

        # We keep cnt_losing[u][p] = number of children v where state[v][1-p] == False

        # When state[v][1-p] changes, we update cnt_losing for parents of v.

        # Let's implement this.

        # Data structures:
        # state[u][p]: bool
        # cnt_losing[u][p]: int
        # parents[u]: list of nodes with edges to u

        parents = rg
        children = g

        state = [[False, False] for __ in range(n)]
        cnt_losing = [[0,0] for __ in range(n)]

        # Initialize terminal nodes and red nodes
        # For each node u:
        # If red[u]:
        #   state[u][0] = False (Cry loses)
        #   state[u][1] = True (River wins)
        # Else if terminal:
        #   if blue:
        #       state[u][0] = True (Cry wins)
        #       state[u][1] = False
        #   else red terminal handled above

        # Initially all blue, so no red nodes
        # So terminal nodes are Cry wins at Cry's turn, lose at River's turn

        # Initialize red array and states accordingly
        # We'll do initial computation after reading input

        # For initial:
        # red = [False]*n

        # Initialize cnt_losing:
        # For each node u and parity p:
        # cnt_losing[u][p] = number of children v where state[v][1-p] == False

        # We'll do a topological order to compute states

        # First, mark red nodes (none initially)
        # Mark terminal nodes

        # We'll implement a function to recompute states from scratch

        # But since q can be large, we need incremental updates

        # So we do initial computation, then for each update (color red), we update states incrementally.

        # Let's implement initial computation:

        # Step 1: Initialize state for terminal nodes and red nodes

        # Step 2: For other nodes, compute cnt_losing and state

        # Step 3: Use queue to propagate changes until stable

        # Then for queries:
        # - For query type 1 u: color u red, update states if changed
        # - For query type 2 u: print YES if state[u][0] == True else NO

        # Implementation:

        # Initialize red array
        # Initially all False

        # Initialize state:
        # For u in [0..n-1]:
        #   if red[u]:
        #       state[u][0] = False
        #       state[u][1] = True
        #   else if outdeg[u] == 0:
        #       state[u][0] = True
        #       state[u][1] = False
        #   else:
        #       state[u][0] = False
        #       state[u][1] = False

        # Then compute cnt_losing[u][p]

        # Then propagate states until stable

        # For updates:
        # When coloring u red:
        #   if red[u] == False:
        #       red[u] = True
        #       old_state0, old_state1 = state[u]
        #       state[u][0] = False
        #       state[u][1] = True
        #       if state changed:
        #           propagate changes backward

        # Propagation:
        # For each parent p of u:
        #   For parity in {0,1}:
        #       if state[u][1-parity] changed from old to new:
        #           update cnt_losing[p][parity]
        #           recompute state[p][parity]
        #           if state[p][parity] changed:
        #               add p to queue

        # We'll implement this carefully.

        # Let's proceed.

        # --- Implementation ---

        # Initialize red
        red = [False]*n

        # Initialize state
        for u in range(n):
            if red[u]:
                state[u][0] = False
                state[u][1] = True
            elif outdeg[u] == 0:
                # terminal blue
                state[u][0] = True
                state[u][1] = False
            else:
                state[u][0] = False
                state[u][1] = False

        # Initialize cnt_losing
        for u in range(n):
            for p in (0,1):
                cnt = 0
                for v in children[u]:
                    if not state[v][1-p]:
                        cnt += 1
                cnt_losing[u][p] = cnt

        # Initialize queue for propagation
        qstate = deque()

        # Initially, nodes where state[u][p] can be updated?
        # Actually, initial states are set, but some nodes may have state[u][p] = False while cnt_losing[u][p] > 0
        # So we recompute states based on cnt_losing

        # Recompute states until stable
        for u in range(n):
            for p in (0,1):
                new_state = cnt_losing[u][p] > 0
                if new_state != state[u][p]:
                    state[u][p] = new_state
                    qstate.append((u,p))

        while qstate:
            u,p = qstate.popleft()
            # propagate to parents
            for par in parents[u]:
                old_cnt = cnt_losing[par][p]
                # state[u][1-p] changed?
                # We need to check if state[u][1-p] changed, but we don't have old state here
                # So we must track changes carefully

                # Actually, we only propagate when state[u][1-p] changes
                # But here we only know state[u][p] changed

                # So we need to propagate changes for state[u][1-p]

                # So we need to propagate changes for state[u][1-p], but we have state[u][p] changed

                # So we need to propagate changes for state[u][1-p] when state[u][1-p] changes

                # So we need to track changes for both parities separately

                # To solve this, we will propagate changes for both parities separately

                # So we need to propagate changes for state[u][1-p] to parents for parity p

                # So here, state[u][p] changed, so parents need to update cnt_losing for parity 1-p

                # So for parent par and parity 1-p:
                # cnt_losing[par][1-p] depends on state[u][p]

                # So update cnt_losing[par][1-p]

                p2 = 1 - p
                old_cnt = cnt_losing[par][p2]
                if state[u][p]:
                    # state[u][p] changed to True
                    # state[u][p] == True means state[u][p] == True
                    # cnt_losing counts children v where state[v][1-p2] == False
                    # Here p2 = 1-p, so 1-p2 = p
                    # So cnt_losing[par][p2] counts children v where state[v][p] == False
                    # state[u][p] changed from old to new
                    # If state[u][p] changed from False to True, cnt_losing decreases by 1
                    # If changed from True to False, cnt_losing increases by 1

                    # We don't know old state here, so we must store old state before changing

                    # To handle this, we will store old state before changing state[u][p]

                    # But here we are propagating after state[u][p] changed

                    # So we need to know old state[u][p] before change

                    # To solve this, we will store old state before changing state[u][p] in the queue processing

                    # So we need to change approach: when state[u][p] changes, we push (u,p,old_state) to queue

                    # Let's restart propagation with old_state stored

                    pass

        # To implement propagation correctly, we need to store old state when pushing to queue

        # Let's rewrite propagation with old_state stored

        # --- Restart implementation ---

        # We'll implement a function to set state[u][p] to new value and propagate if changed

        # We'll keep a queue of nodes to process

        # Let's implement a helper function:

        def set_state(u, p, val):
            if state[u][p] == val:
                return
            old_val = state[u][p]
            state[u][p] = val
            qstate.append((u,p,old_val))

        # Initialize queue with initial states changes

        qstate = deque()

        # Initialize cnt_losing again
        cnt_losing = [[0,0] for __ in range(n)]
        for u in range(n):
            for p in (0,1):
                cnt = 0
                for v in children[u]:
                    if not state[v][1-p]:
                        cnt += 1
                cnt_losing[u][p] = cnt

        # Initialize states based on cnt_losing
        for u in range(n):
            for p in (0,1):
                val = cnt_losing[u][p] > 0
                if state[u][p] != val:
                    set_state(u,p,val)

        # Process queue
        while qstate:
            u,p,old_val = qstate.popleft()
            # propagate to parents
            for par in parents[u]:
                p2 = 1 - p
                # state[u][p] changed from old_val to state[u][p]
                # cnt_losing[par][p2] counts children v where state[v][1-p2] == False
                # 1-p2 = p
                # So cnt_losing[par][p2] depends on state[u][p]

                if old_val == False and state[u][p] == True:
                    # child changed from losing to winning for player p
                    # so cnt_losing[par][p2] decreases by 1
                    cnt_losing[par][p2] -= 1
                elif old_val == True and state[u][p] == False:
                    # child changed from winning to losing for player p
                    # so cnt_losing[par][p2] increases by 1
                    cnt_losing[par][p2] += 1
                else:
                    continue

                val = cnt_losing[par][p2] > 0
                if state[par][p2] != val:
                    set_state(par,p2,val)

        # Now we have initial states computed

        # Process queries

        # For query type 1 u: color u red
        # If red[u] == False:
        #   red[u] = True
        #   old0, old1 = state[u][0], state[u][1]
        #   state[u][0] = False
        #   state[u][1] = True
        #   if state changed, propagate changes

        # We'll implement a function to update node u to red and propagate changes

        def color_red(u):
            if red[u]:
                return
            red[u] = True
            old0, old1 = state[u][0], state[u][1]
            set_state(u,0,False)
            set_state(u,1,True)
            # Process queue until stable
            while qstate:
                uu,pp,old_val = qstate.popleft()
                for par in parents[uu]:
                    p2 = 1 - pp
                    if old_val == False and state[uu][pp] == True:
                        cnt_losing[par][p2] -= 1
                    elif old_val == True and state[uu][pp] == False:
                        cnt_losing[par][p2] += 1
                    else:
                        continue
                    val = cnt_losing[par][p2] > 0
                    if state[par][p2] != val:
                        set_state(par,p2,val)

        # For query type 2 u: print YES if state[u][0] == True else NO

        for __ in range(q):
            x,u = map(int, input().split())
            u -= 1
            if x == 1:
                color_red(u)
            else:
                print("YES" if state[u][0] else "NO")

threading.Thread(target=main).start()