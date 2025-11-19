def has_multiple_subsequences(N, M, A, B):
    from collections import defaultdict
    
    # Create a mapping of values to their indices in A
    index_map = defaultdict(list)
    for i in range(N):
        index_map[A[i]].append(i)
    
    # To track the last index used for matching B
    last_index = -1
    count = 1  # We start with one valid subsequence
    
    for b in B:
        if b not in index_map:
            return "No"
        
        # Get the list of indices for the current value in B
        indices = index_map[b]
        
        # Find the first index in indices that is greater than last_index
        found = False
        for idx in indices:
            if idx > last_index:
                last_index = idx
                found = True
                break
        
        if not found:
            return "No"
        
        # Check if we can find another valid subsequence
        if len(indices) > 1 and indices[0] > last_index:
            count += 1
            if count >= 2:
                return "Yes"
    
    return "Yes" if count >= 2 else "No"

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
A = list(map(int, data[2:N+2]))
B = list(map(int, data[N+2:N+2+M]))

# Get the result and print it
result = has_multiple_subsequences(N, M, A, B)
print(result)