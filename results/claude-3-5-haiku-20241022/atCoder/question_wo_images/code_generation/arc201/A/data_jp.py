def solve():
    n = int(input())
    writers = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        writers.append((a, b, c))
    
    # Binary search on the number of C2C contests
    def can_hold(k):
        # For each writer, decide how many Div.1 and Div.2 to contribute
        # Div.1 needs: min(A_i, B_i) problems from writer i
        # Div.2 needs: min(B_i, C_i) problems from writer i
        # We need total Div.1 >= k and total Div.2 >= k
        
        # For writer i with (a, b, c):
        # Let x_i = number of Div.1 from writer i
        # Let y_i = number of Div.2 from writer i
        # Constraints:
        # x_i <= min(a, b)
        # y_i <= min(b, c)
        # x_i + y_i <= b (shared Medium constraint)
        # sum(x_i) >= k
        # sum(y_i) >= k
        
        # Greedy approach: maximize min(total_div1, total_div2)
        # For each writer, we can allocate Medium to Div.1 or Div.2
        
        total_div1 = 0
        total_div2 = 0
        
        for a, b, c in writers:
            # Maximum Div.1 this writer can contribute
            max_div1 = min(a, b)
            # Maximum Div.2 this writer can contribute
            max_div2 = min(b, c)
            
            # We want to maximize the minimum of contributions
            # If we allocate x to Div.1 and y to Div.2:
            # x + y <= b, x <= a, y <= c
            
            # Strategy: try to balance or prioritize based on need
            # Greedy: allocate as much as possible to both
            total_div1 += max_div1
            total_div2 += max_div2
        
        # Check if we can redistribute Medium to satisfy k for both
        # Actually, we need a flow-based or greedy reallocation
        
        # Better approach: check if we can get k Div.1 and k Div.2
        # simultaneously with the Medium constraint
        
        need_div1 = k
        need_div2 = k
        
        for a, b, c in writers:
            # Allocate to Div.1 first (greedy)
            div1 = min(a, b, need_div1)
            need_div1 -= div1
            b_remaining = b - div1
            
            # Then allocate to Div.2
            div2 = min(b_remaining, c, need_div2)
            need_div2 -= div2
        
        if need_div1 <= 0 and need_div2 <= 0:
            return True
        
        # Try reverse order
        need_div1 = k
        need_div2 = k
        
        for a, b, c in writers:
            # Allocate to Div.2 first
            div2 = min(b, c, need_div2)
            need_div2 -= div2
            b_remaining = b - div2
            
            # Then allocate to Div.1
            div1 = min(a, b_remaining, need_div1)
            need_div1 -= div1
        
        return need_div1 <= 0 and need_div2 <= 0
    
    left, right = 0, sum(min(a, b, c) for a, b, c in writers)
    
    while left < right:
        mid = (left + right + 1) // 2
        if can_hold(mid):
            left = mid
        else:
            right = mid - 1
    
    print(left)

t = int(input())
for _ in range(t):
    solve()