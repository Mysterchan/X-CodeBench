def can_form_good_string(N, A):
    # Check if there are any zeros in A
    if all(a == 1 for a in A):
        return "Yes"
    
    # Check for the presence of at least one '1' in A
    for i in range(N):
        if A[i] == 1:
            # Check the next two elements in a circular manner
            if A[i-1] == 1 or A[(i+1) % N] == 1:
                return "Yes"
    
    return "No"

# Read input
N = int(input().strip())
A = list(map(int, input().strip().split()))

# Get the result and print it
result = can_form_good_string(N, A)
print(result)