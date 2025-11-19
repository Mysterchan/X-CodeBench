import bisect

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Collect all unique values for coordinate compression
    all_values = sorted(set(a))
    val_to_idx = {v: i for i, v in enumerate(all_values)}
    
    # Precompute LIS for each prefix and each value threshold
    # lis[i][j] = LIS length for prefix a[0:i+1] with elements <= all_values[j]
    m = len(all_values)
    
    # For each position, store LIS length for each value threshold
    lis_at_pos = []
    
    for i in range(n):
        if i == 0:
            # First element
            curr = [0] * m
            val_idx = val_to_idx[a[i]]
            for j in range(val_idx, m):
                curr[j] = 1
            lis_at_pos.append(curr)
        else:
            curr = lis_at_pos[-1][:]
            val_idx = val_to_idx[a[i]]
            
            # Update LIS for thresholds >= a[i]
            if val_idx > 0:
                prev_lis = curr[val_idx - 1]
            else:
                prev_lis = 0
            
            new_lis = prev_lis + 1
            for j in range(val_idx, m):
                curr[j] = max(curr[j], new_lis)
            
            lis_at_pos.append(curr)
    
    # Answer queries
    for _ in range(q):
        r, x = map(int, input().split())
        r -= 1  # Convert to 0-indexed
        
        # Binary search for largest value <= x
        idx = bisect.bisect_right(all_values, x) - 1
        
        if idx < 0:
            print(0)
        else:
            print(lis_at_pos[r][idx])

solve()