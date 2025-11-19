def solve():
    n = int(input())
    authors = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        authors.append((a, b, c))
    
    # Binary search on the answer
    def can_hold(k):
        # Check if we can hold k C2C competitions
        # We need k Div.1 (each needs 1 hard + 1 medium from same author)
        # We need k Div.2 (each needs 1 medium + 1 easy from same author)
        
        # For each author, we can contribute:
        # - min(a[i], b[i]) Div.1 competitions
        # - min(b[i], c[i]) Div.2 competitions
        # But b[i] is shared, so we need to allocate optimally
        
        # Greedy approach: for each author, decide how many Div.1 and Div.2 to make
        # Let x_i be Div.1 from author i, y_i be Div.2 from author i
        # Constraints: x_i <= a[i], y_i <= c[i], x_i + y_i <= b[i]
        # We want sum(x_i) >= k and sum(y_i) >= k
        
        # For each author, maximize contribution
        total_div1 = 0
        total_div2 = 0
        
        for a, b, c in authors:
            # Try to satisfy both as much as possible
            # We can make at most min(a, b) Div.1 and min(b, c) Div.2
            # But they share b medium problems
            
            # Strategy: allocate b optimally between Div.1 and Div.2
            max_div1 = min(a, b)
            max_div2 = min(b, c)
            
            # We want to contribute to both if possible
            # If we use x for Div.1 and y for Div.2, we need x + y <= b
            # and x <= a, y <= c
            
            # Best strategy: contribute as much as possible to the limiting resource
            # Try to balance: give k - total_div1 to Div.1 if needed, etc.
            
            # For now, simple greedy: maximize min(contribution to div1, contribution to div2)
            # Actually, we need sum of div1 >= k and sum of div2 >= k
            # So we should maximize total contribution
            
            contrib_div1 = min(a, b)
            contrib_div2 = min(c, b)
            
            # If both fit within b
            if contrib_div1 + contrib_div2 <= b:
                total_div1 += contrib_div1
                total_div2 += contrib_div2
            else:
                # Need to share b
                # Allocate to maximize minimum or to reach k
                # For binary search, we want to check if we can reach k
                # Prioritize the one that's further from k
                
                # Simple approach: split proportionally or greedily
                # Use min(contrib_div1, b) for div1, rest for div2
                used_div1 = min(contrib_div1, b)
                remaining_b = b - used_div1
                used_div2 = min(contrib_div2, remaining_b)
                
                # Or try the other way
                used_div2_alt = min(contrib_div2, b)
                remaining_b_alt = b - used_div2_alt
                used_div1_alt = min(contrib_div1, remaining_b_alt)
                
                # Choose the allocation that helps us reach k better
                # For binary search, we want both >= k eventually
                # So we should balance contributions
                
                total_div1 += max(used_div1, used_div1_alt)
                total_div2 += max(used_div2, used_div2_alt)
        
        return total_div1 >= k and total_div2 >= k
    
    # Better approach: for each k, optimally allocate
    def can_hold_optimal(k):
        total_div1 = 0
        total_div2 = 0
        
        for a, b, c in authors:
            max_div1 = min(a, b)
            max_div2 = min(c, b)
            
            if max_div1 + max_div2 <= b:
                total_div1 += max_div1
                total_div2 += max_div2
            else:
                # We have more potential than b allows
                # Allocate b optimally
                # Give priority to the one that needs it more
                need_div1 = max(0, k - total_div1)
                need_div2 = max(0, k - total_div2)
                
                if need_div1 >= need_div2:
                    alloc_div1 = min(max_div1, b)
                    alloc_div2 = min(max_div2, b - alloc_div1)
                else:
                    alloc_div2 = min(max_div2, b)
                    alloc_div1 = min(max_div1, b - alloc_div2)
                
                total_div1 += alloc_div1
                total_div2 += alloc_div2
        
        return total_div1 >= k and total_div2 >= k
    
    left, right = 0, 5 * 10**9
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_hold_optimal(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer

t = int(input())
for _ in range(t):
    print(solve())