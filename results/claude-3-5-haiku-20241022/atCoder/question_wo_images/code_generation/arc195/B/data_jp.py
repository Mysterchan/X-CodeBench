def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # Count -1s
    a_neg_count = sum(1 for x in A if x == -1)
    b_neg_count = sum(1 for x in B if x == -1)
    
    # Get non-negative values
    a_vals = [x for x in A if x >= 0]
    b_vals = [x for x in B if x >= 0]
    
    # Check if all pairs have -1 in either A or B (both are -1 is also ok)
    all_have_neg = all(A[i] == -1 or B[i] == -1 for i in range(N))
    
    if all_have_neg:
        # We can choose any target sum and set values appropriately
        print("Yes")
        return
    
    # Compute possible sums for fixed positions (where both A[i] and B[i] are non-negative)
    fixed_sums = []
    for i in range(N):
        if A[i] >= 0 and B[i] >= 0:
            fixed_sums.append(A[i] + B[i])
    
    # If there are fixed sums, they must all be equal
    if fixed_sums:
        if len(set(fixed_sums)) > 1:
            print("No")
            return
        target_sum = fixed_sums[0]
    else:
        # No fixed sums, we need to determine target_sum
        # Try to find a valid target_sum
        target_sum = None
    
    # Count positions by type
    both_fixed = sum(1 for i in range(N) if A[i] >= 0 and B[i] >= 0)
    a_fixed_b_neg = sum(1 for i in range(N) if A[i] >= 0 and B[i] == -1)
    a_neg_b_fixed = sum(1 for i in range(N) if A[i] == -1 and B[i] >= 0)
    both_neg = sum(1 for i in range(N) if A[i] == -1 and B[i] == -1)
    
    if target_sum is not None:
        # Check if we can match with target_sum
        # For positions with A[i] fixed and B[i] = -1: need B[i] = target_sum - A[i] >= 0
        # For positions with B[i] fixed and A[i] = -1: need A[i] = target_sum - B[i] >= 0
        
        a_fixed_vals = []
        for i in range(N):
            if A[i] >= 0 and B[i] == -1:
                if A[i] > target_sum:
                    print("No")
                    return
                a_fixed_vals.append(A[i])
        
        b_fixed_vals = []
        for i in range(N):
            if B[i] >= 0 and A[i] == -1:
                if B[i] > target_sum:
                    print("No")
                    return
                b_fixed_vals.append(B[i])
        
        # We need to match a_fixed_vals with some permutation of needed values
        # For each a_fixed_vals[j], we need to find a B value such that a_fixed_vals[j] + B = target_sum
        # This B value must come from either:
        # - Rearranging values from b_fixed positions (target_sum - b_fixed_vals[k])
        # - Setting both_neg positions
        
        needed_b_vals = [target_sum - a for a in a_fixed_vals]
        available_a_vals = [target_sum - b for b in b_fixed_vals]
        
        # Check if we can match needed_b_vals with available_a_vals + both_neg flexibility
        needed_b_vals.sort()
        available_a_vals.sort()
        
        # Greedy matching
        j = 0
        for needed in needed_b_vals:
            if j < len(available_a_vals) and available_a_vals[j] == needed:
                j += 1
            elif both_neg > 0:
                both_neg -= 1
            else:
                print("No")
                return
        
        # Remaining available_a_vals and both_neg must match b_fixed_vals
        remaining = len(available_a_vals) - j + both_neg
        if remaining == len(b_fixed_vals):
            print("Yes")
        else:
            print("No")
    else:
        # No fixed sum constraint, need at least one to determine target
        print("Yes")

solve()