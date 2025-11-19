import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    idx = 0
    
    N = int(input[idx])
    idx += 1
    
    A = list(map(int, input[idx:idx+N]))
    idx += N
    
    B = list(map(int, input[idx:idx+N]))
    idx += N
    
    C = list(map(int, input[idx:idx+N]))
    
    # Find positions where A differs from B
    diff_positions = []
    for i in range(N):
        if A[i] != B[i]:
            diff_positions.append(i)
    
    if not diff_positions:
        print(0)
        return
    
    m = len(diff_positions)
    
    # BFS to find minimum cost
    # State: tuple of current A values (only at diff_positions matter)
    initial_state = tuple(A[i] for i in diff_positions)
    target_state = tuple(B[i] for i in diff_positions)
    
    if initial_state == target_state:
        print(0)
        return
    
    # Use BFS with cost tracking
    from heapq import heappush, heappop
    
    # Dijkstra's algorithm
    visited = {}
    pq = [(0, tuple(A))]
    visited[tuple(A)] = 0
    
    while pq:
        cost, state = heappop(pq)
        
        if cost > visited.get(state, float('inf')):
            continue
        
        # Check if we reached target
        if state == tuple(B):
            print(cost)
            return
        
        # Try flipping each position where state differs from B
        state_list = list(state)
        for i in range(N):
            if state_list[i] != B[i]:
                # Flip position i
                new_state = state_list[:]
                new_state[i] = 1 - new_state[i]
                
                # Calculate cost
                flip_cost = sum(new_state[k] * C[k] for k in range(N))
                new_cost = cost + flip_cost
                
                new_state_tuple = tuple(new_state)
                
                if new_state_tuple not in visited or visited[new_state_tuple] > new_cost:
                    visited[new_state_tuple] = new_cost
                    heappush(pq, (new_cost, new_state_tuple))
    
    print(0)

solve()