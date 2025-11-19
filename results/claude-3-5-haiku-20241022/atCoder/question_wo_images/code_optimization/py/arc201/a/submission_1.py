import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

for _ in range(int(input())):
    n = int(input())
    writers = []
    for i in range(n):
        a, b, c = map(int, input().split())
        writers.append((a, b, c))
    
    # Binary search on answer
    l, h = 0, 5 * 10 ** 9 + 1
    
    while h - l > 1:
        m = (l + h) // 2
        
        # Check if we can hold m contests
        div1_count = 0
        div2_count = 0
        
        # For Div.1: need m pairs of (A, B)
        # Strategy: First allocate B's where B > C (prioritize Div.1)
        # Then allocate remaining B's as needed
        for i in range(n):
            a, b, c = writers[i]
            # First, pair A with B where we have excess B over C
            excess_b = max(0, b - c)
            pairs = min(a, excess_b)
            div1_count += pairs
            a -= pairs
            b -= pairs
        
        # Now allocate more for Div.1 if needed
        if div1_count < m:
            for i in range(n):
                a, b, c = writers[i]
                # Recalculate available after first pass
                excess_b = max(0, b - c)
                pairs_used = min(a, excess_b)
                a -= pairs_used
                b -= pairs_used
                
                # Allocate more pairs
                additional = min(m - div1_count, a, b)
                div1_count += additional
                b -= additional
                if div1_count >= m:
                    break
        
        # For Div.2: count available (B, C) pairs after Div.1 allocation
        for i in range(n):
            a, b, c = writers[i]
            # Calculate remaining B after Div.1
            excess_b = max(0, b - c)
            div1_used_b = min(a, excess_b)
            remaining_b = b - div1_used_b
            
            if div1_count >= m:
                # Need to recalculate based on actual Div.1 usage
                pass
            
            div2_count += min(remaining_b, c)
        
        # Simplified check
        if div1_count >= m and div2_count >= m:
            l = m
        else:
            h = m
    
    print(l)