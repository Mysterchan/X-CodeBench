def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        writers = []
        for i in range(N):
            A, B, C, D, E = map(int, input().split())
            writers.append((A, B, C, D, E))
        
        results = []
        
        # Accumulate totals for each difficulty
        total_A = 0
        total_B = 0
        total_C = 0
        total_D = 0
        total_E = 0
        
        for k in range(N):
            A, B, C, D, E = writers[k]
            total_A += A
            total_B += B
            total_C += C
            total_D += D
            total_E += E
            
            # Binary search for maximum number of contests
            left, right = 0, 10**18
            
            while left < right:
                mid = (left + right + 1) // 2
                
                # Check if we can hold mid contests
                # Div1 needs: Hell, Hard, Medium
                # Div2 needs: Hard, Medium, Easy
                # Div3 needs: Medium, Easy, Baby
                
                # Let x1, x2, x3 be the number of Div1, Div2, Div3 contests
                # x1 + x2 + x3 = mid
                # x1 <= total_A (Hell)
                # x1 + x2 <= total_B (Hard)
                # x1 + x2 + x3 <= total_C (Medium)
                # x2 + x3 <= total_D (Easy)
                # x3 <= total_E (Baby)
                
                # We need to check if there exist x1, x2, x3 >= 0 satisfying all constraints
                
                can_hold = False
                
                # Try all possible values of x1 from 0 to min(mid, total_A)
                for x1 in range(min(mid, total_A) + 1):
                    remaining = mid - x1
                    
                    # x2 + x3 = remaining
                    # x2 <= total_B - x1
                    # x2 + x3 <= total_C - x1
                    # x2 + x3 <= total_D
                    # x3 <= total_E
                    
                    if remaining > total_C - x1 or remaining > total_D:
                        continue
                    
                    # x2 + x3 = remaining
                    # x2 <= total_B - x1
                    # x3 <= total_E
                    
                    # x3 = remaining - x2
                    # remaining - x2 <= total_E
                    # x2 >= remaining - total_E
                    
                    min_x2 = max(0, remaining - total_E)
                    max_x2 = min(remaining, total_B - x1)
                    
                    if min_x2 <= max_x2:
                        can_hold = True
                        break
                
                if can_hold:
                    left = mid
                else:
                    right = mid - 1
            
            results.append(left)
        
        print(' '.join(map(str, results)))

solve()