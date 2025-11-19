def maximize_string(N, M, S, T):
    S = list(S)  # Convert S to a list for mutability
    T = sorted(T, reverse=True)  # Sort T in descending order to maximize the value
    
    j = 0  # Pointer for T
    for i in range(N):
        if j < M and T[j] > S[i]:
            S[i] = T[j]  # Replace S[i] with T[j] if T[j] is greater
            j += 1  # Move to the next character in T
    
    return ''.join(S)  # Join the list back into a string

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