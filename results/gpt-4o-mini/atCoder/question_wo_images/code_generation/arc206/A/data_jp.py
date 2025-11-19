def count_unique_sequences(N, A):
    unique_values = set(A)
    count = 0
    
    for value in unique_values:
        left = 0
        while left < N:
            if A[left] == value:
                right = left
                while right < N and A[right] == value:
                    right += 1
                count += 1  # Count the segment [left, right-1]
                left = right  # Move to the next segment
            else:
                left += 1
    
    return count

# Read input
N = int(input())
A = list(map(int, input().split()))

# Get the result and print it
result = count_unique_sequences(N, A)
print(result)