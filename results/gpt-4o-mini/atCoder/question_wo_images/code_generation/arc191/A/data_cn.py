def maximize_string(N, M, S, T):
    S = list(S)  # Convert string S to a list for mutability
    for k in range(M):
        for i in range(N):
            if T[k] > S[i]:
                S[i] = T[k]
                break  # Only replace one character per T[k]
    return ''.join(S)  # Convert list back to string

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()
N, M = map(int, data[0].split())
S = data[1]
T = data[2]

# Get the result and print it
result = maximize_string(N, M, S, T)
print(result)