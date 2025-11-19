def has_multiple_subsequences(N, M, A, B):
    from collections import defaultdict

    # Step 1: Create a mapping of values in A to their indices
    value_indices = defaultdict(list)
    for index, value in enumerate(A):
        value_indices[value].append(index)

    # Step 2: Check if we can find at least two distinct subsequences matching B
    last_index = -1
    count = 0

    for b in B:
        if b not in value_indices:
            return "No"
        
        # Get the list of indices for the current value in B
        indices = value_indices[b]
        
        # Find the first index that is greater than last_index
        found = False
        for idx in indices:
            if idx > last_index:
                last_index = idx
                found = True
                break
        
        if not found:
            return "No"
        
        # Count how many times we can find this value in A
        count += len(indices) - indices.index(last_index) - 1

    return "Yes" if count > 0 else "No"

# Read input
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Get the result and print it
result = has_multiple_subsequences(N, M, A, B)
print(result)