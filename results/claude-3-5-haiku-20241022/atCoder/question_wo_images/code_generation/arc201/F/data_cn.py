def solve_case():
    n = int(input())
    writers = []
    for _ in range(n):
        a, b, c, d, e = map(int, input().split())
        writers.append((a, b, c, d, e))
    
    results = []
    total_div1 = 0
    total_div2 = 0
    total_div3 = 0
    
    for k in range(n):
        a, b, c, d, e = writers[k]
        
        # Each writer can contribute to Div.1, Div.2, Div.3
        div1 = min(a, b, c)
        div2 = min(b, c, d)
        div3 = min(c, d, e)
        
        total_div1 += div1
        total_div2 += div2
        total_div3 += div3
        
        # After assigning optimally, we need to maximize C3C events
        # Each C3C needs 1 Div.1, 1 Div.2, 1 Div.3
        # But we need to be careful about resource constraints
        
        # Binary search on the number of C3C events
        left, right = 0, (total_div1 + total_div2 + total_div3) // 3
        
        while left < right:
            mid = (left + right + 1) // 2
            
            # Check if we can hold mid C3C events
            # We need mid Div.1, mid Div.2, mid Div.3
            if mid <= total_div1 and mid <= total_div2 and mid <= total_div3:
                # Check if we have enough resources
                needed_b = 0
                needed_c = 0
                needed_d = 0
                
                for i in range(k + 1):
                    a_i, b_i, c_i, d_i, e_i = writers[i]
                    needed_b += min(a_i, b_i, c_i) + min(b_i, c_i, d_i)
                    needed_c += min(a_i, b_i, c_i) + min(b_i, c_i, d_i) + min(c_i, d_i, e_i)
                    needed_d += min(b_i, c_i, d_i) + min(c_i, d_i, e_i)
                
                total_b = sum(writers[i][1] for i in range(k + 1))
                total_c = sum(writers[i][2] for i in range(k + 1))
                total_d = sum(writers[i][3] for i in range(k + 1))
                
                if 2 * mid <= total_b and 3 * mid <= total_c and 2 * mid <= total_d:
                    left = mid
                else:
                    right = mid - 1
            else:
                right = mid - 1
        
        results.append(left)
    
    print(' '.join(map(str, results)))

t = int(input())
for _ in range(t):
    solve_case()