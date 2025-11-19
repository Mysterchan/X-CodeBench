N = int(input())
A = list(map(int, input().split()))

# Check if all are already 1
if all(a == 1 for a in A):
    print("Yes")
else:
    # Check for 3 or more consecutive 0s in circular array
    A_circular = A + A  # Make it circular by doubling
    
    max_consecutive_zeros = 0
    current_zeros = 0
    
    for i in range(len(A_circular)):
        if A_circular[i] == 0:
            current_zeros += 1
            max_consecutive_zeros = max(max_consecutive_zeros, current_zeros)
        else:
            current_zeros = 0
        
        # Only need to check up to N positions for circular property
        if i >= N:
            break
    
    # Also check if all are 0s
    if all(a == 0 for a in A):
        print("No")
    elif max_consecutive_zeros >= 3:
        print("No")
    else:
        print("Yes")