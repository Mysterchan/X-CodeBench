import sys
from bisect import bisect_right

input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])
A = list(map(int, data[2:N+2]))

results = []

queries = []
for i in range(Q):
    R = int(data[N+2 + 2*i])
    X = int(data[N+2 + 2*i + 1])
    queries.append((R, X, i))

# Process queries and sort them
queries.sort(key=lambda x: (x[0], x[1]))

# Prepare a list to handle the subsequence lengths
lis = []
max_length = [0] * (N + 1)

current_index = 0

# Answer each query
for R, X, original_index in queries:
    # Process elements up to R
    while current_index < R:
        if A[current_index] <= X:
            pos = bisect_right(lis, A[current_index])
            if pos == len(lis):
                lis.append(A[current_index])
            else:
                lis[pos] = A[current_index]
        current_index += 1
    
    # The length of the longest increasing subsequence
    max_length[original_index] = len(lis)

# Print out the results in the original order
print("\n".join(map(str, max_length[:Q])))