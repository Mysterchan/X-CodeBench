def count_good_sequences(N, A):
    MOD = 998244353
    
    # Count the number of -1s and the set of fixed values
    count_neg_one = 0
    fixed_values = set()
    
    for value in A:
        if value == -1:
            count_neg_one += 1
        else:
            fixed_values.add(value)
    
    # If there are no -1s, we need to check if the current sequence is good
    if count_neg_one == 0:
        return 1 if is_good_sequence(A) else 0
    
    # Calculate the number of valid replacements
    total_ways = 0
    for x in range(1, N + 1):
        if x not in fixed_values:
            total_ways += pow(len(fixed_values) + 1, count_neg_one, MOD)
            total_ways %= MOD
    
    return total_ways

def is_good_sequence(A):
    N = len(A)
    for l in range(N):
        for r in range(l, N):
            if not can_form_tree(A, l, r):
                return False
    return True

def can_form_tree(A, l, r):
    # Check if we can form a tree in the range A[l:r+1]
    seen = set()
    for i in range(l, r + 1):
        if A[i] != -1:
            seen.add(A[i])
    
    # We need at least one x in the range [l, r] that can connect all others
    return len(seen) <= (r - l + 1)

# Read input
N = int(input().strip())
A = list(map(int, input().strip().split()))

# Get the result
result = count_good_sequences(N, A)

# Print the result
print(result)