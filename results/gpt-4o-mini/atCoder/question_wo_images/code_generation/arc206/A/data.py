def count_unique_sequences(N, A):
    unique_values = set(A)
    count = 0
    last_value = None
    
    for i in range(N):
        if A[i] != last_value:
            count += 1
            last_value = A[i]
    
    return count + len(unique_values) - 1

import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:N+1]))

print(count_unique_sequences(N, A))