def maximize_string(N, M, S, T):
    S = list(S)  # Convert string S to a list for mutability
    for k in range(M):
        # For each character in T, replace the first character in S that is less than T[k]
        for i in range(N):
            if S[i] < T[k]:
                S[i] = T[k]
                break  # Only replace the first valid character
    return ''.join(S)  # Convert list back to string

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
S = data[2]
T = data[3]

# Get the result and print it
result = maximize_string(N, M, S, T)
print(result)