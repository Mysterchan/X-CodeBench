def shortest_repeating_subarray_length(N, A):
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
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))

# Get the result and print it
result = shortest_repeating_subarray_length(N, A)
print(result)