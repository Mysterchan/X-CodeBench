def shortest_repeated_subarray_length(N, A):
    index_map = {}
    min_length = float('inf')

    for i in range(N):
        if A[i] in index_map:
            # Calculate the length of the subarray
            length = i - index_map[A[i]] + 1
            min_length = min(min_length, length)
        
        # Update the last seen index of the current element
        index_map[A[i]] = i

    return min_length if min_length != float('inf') else -1

# Read input
N = int(input().strip())
A = list(map(int, input().strip().split()))

# Get the result and print it
result = shortest_repeated_subarray_length(N, A)
print(result)