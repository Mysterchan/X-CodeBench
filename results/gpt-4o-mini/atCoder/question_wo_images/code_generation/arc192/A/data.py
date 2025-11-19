def is_good_string_possible(N, A):
    # If there are no zeros in A, any string is good
    if all(a == 1 for a in A):
        return "Yes"
    
    # Check for the presence of at least one '1' in A
    # and if there are at least two '0's that are adjacent
    for i in range(N):
        if A[i] == 0:
            if A[(i + 1) % N] == 1 or A[(i - 1) % N] == 1:
                return "Yes"
    
    return "No"

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

# Get the result and print it
result = is_good_string_possible(N, A)
print(result)