def solve_case():
    n = int(input())
    writers = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        writers.append((a, b, c))
    
    # Binary search on the answer
    left, right = 0, 10**18
    
    def can_hold(k):
        # Check if we can hold k C2C contests
        # For each writer, decide how many Div.1 and Div.2 to assign
        # Div.1 uses: min(A_i, B_i) hard and medium
        # Div.2 uses: min(B_i, C_i) medium and easy
        
        # We need to maximize total Div.1 + Div.2 >= k
        # Subject to: for each writer i:
        #   d1_i + d2_i <= min(A_i, B_i + ... constraints
        
        # Greedy: try to assign as many as possible
        total_div1 = 0
        total_div2 = 0
        remaining_b = []
        
        for a, b, c in writers:
            # Maximum Div.1 we can make from this writer
            max_div1 = min(a, b)
            # Maximum Div.2 we can make from this writer
            max_div2 = min(b, c)
            
            # Strategy: allocate to meet target k
            # If we allocate x to Div.1 and y to Div.2:
            # x <= min(a, b), y <= min(b, c)
            # x + y <= b (they share medium problems)
            
            # First, try to satisfy as much as needed
            if total_div1 < k:
                need_div1 = k - total_div1
                alloc_div1 = min(need_div1, max_div1)
                total_div1 += alloc_div1
                b_used = alloc_div1
            else:
                alloc_div1 = 0
                b_used = 0
            
            if total_div2 < k:
                need_div2 = k - total_div2
                b_available = b - b_used
                max_div2_now = min(b_available, c)
                alloc_div2 = min(need_div2, max_div2_now)
                total_div2 += alloc_div2
                b_used += alloc_div2
            else:
                alloc_div2 = 0
            
            remaining_b.append((a, b - b_used, c))
        
        # Check if we met the requirement
        if total_div1 >= k and total_div2 >= k:
            return True
        
        # Try to balance by reallocating
        for a, b_rem, c in remaining_b:
            if total_div1 < k and total_div2 >= k:
                add_div1 = min(k - total_div1, min(a, b_rem))
                total_div1 += add_div1
            elif total_div2 < k and total_div1 >= k:
                add_div2 = min(k - total_div2, min(b_rem, c))
                total_div2 += add_div2
        
        return total_div1 >= k and total_div2 >= k
    
    while left < right:
        mid = (left + right + 1) // 2
        if can_hold(mid):
            left = mid
        else:
            right = mid - 1
    
    print(left)

t = int(input())
for _ in range(t):
    solve_case()