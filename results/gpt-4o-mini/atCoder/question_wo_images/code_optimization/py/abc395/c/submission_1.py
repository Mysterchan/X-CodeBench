N = int(input())
A = list(map(int, input().split()))

# Dictionary to store the last index of each element
last_index = {}
min_length = float('inf')

for i in range(N):
    if A[i] in last_index:
        # Found a repeated value
        subarray_length = i - last_index[A[i]] + 1
        if subarray_length < min_length:
            min_length = subarray_length
    # Update the last index of the current element
    last_index[A[i]] = i

# Print the result
print(min_length if min_length != float('inf') else -1)