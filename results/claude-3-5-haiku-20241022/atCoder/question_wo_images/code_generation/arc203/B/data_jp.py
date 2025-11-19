def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Check if sum of A equals sum of B
    if sum(a) != sum(b):
        print("No")
        return
    
    # If A already equals B
    if a == b:
        print("Yes")
        return
    
    # Build canonical forms using BFS
    from collections import deque
    
    def to_tuple(lst):
        return tuple(lst)
    
    # BFS from A
    visited_a = {to_tuple(a)}
    queue_a = deque([a[:]])
    
    # BFS from B
    visited_b = {to_tuple(b)}
    queue_b = deque([b[:]])
    
    # Bidirectional BFS
    for _ in range(7):  # Limit iterations
        if len(queue_a) == 0 or len(queue_b) == 0:
            break
            
        # Expand from smaller set
        if len(visited_a) <= len(visited_b):
            new_queue = deque()
            while queue_a:
                current = queue_a.popleft()
                
                # Generate all possible next states
                for a_idx in range(n):
                    for b_idx in range(a_idx, n):
                        sum_ab = sum(current[a_idx:b_idx+1])
                        
                        for c_idx in range(b_idx+1, n):
                            for d_idx in range(c_idx, n):
                                sum_cd = sum(current[c_idx:d_idx+1])
                                
                                if sum_ab == sum_cd:
                                    # Perform swap
                                    new_state = (current[:a_idx] + 
                                               current[c_idx:d_idx+1] + 
                                               current[b_idx+1:c_idx] + 
                                               current[a_idx:b_idx+1] + 
                                               current[d_idx+1:])
                                    
                                    new_tuple = to_tuple(new_state)
                                    if new_tuple in visited_b:
                                        print("Yes")
                                        return
                                    
                                    if new_tuple not in visited_a:
                                        visited_a.add(new_tuple)
                                        new_queue.append(new_state)
            
            queue_a = new_queue
        else:
            new_queue = deque()
            while queue_b:
                current = queue_b.popleft()
                
                # Generate all possible next states
                for a_idx in range(n):
                    for b_idx in range(a_idx, n):
                        sum_ab = sum(current[a_idx:b_idx+1])
                        
                        for c_idx in range(b_idx+1, n):
                            for d_idx in range(c_idx, n):
                                sum_cd = sum(current[c_idx:d_idx+1])
                                
                                if sum_ab == sum_cd:
                                    # Perform swap
                                    new_state = (current[:a_idx] + 
                                               current[c_idx:d_idx+1] + 
                                               current[b_idx+1:c_idx] + 
                                               current[a_idx:b_idx+1] + 
                                               current[d_idx+1:])
                                    
                                    new_tuple = to_tuple(new_state)
                                    if new_tuple in visited_a:
                                        print("Yes")
                                        return
                                    
                                    if new_tuple not in visited_b:
                                        visited_b.add(new_tuple)
                                        new_queue.append(new_state)
            
            queue_b = new_queue
    
    print("No")

t = int(input())
for _ in range(t):
    solve()