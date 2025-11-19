def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    # If all are already 1, any string works
    if all(a == 1 for a in A):
        print("Yes")
        return
    
    # Try to find a valid assignment using BFS on possible string configurations
    # Key insight: we only need to try strings that could potentially help
    # Focus on positions with zeros
    
    from collections import deque
    
    # Try a smarter search: for each configuration of critical positions
    # We'll use a more targeted approach
    
    def can_solve(S):
        state = tuple(A)
        visited = {state}
        queue = deque([state])
        
        while queue:
            current = queue.popleft()
            if all(x == 1 for x in current):
                return True
            
            current_list = list(current)
            for i in range(N):
                # Try operation 1: ARC pattern at positions i, i+1, i+2
                if (S[i] == 'A' and S[(i + 1) % N] == 'R' and S[(i + 2) % N] == 'C' 
                    and current_list[i] == 0):
                    new_state = current_list[:]
                    new_state[i] = 1
                    new_state[(i + 1) % N] = 1
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
                
                # Try operation 2: CRA pattern at positions i, i+1, i+2
                if (S[i] == 'C' and S[(i + 1) % N] == 'R' and S[(i + 2) % N] == 'A' 
                    and current_list[i] == 0):
                    new_state = current_list[:]
                    new_state[i] = 1
                    new_state[(i + 1) % N] = 1
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
        
        return False
    
    # Smart enumeration: try promising patterns
    # Try patterns based on zero positions
    from itertools import product
    
    zero_positions = [i for i in range(N) if A[i] == 0]
    
    # For small N or few zeros, we can try strategic patterns
    if N <= 20:
        for S in product('ARC', repeat=N):
            if can_solve(S):
                print("Yes")
                return
    else:
        # For larger N, try heuristic patterns
        patterns = []
        # Try cyclic patterns
        for start in ['ARC', 'RCA', 'CAR', 'CRA', 'RAC', 'ACR']:
            S = (start * ((N // 3) + 1))[:N]
            if can_solve(S):
                print("Yes")
                return
        
        # Try random-ish patterns focusing on coverage
        import random
        random.seed(42)
        for _ in range(1000):
            S = ''.join(random.choice('ARC') for _ in range(N))
            if can_solve(S):
                print("Yes")
                return
    
    print("No")

solve()