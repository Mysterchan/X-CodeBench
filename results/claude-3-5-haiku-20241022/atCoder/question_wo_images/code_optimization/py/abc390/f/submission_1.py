def compute_f_values():
    N = int(input())
    A = list(map(int, input().split()))
    
    total = 0
    
    for L in range(N):
        present = set()
        min_val = float('inf')
        max_val = float('-inf')
        
        for R in range(L, N):
            val = A[R]
            
            if val not in present:
                present.add(val)
                min_val = min(min_val, val)
                max_val = max(max_val, val)
            
            # Count gaps: number of missing values in [min_val, max_val]
            gaps = (max_val - min_val + 1) - len(present)
            f_val = gaps + 1
            
            total += f_val
    
    print(total)

compute_f_values()