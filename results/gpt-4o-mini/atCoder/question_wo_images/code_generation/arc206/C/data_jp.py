def count_good_sequences(N, A):
    MOD = 998244353
    
    # Count the number of fixed values and the number of -1s
    fixed_values = set()
    count_neg_ones = 0
    
    for value in A:
        if value == -1:
            count_neg_ones += 1
        else:
            fixed_values.add(value)
    
    # The number of unique values that can be used to fill -1s
    unique_values = N - len(fixed_values)
    
    # If there are no -1s, we need to check if the current array is good
    if count_neg_ones == 0:
        return 1 if is_good_sequence(A) else 0
    
    # Calculate the number of ways to fill -1s
    # Each -1 can be filled with any of the unique values
    return pow(unique_values, count_neg_ones, MOD)

def is_good_sequence(A):
    N = len(A)
    for l in range(N):
        for r in range(l, N):
            if not can_form_tree(A, l, r):
                return False
    return True

def can_form_tree(A, l, r):
    # Check if we can form a tree with the vertices from l to r
    vertices = set(range(l + 1, r + 2))  # 1-based index
    edges = set()
    
    for i in range(l, r + 1):
        if A[i] != -1:
            edges.add((i + 1, A[i]))  # (vertex, A[vertex])
    
    # Check if we can find a vertex x in [l, r] such that all other vertices are connected
    for x in range(l + 1, r + 2):
        connected = set()
        for i in range(l, r + 1):
            if i + 1 != x:
                connected.add(i + 1)
                if A[i] != -1:
                    connected.add(A[i])
        
        if connected == vertices:
            return True
    
    return False

# Input reading
N = int(input().strip())
A = list(map(int, input().strip().split()))

# Output the result
print(count_good_sequences(N, A))