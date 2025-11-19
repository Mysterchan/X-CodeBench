def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # Count -1s in A and B
    a_minus_ones = sum(1 for x in A if x == -1)
    b_minus_ones = sum(1 for x in B if x == -1)
    
    # Extract non -1 values
    a_vals = [x for x in A if x != -1]
    b_vals = [x for x in B if x != -1]
    
    # Try different target sums
    # The target sum should be at least max of all known values
    possible_targets = set()
    
    # If all are -1, any target works
    if len(a_vals) == 0 and len(b_vals) == 0:
        print("Yes")
        return
    
    # Collect all known values to determine possible targets
    all_vals = a_vals + b_vals
    if all_vals:
        max_val = max(all_vals)
    else:
        max_val = 0
    
    # Try targets from max_val to max_val + some reasonable range
    # For each B[i], we need A[i] = target - B[i]
    # For each A[i], we need B[i] = target - A[i]
    
    # Calculate required pairs
    for target in range(max_val, max_val + 2001):
        # For each B[i] != -1, calculate required A value
        required_a = []
        free_b_positions = []
        
        valid = True
        for i in range(N):
            if B[i] != -1:
                needed = target - B[i]
                if needed < 0:
                    valid = False
                    break
                required_a.append(needed)
            else:
                free_b_positions.append(i)
        
        if not valid:
            continue
        
        # For each A[i] != -1, calculate required B value
        required_b = []
        free_a_positions = []
        
        for i in range(N):
            if A[i] != -1:
                needed = target - A[i]
                if needed < 0:
                    valid = False
                    break
                required_b.append(needed)
            else:
                free_a_positions.append(i)
        
        if not valid:
            continue
        
        # Now check if we can match
        # We have a_vals (non -1 A values) and required_a (what A needs for non -1 B)
        # We need to check if a_vals can be rearranged to cover required_a
        
        from collections import Counter
        
        a_counter = Counter(a_vals)
        required_a_counter = Counter(required_a)
        
        # Check if required_a can be satisfied by a_vals
        remaining_a = a_counter.copy()
        for val, cnt in required_a_counter.items():
            if remaining_a[val] < cnt:
                # Not enough of this value, need to use -1s
                deficit = cnt - remaining_a[val]
                if deficit > a_minus_ones:
                    valid = False
                    break
                a_minus_ones -= deficit
                remaining_a[val] = 0
            else:
                remaining_a[val] -= cnt
        
        if not valid:
            continue
        
        # Check B side
        b_counter = Counter(b_vals)
        required_b_counter = Counter(required_b)
        
        remaining_b = b_counter.copy()
        temp_b_minus = b_minus_ones
        for val, cnt in required_b_counter.items():
            if remaining_b[val] < cnt:
                deficit = cnt - remaining_b[val]
                if deficit > temp_b_minus:
                    valid = False
                    break
                temp_b_minus -= deficit
                remaining_b[val] = 0
            else:
                remaining_b[val] -= cnt
        
        if valid:
            print("Yes")
            return
    
    print("No")

solve()