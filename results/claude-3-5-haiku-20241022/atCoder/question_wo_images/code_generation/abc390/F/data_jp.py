def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    total = 0
    
    for L in range(N):
        for R in range(L, N):
            # Calculate f(L, R)
            subarray = A[L:R+1]
            
            # Count the number of distinct contiguous ranges
            # We need to find the minimum number of operations
            # which is equivalent to finding the number of maximal contiguous ranges
            
            # Sort the subarray with their original indices
            indexed = [(subarray[i], i) for i in range(len(subarray))]
            indexed.sort()
            
            operations = 0
            i = 0
            while i < len(indexed):
                # Start a new contiguous range
                operations += 1
                current_val = indexed[i][0]
                max_idx = indexed[i][1]
                min_idx = indexed[i][1]
                i += 1
                
                # Extend the range as much as possible
                while i < len(indexed) and indexed[i][0] <= current_val + (max_idx - min_idx + 1):
                    # Check if we can include this value
                    new_idx = indexed[i][1]
                    new_val = indexed[i][0]
                    
                    # Update range
                    new_min_idx = min(min_idx, new_idx)
                    new_max_idx = max(max_idx, new_idx)
                    
                    # Check if all values in [current_val, new_val] are covered by indices [new_min_idx, new_max_idx]
                    if new_val <= current_val + (new_max_idx - new_min_idx + 1):
                        min_idx = new_min_idx
                        max_idx = new_max_idx
                        current_val = new_val
                        i += 1
                    else:
                        break
            
            total += operations
    
    print(total)

solve()