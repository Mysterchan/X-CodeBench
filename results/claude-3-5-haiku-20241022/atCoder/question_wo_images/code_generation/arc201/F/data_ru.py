def solve_case():
    n = int(input())
    authors = []
    for _ in range(n):
        a, b, c, d, e = map(int, input().split())
        authors.append((a, b, c, d, e))
    
    results = []
    
    # Track cumulative resources
    total_a = 0
    total_b = 0
    total_c = 0
    total_d = 0
    total_e = 0
    
    for k in range(n):
        a, b, c, d, e = authors[k]
        total_a += a
        total_b += b
        total_c += c
        total_d += d
        total_e += e
        
        # Binary search for maximum number of C3C
        left, right = 0, 10**18
        
        while left < right:
            mid = (left + right + 1) // 2
            
            # Check if we can conduct mid C3Cs
            # We need: mid Div.1, mid Div.2, mid Div.3
            # Div.1: mid A, mid B, mid C
            # Div.2: mid B, mid C, mid D
            # Div.3: mid C, mid D, mid E
            
            # Total needs:
            # A: mid
            # B: 2*mid
            # C: 3*mid
            # D: 2*mid
            # E: mid
            
            need_a = mid
            need_b = 2 * mid
            need_c = 3 * mid
            need_d = 2 * mid
            need_e = mid
            
            if (total_a >= need_a and 
                total_b >= need_b and 
                total_c >= need_c and 
                total_d >= need_d and 
                total_e >= need_e):
                left = mid
            else:
                right = mid - 1
        
        results.append(left)
    
    print(' '.join(map(str, results)))

t = int(input())
for _ in range(t):
    solve_case()