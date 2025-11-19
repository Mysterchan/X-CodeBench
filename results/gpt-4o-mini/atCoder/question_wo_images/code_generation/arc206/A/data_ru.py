def count_unique_sequences(N, A):
    unique_values = set()
    last_value = None
    for i in range(N):
        if A[i] != last_value:
            unique_values.add(A[i])
            last_value = A[i]
    return len(unique_values)

import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:N+1]))

result = count_unique_sequences(N, A)
print(result)