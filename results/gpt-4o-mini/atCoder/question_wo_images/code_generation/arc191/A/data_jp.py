def maximize_string(N, M, S, T):
    S = list(S)  # Convert to list for mutability
    T = sorted(T, reverse=True)  # Sort T in descending order

    j = 0  # Pointer for T
    for i in range(N):
        if j < M and S[i] < T[j]:
            S[i] = T[j]
            j += 1

    return ''.join(S)

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
S = data[1]
T = data[2]

# Get the result and print it
result = maximize_string(N, M, S, T)
print(result)